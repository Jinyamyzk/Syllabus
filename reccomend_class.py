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

def sum_class_score(nendo):
    available_classes = df[(df['年度'] == nendo)]
    class_names_topics = available_classes[['科目名','トピックの確率']].values.tolist()
    for class_name_topic in class_names_topics:
        # combined = [x*y for (x,y) in zip(class_name_topic[1],sum_topic_odds)]
        # total_clas_score = sum(combined)
        # class_name_topic[1] = total_clas_score
        class_names.append(class_name_topic)



df = pd.read_json('syllabus_tfidf.json')
with open('grade2.csv') as f:
    h = next(csv.reader(f))
    reader = csv.reader(f)
    grades = [e for e in reader]
    f.close()

for row in grades:
    topic_grades = search_goodat_topic(int(row[0]), row[1], float(row[2]))
    if topic_grades is not None:
        sum_topic_odds = [topic_grades[i] + sum_topic_odds[i] for i in range(len(topic_grades))]


class_names = []
sum_class_score(2020)
# class_names_sorted = sorted(class_names, reverse=True, key=lambda x: x[1])
for i in class_names[0:10]:
    print(i)
