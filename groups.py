import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('py4ai-score.csv')
df.fillna(0, inplace=True)

def score_groups(a):
    kmeans = KMeans(n_clusters=a, n_init='auto')
    X = np.stack((df['S6'], df['S10'], df['GPA'])).T
    kmeans.fit(X)
    st.plotly_chart(px.scatter_3d(df, x = 'S6', y = 'S10', z = 'GPA', color = kmeans.labels_))
    for i in range(a):
        st.write(f'Group {i+1}: highest GPA ', df['GPA'][kmeans.labels_==i].max(), ', lowest GPA ', df['GPA'][kmeans.labels_==i].min(), ', average: ', np.round(df['GPA'][kmeans.labels_==i].mean(), decimals = 1))
        st.write(df[['NAME', 'CLASS', 'GPA']][kmeans.labels_==i])