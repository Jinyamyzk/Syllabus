import collections

# 集計方法1
# f = open('scraping_otocre_word_list_exclude.txt')
# data = f.read()  #ファイルを文字列として取得
#
# 集計 ※dict型を定義してgetメソッドで数える。
# words = {}
# for word in data.split():
#     words[word] = words.get(word, 0) + 1

# 集計方法2 内包表現を使用
path = 'syllabus_word_list_exclude.csv'
with open(path) as f:
    words = [s.strip() for s in f.readlines()]

# 集計処理
## count()を使用
# d = [(v,k) for k,v in words.items()]
# d.sort()
# d.reverse()
# for count, word in d[:10]:
#     print(count, word)

##collections.Counter()を使用
counter = collections.Counter(words)
for word in counter.most_common(100):
    print(word)
