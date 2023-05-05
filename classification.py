import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('py4ai-score.csv')
df.fillna(0, inplace=True)

df['AVERAGE'] = [df.loc[i][['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9']].mean() for i in df.index]
def pass_fail(row):
    if row['GPA'] >= 6:
        return 'PASS'
    else:
        return 'FAIL'
df['PASS/FAIL'] = df.apply(pass_fail, axis=1)

model = LogisticRegression()
model.fit(np.stack((df['AVERAGE'], df['S6'])).T, df['PASS/FAIL'])

weights = model.coef_[0]
bias = model.intercept_[0]
w1, w2 = weights

x1 = np.array([0, 10])
x2 = -(w1*x1 + bias)/w2

def two_features():
    fig = plt.figure() 
    plt.plot(x1, x2)
    plt.scatter(df['AVERAGE'][df['PASS/FAIL'] == 'PASS'], df['S6'][df['PASS/FAIL'] == 'PASS'])
    plt.scatter(df['AVERAGE'][df['PASS/FAIL'] == 'FAIL'], df['S6'][df['PASS/FAIL'] == 'FAIL'])
    st.pyplot(fig)
    