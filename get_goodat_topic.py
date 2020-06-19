import pandas as pd
import pickle
import csv
import json

sum_topic_odds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def search_goodat_topic(nendo, code, grade):
    topic_grades = None
    taken_class = df[(df['年度'] == nendo) & (df['時間割コード'] == code)]
    topic_value = taken_class['トピックの確率'].values.tolist()
    if len(topic_value) == 1:
        topic_grades = [n * grade for n in topic_value[0]]
    return topic_grades

def get_reccomend_class(nendo,topic_index):
    available_classes = df[(df['年度'] == nendo)]
    class_names_topics = available_classes[['科目名','トピックの確率']].values.tolist()
    for i in class_names_topics:
        i[1] = i[1][topic_index]
        class_names.append(i)












df = pd.read_json('syllabus.json')
with open('grade.csv') as f:
    h = next(csv.reader(f))
    reader = csv.reader(f)
    grades = [e for e in reader]
    f.close()

for row in grades:
    topic_grades = search_goodat_topic(int(row[0]), row[1], float(row[2]))
    if topic_grades is not None:
        sum_topic_odds = [topic_grades[i] + sum_topic_odds[i] for i in range(len(topic_grades))]

topic_index = sum_topic_odds.index(max(sum_topic_odds))

class_names = []

get_reccomend_class(2020,topic_index)
class_names_sorted = sorted(class_names, reverse=True, key=lambda x: x[1])
for i in class_names_sorted[0:5]:
    print(i[0])
