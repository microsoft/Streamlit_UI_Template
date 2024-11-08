# Tutorial for APP_2
This tutorial is designed to guide users through the process of customizing the `app_2` Streamlit application. This template focuses on styling a chat interface for communicating with LLM APIs on the backend, while utilizing the streamlit Navigation bar. This demo application does not utilize a custom template.css script as other scripts do, but rather injects the css directly in the `app.py` python script, which is the central page for the app. Please see `app_2/app.py` for the python code on creating this streamlit interface. Learning objectives include: 
1. [Understanding Streamlit Basics](#streamlit-basics)  
2. [Customizing App components with CSS (in code)](#streamlit-app-css)
3. [Implementing Navigation Bars](#streamlit-nav)  
4. [Creating and Organizing Page Functions](streamlit-page-functions)
5. [Practical Implementation](#streamlit-practical-implementation)

## File Structure
```
app.py  
pages/  
    __init__.py  
    home.py  
```

## 1. Understanding Streamlit Basics <a name="streamlit-basics"></a> 
In Streamlit, the `st.set_page_config` function is used to configure the initial settings of the page, such as the layout and the state of the sidebar. 
```python 
import streamlit as st  
  
st.set_page_config(  
    initial_sidebar_state="collapsed",  
    layout="wide"  
)  
```
### Explanation
- `initial_sidebar_state`: Specifies the initial state of the sidebar. Options include #expanded", "collapsed", and "auto". 
- `layout`: Specifies the layout of the page. Options include "centered" and "wide".


## 2. Customizing App Components with CSS (in code) <a name="streamlit-app-css"></a> 
In `app.py`, we inject custom CSS directly into the Streamlit application to style various elements such as the sidebar collapse button and the page title. This styling will translate to all pages hosted in the app. 
```python  
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
```
### Explanation 
- The `st.markdown` function is used to inject custom HTML and CSS.
- `unsafe_allow_html=True` is required to allow the injection of raw HTML and CSS.
- The CSS rules customize the appearance of the **sidebar collapse widget** and the **page title**.


## 3. Implementing Navigation Bars <a name="streamlit-nav"></a> 
The navigation bar is implemented using the `st_navbar` function from the `streamlit_navigation_bar` package. This function takes several parameters such as `pages`, `logo_path`, `styles`, and `options` to configure the navigation bar.
```python 
# Define the pages for the navigation bar  
pages = [""]  
  
# Define the path to the logo image  
parent_dir = os.path.dirname(os.path.abspath(__file__))  
logo_path = os.path.join(parent_dir, "microsoft_logo.svg")  
  
# Define the styles for the navigation bar  
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
  
# Define the options for the navigation bar  
options = {  
    "show_menu": False,  
    "show_sidebar": False,  
}  
  
# Create the navigation bar  
page = st_navbar(  
    pages=pages,  
    logo_path=logo_path,  
    styles=styles,  
    options=options,  
)  
```

### Explanation
- `pages`: A list of pages to include in the navigation bar. We leave this empty since our app is not multi-paged. 
- `parent_dir`: The directory containing the current script.
- `logo_path`: The path to the logo image to be included in the navigation bar.
- `styles`: Custom styles for the navigation bar, including background color, text color, padding, and margins.
- `options`: Options to show or hide the main menu and the sidebar.
- `st_navbar`: Function to create the navigation bar.

## 4. Creating and Organizing Page Functions <a name="streamlit-page-functions"></a> 
The` __init__.py` script in the pages directory imports the `home` function from `home.py`, enabling it to be called within `app.py`.
```python 
# __init__.py  
from .home import home  
```

### Explanation 
- The `__init__.py` script imports the `home` function, making it accessible as `pg.home` in `app.py`.

The `home.py` script contains all the Streamlit chat components, representing a page in `app.py`.
```python
# home.py  
import streamlit as st  
import time  
  
def chat(messages, question):  
    messages.append({"role": "user", "content": question})  
    with st.chat_message("user", avatar="👤"):  
        st.markdown(question)  
    with st.spinner('Processing...'):  
        time.sleep(5)  
        response = "Welcome to Streamlit Template 2."  
        messages.append({"role": "assistant", "content": response})  
        with st.chat_message("assistant", avatar="🤖"):  
            st.markdown(response)  
  
def clear_session(messages):  
    # Clear necessary session state variables  
    st.cache_data.clear()  
    messages.clear()  
    return messages  
  
def home():  
    st.markdown('<h1 class="title">Streamlit_UI_APP2</h1>', unsafe_allow_html=True)  
    if 'messages' not in st.session_state:  
        st.session_state.messages = []  
  
    question = st.chat_input('Input query here...')  
    avatars = {  
        "assistant": "🤖",  # Avatar for assistant  
        "user": "👤"        # Avatar for user  
    }  
  
    for message in st.session_state.messages:  
        avatar = avatars.get(message["role"], "❓")  # Get the avatar based on the role  
        with st.chat_message(message["role"], avatar=avatar):  
            st.markdown(message['content'])  
  
    if question:  
        chat(st.session_state.messages, question)  
        st.write('-' * 50)  
  
    clear_chat_placeholder = st.empty()  
    if clear_chat_placeholder.button('Start New Session'):  
        st.session_state.messages = clear_session(st.session_state.messages)  
        clear_chat_placeholder.empty()  
        st.success("Chat session has been reset.")  
```

### Exaplanation 
- `chat`: Function to handle the chat interaction. It appends the user's question to the messages list, displays it, and then simulates a response from the assistant.
- `clear_session`: Function to clear the chat session by resetting the session state variables.
- `home()`: Main function to render the home page. It displays the title, handles the chat input, and manages the chat session.

## 5. Practical Implementation <a name="streamlit-practical-implementation"></a> 
Finally, in `app.py`, we set up the navigation bar and page redirection using the `functions` dictionary and `st_navbar` function.
```python 
# app.py  
functions = {  
    "Home": pg.home  
}  
  
page = st_navbar(  
    pages=pages,  
    logo_path=logo_path,  
    styles=styles,  
    options=options,  
)  
  
go_to = functions.get(page)  
if go_to:  
    go_to()  
```

### Explanation 
- `functions`: Dictionary mapping page names to their corresponding functions.
- `st_navbar`: Function to create the navigation bar.
- `go_to`: Function to navigate to the selected page.


## Conclusion 
This tutorial provided the process of creating and customizing a chat interface application using Streamlit and Streamlit Navigation.Objectives covered included:

1. [Understanding Streamlit Basics](#streamlit-basics)  
2. [Customizing App components with CSS (in code)](#streamlit-app-css)
3. [Implementing Navigation Bars](#streamlit-nav)  
4. [Creating and Organizing Page Functions](streamlit-page-functions)
5. [Practical Implementation](#streamlit-practical-implementation)

By following these steps, you can leverage the power of Streamlit to build interactive and visually appealing web applications tailored to your specific needs. Each section specifies various CSS classes and attribute selectors, detailing how they can be applied within a Streamlit application to achieve specific visual effects. **Remember this template works best for single or multi paged Streamlit apps that utilize the the Streamlit Navigation feature.**