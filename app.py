import streamlit as st
from students import PY4AI_classes
from scores import session_scores
from groups import score_groups
def main():
  st.title('PY4AI CLASS SCORES')
  tab1, tab2, tab3, tab4 = st.tabs(['Lists', 'Charts', 'Groups', 'Classification'])
  
  with tab2:
    tab21, tab22 = st.tabs(['Number of students', 'Scores'])
    with tab21:
      PY4AI_classes()
    with tab22:
      radio = st.radio('Sessions', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
      session_scores(radio)
  with tab3:
    slider = st.slider('Number of groups', 2, 5, 3)
    score_groups(slider)
    

main()
