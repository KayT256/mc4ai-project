import streamlit as st
from students import room

def main():
  st.title('PY4AI CLASS SCORES')
  tab1, tab2, tab3 = st.tabs(['Lists', 'Charts', 'Classification'])
  
  with tab1:
    room()
main()
