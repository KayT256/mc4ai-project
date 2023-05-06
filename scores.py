import plotly.express as px
import streamlit as st
from list import add_specialized_class, add_grade

df = add_specialized_class()
df = add_grade()

def session_scores(a):
    st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = a, color  = 'GENDER'))
    st.info('Comment: Overall, in this course, boys study better than girls')
    st.plotly_chart(px.box(df, x = 'SPECIALIZED CLASS', y = a))
    st.info(
            """
            Comment:
            - Students from IT-specialized classes study best.
            - Students from foreign language specialized classes study pretty weakly.
            """
    )
    st.plotly_chart(px.histogram(df, x = 'SPECIALIZED CLASS', y = a, color = 'GENDER'))