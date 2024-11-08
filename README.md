# Streamlit UI Template (CSS)

This repository contains guides and templates for embedding CSS into Streamlit applications. It provides step-by-step instructions on how to create and implement a CSS file in your Streamlit project. Ideal for those looking to customize their Streamlit UI appearance.

If interested in a specific template, please reach out to Cameron Jackson (MS Fed Civ - Cloud Solution Architect) at camerjackson@microsoft.com.

Navigate to:
- [Prerequisites](#prerequisites)
- [Embed CSS to Streamlit site](#embed-css-to-streamlit-site)
- [Run the Demo App Locally](#run-the-demo-app-locally)
- [Templates](#templates)

## Prerequisites <a name="prerequisites"></a> 

- Installed a code editor such as [Visual Studio Code](https://code.visualstudio.com/download) or an equivalent.
- Installed [Python](https://www.python.org/downloads/) on your machine. Python installation by running `python --version` in the command line. This project was created with Python 3.11.

## Embed CSS to Streamlit site  <a name="embed-css-to-streamlit-site"></a> 

To embed css file to streamlit follow these steps:
1. Create CSS file in project directory. Use `style_example.css` as template.
   
2. Create a standalone python file to open the css file. Example for python file `styling_example.py`:
```python
   import streamlit as st
   def global_page_style():  
       with open('style_example.css') as f:
           css = f.read()
       st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
```
3. Call the file from step 2 into the streamlit app code file (Note: If multipage app, call on each page.) 
```python
   from styling import global_page_style
```
4. Call the function in your code:
```python
   if __name__ == '__main__':
        global_page_style()
```

## Run the Demo App Locally <a name="run-the-demo-app-locally"></a> 

**Clone this repository**
```
git clone https://github.com/microsoft/Streamlit_UI_Template
```

**Create .venv environment in code interpretor**
- Steps reflect creating .venv in VsCode
```
1. Open the command palette: CTRL + SHIFT + P
2. Search: Python: Create Environment
3. Select: Venv
4. Select the latest version of Python installed on your device.
5. .venv environment created
```

**Install the necessary libraries**
```
pip install -r requirements.txt  
```

**Navigate to the /app directory**
```
cd app
```

**Run the streamlit application**
```
streamlit run Page_One.py
```

## Templates <a name="templates"></a> 
### Template #1 (used in App 1 only)
 Key modifications include styling the main app container, form elements, sidebar, navigation bar, success messages, titles, buttons, text inputs, and select boxes in a streamlit application.

[Template #1 - Image](media/template1_style.png)

[Template #1 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EXjjir5b0r1Gg91bKMBzakcBuTS4RqItXuzgc6X0sEPm7Q?e=XfwgDC)

[Template #1 - Tutorial](tutorials/1_template1_style/readme.md)

[Template #1 - CSS](templates/template1_style.css)

[Template #1 - Python](apps/app_1/Page_One.py)

### Template #2 (used in App 1 only)
 Key modifications include styling the chat input class and streamlit menu class, in a streamlit application.

[Template #2 - Image](media/template2_style.png)

[Template #2 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EVQHO8swd09BgHMDd9-i9mcB2UVUs69A3UtYGZalinrlAg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=bUfojP)

[Template #2 - Tutorial](tutorials/2_template2_style/readme.md)

[Template #2 - CSS](templates/template2_style.css)

[Template #2 - Python](apps/app_1/pages/Page_Two.py)

### App 2 
App 2 is dedicated to developing a Streamlit application, integrating the Streamlit navigation bar for enhanced user interaction. This methodology is particularly suited for scenarios requiring the construction of single or multi-page applications utilizing navigation bars for seamless navigation and user experience.

[App 2 - Image](media/app2_styling.png)

[App 2 - Tutorial](tutorials/3_app_2_style/readme.md)

[App 2 - Python](apps/app_2/app.py)