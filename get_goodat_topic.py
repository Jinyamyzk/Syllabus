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


df = pd.read_json('syllabus.json')
with open('grade.csv') as f:
    h = next(csv.reader(f))
    reader = csv.reader(f)
    grades = [e for e in reader]
    f.close()

for row in grades:
    print(int(row[0]), row[1], float(row[2]))
    topic_grades = search_goodat_topic(int(row[0]), row[1], float(row[2]))
    if topic_grades is not None:
        sum_topic_odds = [topic_grades[i] + sum_topic_odds[i] for i in range(len(topic_grades))]

print(sum_topic_odds)
