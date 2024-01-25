# -*- coding: utf-8 -*-
"""pandas02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B-CwGYRWMnJSWvAgjJKzpLJXS9Hc6Qt8
"""

import pandas as pd
import numpy as np
import seaborn as sns       # 타이타닉 데이터가 안에 있음.
from sklearn import preprocessing   # 전처리

pd.set_option('display.max_columns', 8)   # column을 한줄로 보기 위한 설정. 8은 앞에 4개 뒤에 4개를 보여줌.
pd.set_option('display.unicode.east_asian', True)
# 이 옵션은 유니코드 문자를 포함한 동아시아 언어(예: 한국어, 중국어, 일본어)의 표시 방식을 설정.
# 설정값을 True로 지정하면, 데이터프레임 출력에서 동아시아 언어 문자열을 올바르게 표시할 수 있도록 함.

df = sns.load_dataset('titanic')
print(df)

nan_deck = df['deck'].value_counts()    # nan값 제외 'deck'의 항목 count
print(nan_deck)

nan_deck1 = df['deck'].value_counts(dropna=False)     # nan값 포함 'deck'의 항목 count
print(nan_deck1)

print(df.isnull())

print(df.head().isnull())

print(df.head().notnull())

print(df.isnull().sum())

df.dropna(axis=1, thresh=500, inplace=True)   # nan값이 500개 이상인 column을 지워라.
print(df.columns)

df_age = df.dropna(subset=['age'], how='any', axis=0)
df_age.info()

mean_age = df['age'].mean()                   # age의 평균을 구함.
df['age'].fillna(mean_age, inplace = True)    # nan에 값을 채워 넣는 함수 -> fillna()
print(df.head(10))

most_freq = df['embark_town'].value_counts(dropna=True)      #
print(most_freq)

most_freq1 = df['embark_town'].value_counts(dropna=True).idxmax()      # 최빈값을 보여줌.
print(most_freq1)

df_most_freq = df['embark_town'].fillna(most_freq1, inplace=False)
# 'embark_town'의 nan값에 most_freq1에서 찾은 최빈값을 넣어줌.
print(df_most_freq[825:830])
print(df[825:830])

df['embark_town'].fillna(method='ffill', inplace=True)
# 'embark_town'의 nan값에 method='ffill'을 설정 -> 이전값을 넣는다는 뜻.
# method='bfill' 설정은 이후값을 넣는다는 뜻.
print(df_most_freq[825:830])
print(df[825:830])

df.info()

df.drop(['survived', 'embarked'], axis=1, inplace=True)
df.info()

print(df.isnull().sum())      # 각 column에 nan값이 있는지 검색.