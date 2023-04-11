# -*- coding: utf-8 -*-
"""Seminal-Augementation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eO7P5YyZmg4gj4vonfmze3k9q9KgDaoF
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('/content/train.csv')
df_english = df.query('language == "English"')
df_english.head()
analytic = df.groupby(by=['language','label']).size()
analytic.head()
analytic.to_csv('data-analytics.csv')
df.groupby(['language', 'label']).size()



df = pd.read_csv('/content/train copy.csv')
df= df.drop(['language'], axis = 1)
df_2 = pd.read_csv('/content/0.3dataaug.csv')
df_2.columns = ["text", "label",]
df_2.head()
df_merge = pd.concat([df,df_2])
df_merge.to_csv('train-0.3-data-aug.csv')

df = pd.read_csv('/content/train copy.csv')
df= df.drop(['language'], axis = 1)
df_2 = pd.read_csv('/content/0.3dataaug.csv')
df_merge = pd.concat([df,df_2])
df_merge.to_csv('train-0.3-data-aug.csv')
len(df_merge)
