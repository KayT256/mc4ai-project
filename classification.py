import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('py4ai-score.csv')
df.fillna(0, inplace=True)

df['S-AVERAGE'] = [df.loc[i][['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9']].mean() for i in df.index]
def pass_fail(row):
        if row['GPA'] >= 6:
            return 'PASS'
        else:
            return 'FAIL'
df['PASS/FAIL'] = df.apply(pass_fail, axis=1)

def two_features():
    model = LogisticRegression()
    model.fit(np.stack((df['S-AVERAGE'], df['S6'])).T, df['PASS/FAIL'])

    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2 = weights

    x1 = np.array([0, 10])
    x2 = -(w1*x1 + bias)/w2
    fig = plt.figure() 
    plt.xlabel('S-AVERAGE')
    plt.ylabel('S6 (Midterm test)')
    plt.plot(x1, x2)
    plt.scatter(df['S-AVERAGE'][df['PASS/FAIL'] == 'PASS'], df['S6'][df['PASS/FAIL'] == 'PASS'])
    plt.scatter(df['S-AVERAGE'][df['PASS/FAIL'] == 'FAIL'], df['S6'][df['PASS/FAIL'] == 'FAIL'])
    st.pyplot(fig)
    st.write('Score: ', np.round(model.score(np.stack((df['S-AVERAGE'], df['S6'])).T, df['PASS/FAIL']), decimals=2))

def three_features():
    X = df[['S-AVERAGE','S6','S10']].values.copy()
    y = df['PASS/FAIL'].values.copy()  
    model = LogisticRegression()
    model.fit(X,y)

    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2, w3 = weights

    x1 = np.array([X[:,0].min(), X[:,0].max()])
    y1 = np.array([X[:,1].min(), X[:,1].max()])

    xx, yy = np.meshgrid(x1, y1)
    xy = np.c_[xx.ravel(), yy.ravel()]
    z = -(bias + w1*xy[:,0] + w2*xy[:,1])/w3

    z = z.reshape(xx.shape)

    X1 = X[y=='PASS']
    X2 = X[y=='FAIL']

    fig = go.Figure(data=[go.Scatter3d(x=X1[:,0], y=X1[:,1], z=X1[:,2], mode='markers'),
                          go.Scatter3d(x=X2[:,0], y=X2[:,1], z=X2[:,2], mode='markers'),
                          go.Surface(x=x1, y=y1, z=z)])
    st.plotly_chart(fig)
    st.write('Score: ', np.round(model.score(X,y), decimals=2))