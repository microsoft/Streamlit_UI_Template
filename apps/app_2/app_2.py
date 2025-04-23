import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

# Inject custom CSS for the sidebar collapse button  
st.markdown(  
    """  
    <style>  
    /* Customize the sidebar collapse widget */  
    svg.eyeqlp53.st-emotion-cache-1f3w014.ex0cdmw0 {  
      color: #0c00e6 !important; /* Change text color if needed */  
        }  
    /* Customize the Page Title element */
    .title {  
        font-family: 'Roboto', sans-serif;  
        text-align: center;  
        font-size: 3em; /* Adjust the size if needed */  
        color: black; /* Change the color if needed */  
        text-decoration: underline; /* Underline the text */ 
    }  
    </style>  
    """,  
    unsafe_allow_html=True  
)  

pages = [""]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "microsoft_logo.svg")
styles = {
    "nav": {
        "background-color": "#0c00e6",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "10px",
        "width": "100px",
        "height": "50px",
        "margin-top": "-10px"
    },
    "span": {
        "color": "FFFFFF",
        "padding": "14px",
    },
    "active": {
        "background-color": "FFFFFF",
        "color": "000000",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages=pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.home
}
go_to = functions.get(page)
if go_to:
    go_to()