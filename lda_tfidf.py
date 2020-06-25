import pickle
from gensim import corpora, models, similarities
import gensim
import math
import csv
import numpy as np

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict

import pandas as pd
import itertools

from tqdm import tqdm
import matplotlib
import matplotlib.pylab as plt
import json
from wordcloud import WordCloud

import logging


df = pd.read_csv('syllabus.csv', usecols=[0])
class_names = df.values.tolist()
class_names = list(itertools.chain.from_iterable(class_names))

f = open("theme_words.csv", "r")
reader = csv.reader(f)
texts = [e for e in reader]
f.close()

dictionary = corpora.Dictionary(texts)
# make corpus
corpus = [dictionary.doc2bow(t) for t in texts]


# tfidf
tfidf = gensim.models.TfidfModel(corpus)


# make corpus_tfidf
corpus_tfidf = tfidf[corpus]

# LDA Model
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=9, alpha='symmetric', random_state=0)



# WordCloud
fig, axs = plt.subplots(ncols=2, nrows=math.ceil(lda_model.num_topics/2), figsize=(16,20))
axs = axs.flatten()

def color_func(word, font_size, position, orientation, random_state, font_path):
    return 'darkturquoise'

for i, t in enumerate(range(lda_model.num_topics)):

    x = dict(lda_model.show_topic(t, 30))
    im = WordCloud(
        background_color='black',
        color_func=color_func,
        max_words=4000,
        width=300, height=300,
        random_state=0
    ).generate_from_frequencies(x)
    axs[i].imshow(im.recolor(colormap= 'Paired_r' , random_state=244), alpha=0.98)
    axs[i].axis('off')
    axs[i].set_title('Topic '+str(t))

# vis
plt.tight_layout()
plt.show()

# save as png
plt.savefig('wordcloud.png')
