import pandas as pd

data =[{'A': 5, 'B': 4, 'C': 2, 'D': 6},
       {'A': 4, 'B': 6, 'C': 4, 'D': 3},
       {'A': 8, 'B': 6, 'C': 4, 'D': 9},
       {'A': 1, 'B': 3, 'C': 8, 'D': 4}]

df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
# pour obtenir la colone A
print(df['A'])
print(df)
# pour obtenir la colone A et C
print(df[['A', 'C']])
# pour obtenir la colone B jusqua D
print(df.ix[:, 'B': 'D'])
# pour obtenir les lignes de two a four
print(df.ix['two': 'four'])
# df.ix[rows, columm]
print(df.ix[['two', 'three'], ['B', 'C']])
#par pas de deux facil a comprendre
print(df.ix['one':'four':2, 'B': 'D' ])

#""""""""""""""Missing data""""""""""""""""""""""
S1 = pd.Series([1, 2, 3, 4], index= list("ABCD"))
S2 = pd.Series([5, 6,7, 8], index= list("CDEF"))
df1 = pd.DataFrame({'a': S1, 'b':S2})
df2 = pd.DataFrame([S1,S2])
print('ca commence ici')
print(df1)
print(df2)
# permet de supprimer la ou ya les nan et de garder l'intersection
print(df1.dropna())
#permet de changé la valeur nan du datafram
print(df1.fillna(0))
# reindex combiné des tableaux
t = df.reindex(index=['three', 'four', 'five', 'seven'], columns=['C', 'D', 'E', 'F'])
print(t)
#fusion = merging
pd.merge(df1,df2)
#df1.join([df2, df1])
#contatenation avec les ligne des dataframe avec columms
pd.concat([df1, df2])
#contatenation avec les colones des dataframe avec columms
pd.concat([df1, df2], axis=1)