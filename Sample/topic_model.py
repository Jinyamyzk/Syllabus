from gensim import corpora, models, similarities
import pandas as pd

df = pd.read_csv('theme_words.csv')
array = df.values.tolist()
for arr in array:
    print(arr)
