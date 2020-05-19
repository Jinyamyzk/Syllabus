from pathlib import Path
from janome.charfilter import *
from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import *
from gensim import corpora


data_dir_path = Path('.')
corpus_dir_path = Path('.')


file_name = 'syllabus.csv'

with open(data_dir_path.joinpath(file_name), 'r', encoding='utf-8') as file:
    next(file)
    texts = file.readlines()

texts = [text_.replace('\n', '') for text_ in texts]

# janomeのAnalyzerを使うことで、文の分割と単語の正規化をまとめて行うことができる
# 文に対する処理のまとめ
char_filters = [UnicodeNormalizeCharFilter(),         # UnicodeをNFKC(デフォルト)で正規化
                RegexReplaceCharFilter('\(', ''),     # (を削除
                RegexReplaceCharFilter('\)', '')      # )を削除
                ]

# 単語に分割
tokenizer = Tokenizer()

#
# 名詞中の数(漢数字を含む)を全て0に置き換えるTokenFilterの実装
#
class NumericReplaceFilter(TokenFilter):

    def apply(self, tokens):
        for token in tokens:
            parts = token.part_of_speech.split(',')
            if (parts[0] == '名詞' and parts[1] == '数'):
                token.surface = '0'
                token.base_form = '0'
                token.reading = 'ゼロ'
                token.phonetic = 'ゼロ'
            yield token


#
#  ひらがな・カタガナ・英数字の一文字しか無い単語は削除
#
class OneCharacterReplaceFilter(TokenFilter):

    def apply(self, tokens):
        for token in tokens:
            # 上記のルールの一文字制限で引っかかった場合、その単語を無視
            if re.match('^[あ-んア-ンa-zA-Z0-9ー]$', token.surface):
                continue

            yield token


# 単語に対する処理のまとめ
token_filters = [NumericReplaceFilter(),                         # 名詞中の漢数字を含む数字を0に置換
                 CompoundNounFilter(),                           # 名詞が連続する場合は複合名詞にする
#                POSKeepFilter(['名詞', '動詞', '形容詞', '副詞']), # 名詞・動詞・形容詞・副詞のみを取得する
                 POSKeepFilter(['名詞']),                         # 名詞のみを取得する
                 LowerCaseFilter(),                              # 英字は小文字にする
                 OneCharacterReplaceFilter()                     # 一文字しか無いひらがなとカタガナと英数字は削除
                 ]

analyzer = Analyzer(char_filters, tokenizer, token_filters)


tokens_list = []
raw_texts = []
for text in texts:
    # 文を分割し、単語をそれぞれ正規化する
    text_ = [token.base_form for token in analyzer.analyze(text)]
    if len(text_) > 0:
        tokens_list.append([token.base_form for token in analyzer.analyze(text)])
        raw_texts.append(text)

# 正規化された際に一文字もない文の削除後の元テキストデータ
raw_texts = [text_+'\n' for text_ in raw_texts]
with open(data_dir_path.joinpath(file_name.replace('.csv', '_cut.csv')), 'w', encoding='utf-8') as file:
    file.writelines(raw_texts)

# 単語リストの作成
words = []
for text in tokens_list:
    words.extend([word+'\n' for word in text if word != ''])
with open(corpus_dir_path.joinpath(file_name.replace('.csv', '_word_list.csv')), 'w', encoding='utf-8') as file:
    file.writelines(words)



# 単語リストからストップワードを削除
## ストップワードファイルからの呼び込み
stop_words = []
path = 'stopwords_jp.txt'
with open(path) as f:
    stop_words = f.readlines()

## ストップワードの除外

changed_words = [word for word in words if word not in stop_words]
print('-----------------')
print('Delited ' + str(len(words) - len(changed_words)) + ' words' )
print('-----------------')

with open(corpus_dir_path.joinpath(file_name.replace('.csv', '_word_list_exclude.csv')), 'w', encoding='utf-8') as file:
    file.writelines(changed_words)
print(changed_words)
