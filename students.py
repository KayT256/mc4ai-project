import plotly.express as px
import streamlit as st
from list import add_specialized_class, add_grade

df = add_specialized_class()
df = add_grade()

def PY4AI_classes():
  st.plotly_chart(px.pie(df, names="PYTHON-CLASS", title='Percentages of students per PY4AI-COTAI class'))
  st.success('Comment: The distribution of students in each class is nearly equal.')

def specialized_class():
  st.plotly_chart(px.pie(df, names="SPECIALIZED CLASS", title='Percentages of students per specialized class'))
  st.success('Comment: Most of the students are from Math, English, Physics, and IT specialized classes.')

def gender():
  st.plotly_chart(px.pie(df, names="GENDER", title='Gender ratio'))
  st.success('Comment: Boys seem to be more interested in AI than girls.')