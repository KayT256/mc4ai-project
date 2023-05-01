import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('py4ai-score.csv')

def session_scores(a):
    st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = a, color  = 'GENDER'))
    st.info('Comment: Overall, in this course, boys study better than girls')