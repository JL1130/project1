import streamlit as st
st.title("KUAN LOVE PUNA")
st.write("New Project")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello KUAN{name}! 👋")