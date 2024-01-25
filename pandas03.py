# -*- coding: utf-8 -*-
"""pandas03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqAaq7WDWGn8ZaUnNpQSaWa-dGEBYdfy
"""

import pandas as pd

df1 = pd.DataFrame({'a':['a0', 'a1', 'a2', 'a3'],
                    'b':['b0', 'b1', 'b2', 'b3'],
                    'c':['c0', 'c1', 'c2', 'c3']})
df1

df2 = pd.DataFrame({'a':['a2', 'a3', 'a4', 'a5'],
                    'b':['b2', 'b3', 'b4', 'b5'],
                    'c':['c2', 'c3', 'c4', 'c5'],
                    'd':['d2', 'd3', 'd4', 'd5']},
                   index = [2, 3, 4, 5])
df2

result1 = pd.concat([df1, df2])   # 두 개의 데이터프레임을 수직으로(concatenation) 결합하는 작업을 수행
result1

result1 = pd.concat([df1, df2])   # 두 개의 데이터프레임을 수직으로(concatenation) 결합하는 작업을 수행
result1.reset_index(drop=True, inplace=True)  # index를 그대로 살리고 싶다면 drop = False를 입력.
result1

result1 = pd.concat([df1, df2], ignore_index = True)
result1

result2 = pd.concat([df1, df2], axis = 'columns')
result2

result3 = pd.concat([df1, df2], axis=1, join='inner')   # join='inner ' 이덱스의 교집합만 뽑아서 가져다 줌.
print(result3)

result3 = pd.concat([df1, df2], axis=1, join='outer')   # join='outer ' 이덱스의 합집합 뽑아서 가져다 줌.
print(result3)

import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare','sex','class', 'survived']]
print(df.head())

grouped = df.groupby(['class'])
print(grouped)

grouped_df = {}
for key, group in grouped:
  print('key:', key)
  print('lenght:', len(group))
  grouped_df[key] = group
  print(group.head())

print(grouped_df.keys())

grouped_df['First']

grouped_df['Second']

average = grouped.mean()
average

grouped.min()

grouped.max()

grouped_two = df.groupby(['class', 'sex']) #  'class'와 'sex' 열 값을 기준으로 데이터를 여러 그룹으로 나누는 것
for key, group in grouped_two:
  print('key: ' , key)
  print('lenght: ', len(group))
  print(group.head())

grouped_two.mean()

group3f = grouped_two.get_group(('Third','female'))
# 'class'가 'Third'이고 'sex'가 'female'인 그룹을 선택하는 작업.
group3f

dfg = grouped_two.mean()
# 데이터프레임을 그룹화한 후,
# 각 그룹에 대한 평균을 계산하여 새로운 데이터프레임 dfg를 생성하는 작업을 수행.
# .mean(): 이 부분은 그룹화된 데이터에 대한 평균을 계산하는 메서드.
dfg

dfg.loc[('First', 'male')]

dfg.loc['First']
# Pandas 데이터프레임에서 특정 라벨(label) 또는 인덱스(index)인
# 'First'에 해당하는 행(row)을 선택하는 방법.

dfg.xs('female', level = 'sex')
# df.xs(key, axis=0, level=None, drop_level=True)
# Pandas 데이터프레임에서 특정 라벨(label) 또는 인덱스(index)를 가진 데이터를 선택하는 메서드.

titanic

df_teenage = titanic.loc[
    (titanic.age >= 10) & (titanic.age<20), :]
df_teenage

df_teenage.info()
print(df_teenage.survived.sum())
df_teenage.survived.mean()

df_female_under10 = titanic.loc[
    (titanic.age <= 10) & (titanic.sex == 'female'), :]
df_female_under10.head()
df_female_under10.info()
df_female_under10.survived.sum()
df_female_under10.survived.mean()

df_under10_up60 = titanic.loc[
    ( titanic.age < 10 ) | ( titanic.age >= 60 ), :]
df_under10_up60.info()
df_under10_up60.survived.sum()
df_under10_up60.survived.mean()

isin_filter = titanic['sibsp'].isin([2,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())
df_isin.count()

isin_filter

df_sibsp245 = titanic.loc[(titanic.sibsp==2) | (titanic.sibsp==4) | (titanic.sibsp==5)]
df_sibsp245.head()

df_sibsp245 = titanic[(titanic.sibsp==2) | (titanic.sibsp==4) | (titanic.sibsp==5)]
df_sibsp245.head()