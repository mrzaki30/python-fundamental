import streamlit as st
import pandas as pd

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.markdown('## My first app')
st.title('Hello, world!')
st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
