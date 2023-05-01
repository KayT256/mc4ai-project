import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('py4ai-score.csv')
def PY4AI_classes():
  st.plotly_chart(px.pie(df, names="PYTHON-CLASS", title='Percentages of students per PY4AI-COTAI class'))
