import streamlit as st
import pandas as pd

df = pd.read_csv('py4ai-score.csv')

def specialized_class(row):
    if 'CV' in row['CLASS']:
        return 'Literature'
    elif 'CT' in row['CLASS']:
        return 'Math'
    elif 'CL' in row['CLASS']:
        return 'Physics'
    elif 'CH' in row['CLASS']:
        return 'Chemistry'
    elif 'CA' in row['CLASS']:
        return 'English'
    elif 'CTIN' in row['CLASS']:
        return 'IT'
    elif 'CSD' in row['CLASS']:
        return 'History and Geography'
    elif 'CTRN' in row['CLASS']:
        return 'Chinese and Japanese'
    elif 'TH' in row['CLASS'] or 'SN' in row['CLASS']:
        return 'Bilingual'
    else:
        return 'Others'

def grade(row):
    if '10' in row['CLASS']:
        return 10
    elif '11' in row['CLASS']:
        return 11
    else:
        return 12


df['SPECIALIZED CLASS'] = df.apply(specialized_class, axis=1)
df['GRADE'] = df.apply(grade, axis=1)

def selections():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('Gender')
        male = st.checkbox('Male', True)
        female = st.checkbox('Female', True)
    
    with col2:
        grade = st.radio('Grade', ('All', 'Grade 10', 'Grade 11', 'Grade 12'))

    with col3:
        room = st.selectbox('Room', ('All', 'A.114', 'A.115'))
    
    with col4:
        session = st.selectbox('Session', ('All', 'Morning', 'Afternoon'))

    st.write('Specialized Class')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        literature = st.checkbox('Literature', True)
        math = st.checkbox('Math', True)
    
    with col2:
        physics = st.checkbox('Physics', True)
        chemistry = st.checkbox('Chemistry', True)

    with col3:
        english = st.checkbox('English', True)
        it = st.checkbox('IT', True)
    
    with col4:
        history_geography = st.checkbox('History and Geography', True)
        chinese_japanese = st.checkbox('Chinese and Japanese', True)
    
    with col5:
        bilingual = st.checkbox('Bilingual', True)
        others = st.checkbox('Others', True)

    if male == True and female == True:
        selected = df
    elif male == True:
        selected = df[df['GENDER'] == 'M']
    elif female == True:
        selected = df[df['GENDER'] == 'F']
    else:
        st.error('Please select a Gender!')

    if grade == 'Grade 10':
        selected = selected[selected['GRADE'] == 10]
    elif grade == 'Grade 11':
        selected = selected[selected['GRADE'] == 11]
    elif grade == 'Grade 12':
        selected = selected[selected['GRADE'] == 12]
    
    if room == 'A.114':
        selected = selected[(selected['PYTHON-CLASS'] == '114-S') | (selected['PYTHON-CLASS'] == '114-C')]
    elif room == 'A.115':
        selected = selected[(selected['PYTHON-CLASS'] == '115-S') | (selected['PYTHON-CLASS'] == '115-C')]
    
    if session == 'Morning':
        selected = selected[(selected['PYTHON-CLASS'] == '114-S') | (selected['PYTHON-CLASS'] == '115-S')]
    elif session == 'Afternoon':
        selected = selected[(selected['PYTHON-CLASS'] == '114-C') | (selected['PYTHON-CLASS'] == '115-C')]
    
    st.write(selected[['NAME', 'GENDER', 'CLASS', 'PYTHON-CLASS', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'BONUS', 'GPA', 'REG-MC4AI']])


def info():
    st.write('Number of students: ', len(df))
