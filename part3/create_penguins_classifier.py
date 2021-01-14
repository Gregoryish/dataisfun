import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pickle


df = pd.read_csv(r'D:\GregoryishGithub\data\penguins_cleaned.csv')

target = 'species'

get_dummies = ['island', 'sex']


for col in get_dummies:
    df = pd.concat([df, pd.get_dummies(df[col])], axis=1)
    df = df.drop(col, axis=1)


dict_target = dict(zip(df[target].unique(), [1,2,3]))

df[target] = df[target].apply(lambda x: dict_target[x])

X = df.drop(target, axis=1)
y = df[target]

clf = RandomForestClassifier()

clf.fit(X, y)

pickle.dump(clf, open('penguins_classifier.sav', 'wb'))

clf = pickle.load(open('penguins_classifier.sav', 'rb'))

print('Penguins classifier has been successfully created and saved!')