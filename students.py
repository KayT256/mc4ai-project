import plotly.express as px
import streamlit
import pandas as pd

df = pd.read_csv('py4ai-score.csv')
def room():
  st.plotly_chart(px.pie(df, names="PYTHON-CLASS"))
