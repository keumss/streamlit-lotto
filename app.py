import streamlit as st
import random

st.header("Good Luck!")

for col, number in zip(st.columns(6), sorted(random.sample(range(1, 46), k=6))):
    with col:
        st.html(f"<h2><center>{number}</center></h2>")

st.button("Roll", type="primary", use_container_width=True)
