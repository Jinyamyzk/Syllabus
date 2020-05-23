from gensim import corpora, models, similarities
import gensim
import math
import csv

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict

import pandas as pd
import itertools


df = pd.read_csv('syllabus.csv', usecols=[0])
class_names = df.values.tolist()
class_names  = list(itertools.chain.from_iterable(class_names))

f = open("theme_words.csv", "r")
reader = csv.reader(f)
texts = [ e for e in reader ]
f.close()

# トピック数の設定
NUM_TOPICS = 10

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda_model = LdaModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)


# pyLDAvis
import pyLDAvis.gensim

vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary, n_jobs = 1, sort_topics = False)

pyLDAvis.save_html(vis, 'pyLDA_vis.html')
