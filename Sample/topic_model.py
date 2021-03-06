from gensim import corpora, models, similarities
import gensim
import math
import csv

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict
import pandas as pd

df = pd.read_csv('syllabus.csv', usecols=[0])
class_names = df.values.tolist()




f = open("theme_words.csv", "r")
reader = csv.reader(f)
texts = [ e for e in reader ]

# トピック数の設定
NUM_TOPICS = 3

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = LdaModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)

# テストデータをモデルに掛ける
score_by_topic = defaultdict(int)
test_corpus = [dictionary.doc2bow(text) for text in texts]

# クラスタリング結果を出力
for unseen_doc, raw_train_text in zip(test_corpus, texts):
    for class_name in class_names:
        print(class_name)
    for topic, score in lda[unseen_doc]:
        score_by_topic[int(topic)] = float(score)
    for i in range(NUM_TOPICS):
        print('{:.2f}'.format(score_by_topic[i]), end='\t')
    print()



f.close()
