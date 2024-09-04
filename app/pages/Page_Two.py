from styling import template1_page_style
import streamlit as st  
  
def main():  
    st.title('Thank You for Visiting the Demo!')  
    st.balloons() 
    st.write("Click here to return to Page One: ")
    st.page_link("Page_One.py", label="Page One", icon="🏠")
  
if __name__ == "__main__":  
    template1_page_style()
    main()  
