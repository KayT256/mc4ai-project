from distutils.log import info
import streamlit as st
from students import PY4AI_classes, specialized_class, gender
from scores import session_scores
from groups import score_groups
from classification import three_features, two_features
from list import selections

def main():
  st.title('PY4AI CLASS SCORES')
  tab1, tab2, tab3, tab4 = st.tabs(['Lists', 'Charts', 'Groups', 'Classification'])
  with tab1:
    selections()

  with tab2:
    tab21, tab22 = st.tabs(['Number of students', 'Scores'])
    with tab21:
      PY4AI_classes()
      specialized_class()
      gender()
    with tab22:
      sessions = st.radio('Sessions', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'), horizontal=True)
      session_scores(sessions)
  with tab3:
    slider = st.slider('Number of groups', 2, 5, 3)
    score_groups(slider)
  with tab4:
    features = st.radio('Number of features', (2, 3), horizontal=True)
    if features == 2:
      two_features()
    else:
      three_features()

main()
