import streamlit as st
from students import PY4AI_classes
from scores import session_scores
def main():
  st.title('PY4AI CLASS SCORES')
  tab1, tab2, tab3 = st.tabs(['Lists', 'Charts', 'Classification'])
  
  with tab2:
    tab1, tab2 = st.tabs(['Number of students', 'Scores'])
    with tab1:
      PY4AI_classes()
    with tab2:
      radio = st.radio(label='Sessions', options=('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
      session_scores(radio)
main()
