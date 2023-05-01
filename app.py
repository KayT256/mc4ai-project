import streamlit as st
from students import PY4AI_classes

def main():
  st.title('PY4AI CLASS SCORES')
  tab1, tab2, tab3 = st.tabs(['Lists', 'Charts', 'Classification'])
  
  with tab2:
    tab1, tab2 = st.tabs(['Number of students', 'Scores'])
    with tab1:
      PY4AI_classes()
      st.success('Comment: The distribution of students in each class is nearly equal.')
    

main()
