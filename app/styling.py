import streamlit as st
def global_page_style():  
    with open('style_example.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)