import streamlit as st

def handle_exception(exception):
    st.error(f"An error occurred: {exception}")

    