import csv
from janome.tokenizer import Tokenizer

import pandas as pd
df = pd.read_csv('syllabus_sample.csv', usecols=[0,1])
array = df.values.tolist()

t = Tokenizer()

theme_word_list = []
for row in array:
    token_list = t.tokenize(row[1])
    word_list = []
    word_list.append(row[0])
    for token in token_list:
        if token.part_of_speech.split(',')[0] == u'名詞':
            word_list.append(token.base_form)
    theme_word_list.append(word_list)

print(theme_word_list)

with open('/Users/Jinya/Desktop/Syllabus/Sample/theme_words.csv', 'w',encoding='utf8') as f:
    writer = csv.writer(f)

    writer.writerows(theme_word_list)
