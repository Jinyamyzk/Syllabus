
from gensim import corpora, models, similarities
import gensim
import math
import csv

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict

#LDAモデルのロード
import pickle
with open("lda_model.pickle", "rb") as f:
    lda_model = pickle.load(f)

#とりあえず適当なシラバスのベクトルゲット

target_class_num =  44#ターゲットの科目を選択

f = open("theme_words_2018.csv", "r")
reader = csv.reader(f)
texts = [ e for e in reader ]
f.close()
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
all_topics = lda_model.get_document_topics(corpus, minimum_probability=0)

from gensim import similarities
doc_index = similarities.docsim.MatrixSimilarity(lda_model[corpus])

vec_lda = all_topics[target_class_num]
s = doc_index.__getitem__(vec_lda)
s = sorted(enumerate(s), key=lambda t: t[1], reverse=True)

#似ているtop3の授業の番号を取り出す
sim_list=[]
for i in s[1:4]:
    sim_list.append(i[0])


import pandas as pd
import itertools
df = pd.read_csv('syllabus_2018.csv', usecols=[0])

class_names = df.values.tolist()
class_names  = list(itertools.chain.from_iterable(class_names))



print(class_names[target_class_num])

print("-----------------------")

for doc_id in sim_list:
    print(class_names[doc_id])

# dictionary = corpora.Dictionary(texts)
# other_corpus = [dictionary.doc2bow(texts[2])]
# unseen_doc = other_corpus[0]
# vector = lda_model[unseen_doc]
# print(vector)
