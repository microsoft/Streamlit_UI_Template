from styling import global_page_style
import streamlit as st  
  
def main():  
    st.title('Welcome to Streamlit_UI_Template')  
    st.write('-'*50)
    st.markdown("<p style='text-align: center; color: black;'>This is a demo page created with Streamlit. \
                It uses a custom CSS file to modify the UI.</p>", unsafe_allow_html=True)  
    st.write('-'*50)
  
    user_name = st.text_input('Please enter your name')  
  
    # Add a selectbox to the sidebar.  
    option = st.selectbox(  
        'Which greeting do you prefer?',  
        ['Hello', 'Hi', 'Hey'])  
  
    if st.button('Greet Me'):  
        if user_name:  
            st.success(f'{option}, {user_name}! Nice to meet you.')  
        else:  
            st.success(f'{option} there! Nice to meet you.')  
  


if __name__ == "__main__":  
    global_page_style()
    main()  