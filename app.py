import streamlit as st
import random

for col, number in zip(st.columns(6), sorted(random.sample(range(1, 46), k=6))):
    with col:
        st.header(f"{number}")

st.button("Roll")
