# Streamlit UI Template (CSS)

This repository contains guides and templates for embedding CSS into Streamlit applications. It provides step-by-step instructions on how to create and implement a CSS file in your Streamlit project. Ideal for those looking to customize their Streamlit UI appearance.

***If interested in a specific template, please reach out to Cameron Jackson (MS Fed Civ - Cloud Solution Architect) at camerjackson@microsoft.com.***

## Prerequisites

- Installed a code editor such as [Visual Studio Code](https://code.visualstudio.com/download) or an equivalent.
- Installed [Python](https://www.python.org/downloads/) on your machine. Python installation by running `python --version` in the command line. This project was created with Python 3.11.

## Embed CSS to Streamlit site

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

## Run the Demo App Locally

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

## Templates
### Template #1
 Key modifications include styling the main app container, form elements, sidebar, navigation bar, success messages, titles, buttons, text inputs, and select boxes in a streamlit application.

[Template #1 - Image](media/basic_template.png)

[Template #1 - MP4](media/streamlit_template1.mp4)

[Template #1 - Tutorial](tutorials/template1_style/readme.md)

### Template #2
Coming soon...