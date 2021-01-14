import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.write("""
# Simple Iris Flower Prediction App

This app predicts the Iris flower type!

""")

st.sidebar.header('User Input Parametrs')

def user_input_features():

    sepal_length = st.sidebar.slider('sepal_length', 4.3, 7.9, 5.8)
    sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.4, 2.2)
    petal_length = st.sidebar.slider('petal_length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 0.2)
    data = {'sepal_length':sepal_length,
        'sepal_width':sepal_width, 
        'petal_length':petal_length, 
        'petal_width':petal_width}
    
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
st.sidebar.write('# Gregoryish@gmail.com')
st.subheader('User Input Parametrs')
st.write(df)

iris = datasets.load_iris()

X = iris.data
Y = iris.target

clf = RandomForestClassifier()

clf.fit(X,Y)

prediction = clf.predict(df)
prediction_probab = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_probab)