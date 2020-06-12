import pandas as pd
import pickle
import csv

sum_topic_odds = [0,0,0,0,0,0,0,0,0,0]
def search_goodat_topic(nendo,code,grade):
    taken_class = df[(df['年度']==nendo) & (df['時間割コード']==code)]
    topic_grades = [float(n)*grade for n in taken_class['トピックの確率'].values.tolist()[0]]
    return [x+y for(x,y) in zip(topic_grades,sum_topic_odds)]


df = pd.read_pickle('syllabus.pkl')
with open('grade.csv') as f:
    h = next(csv.reader(f))
    reader = csv.reader(f)
    grades = [e for e in reader]
    f.close()

for row in grades:
     sum_topic_odds=search_goodat_topic(int(row[0]),row[1],float(row[2]))


print(sum_topic_odds)
