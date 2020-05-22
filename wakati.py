import csv
from janome.tokenizer import Tokenizer
import re

import pandas as pd
df = pd.read_csv('syllabus.csv', usecols=[0,1])
array = df.values.tolist()

t = Tokenizer()

theme_word_list = []
for row in array:
    if type(row[1]) is str:
        row_ = re.sub('u3000','',row[1])
        print(row_)


        token_list = t.tokenize(row_)
        word_list = []
        # word_list.append(row[0])
        for token in token_list:
            if token.part_of_speech.split(',')[0] == u'名詞':
                word_list.append(token.base_form)
        theme_word_list.append(word_list)
    else:
        theme_word_list.append([])

print(theme_word_list)

with open('/Users/Jinya/Desktop/Syllabus/theme_words.csv', 'w',encoding='utf8') as f:
    writer = csv.writer(f)

    writer.writerows(theme_word_list)
