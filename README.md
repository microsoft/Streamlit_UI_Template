# Streamlit UI Template (CSS)

This repository provides templates and tutorials for creating visually appealing and functional Streamlit applications using custom CSS. Whether you're building a single-page chatbot, a multi-page app with navigation, or a professional UI with custom styling, this project has you covered.

Streamlit is a Python-based framework for building interactive web applications. By combining Streamlit's simplicity with custom CSS, you can create polished and professional UIs tailored to your needs.

This project includes:
- **App 1**: A multi-page app featuring a form-based interface with custom CSS for styling and a chat interface with additional CSS for streamlined interactions.
- **App 2**: A multi-page app featuring a chat interface, with a navigation bar to enhance usability and organization across multiple pages.
- **App 3**: A single-page chat interface app with minimalistic styling injected directly into the Python script.

If interested in a specific template, please reach out to Cameron Jackson (MS Fed Civ - Cloud Solution Architect) at camerjackson@microsoft.com.

Navigate to:
- [Prerequisites](#prerequisites)
- [Embed CSS to Streamlit site](#embed-css-to-streamlit-site)
- [Run the Demo App Locally](#run-the-demo-app-locally)
- [Templates](#templates)

## Prerequisites <a name="prerequisites"></a> 

- Installed a code editor such as [Visual Studio Code](https://code.visualstudio.com/download) or an equivalent.
- Installed [Python](https://www.python.org/downloads/) on your machine. Python installation by running `python --version` in the command line. This project was created with Python 3.11.

## Embed CSS in Streamlit Apps <a name="embed-css-to-streamlit-site"></a>

Streamlit apps in this repository use two approaches to apply custom styles:

1. **Using a CSS File**:
   - Create a CSS file (e.g., `style.css`) in the app's directory.
   - Load and apply the CSS file in your app using the following function:
     ```python
     import streamlit as st

     def apply_custom_css(css_file):
         with open(css_file) as f:
             css = f.read()
         st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
     ```
   - Call this function in your app:
     ```python
     apply_custom_css('style.css')
     ```

2. **Embedding Styles Directly in Python**:
   - For simpler apps, you can embed CSS directly in the Python script:
     ```python
     import streamlit as st

     def apply_inline_styles():
         css = """
         body {
             background-color: #f0f0f0;
         }
         .stButton>button {
             color: white;
             background-color: #007bff;
         }
         """
         st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
     ```
   - Call this function in your app:
     ```python
     apply_inline_styles()
     ```

### Notes:
- **App 1** uses the first approach with an external `.css` file for more complex styling.
- **Apps 2 and 3** use the second approach, embedding styles directly in the Python script for simplicity.

Choose the approach that best fits your app's requirements.

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

**Navigate to either the /app_1, /app_2, or /app_3 directory**

Navigation to /app_1:
```
cd apps/app_1
```

Navigation to /app_2:
```
cd apps/app_2
```

Navigation to /app_3:
```
cd apps/app_3
```

**Run the streamlit application**

Command for app_1:
```
streamlit run Page_One.py
```

Command for app_2:
```
streamlit run app_2.py
```

Command for app_3:
```
streamlit run app_3.py
```

## Templates <a name="templates"></a> 

### App 1
App 1 is a multi-page Streamlit application. It includes:
- **Page 1**: A form-based interface with custom CSS for form elements, sidebar, and navigation.
- **Page 2**: A chat interface styled using `template2_style.css`, designed for streamlined user interactions.

#### Page 1 

[Template #1 - Image](media/template1_style.png)

[Template #1 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EXjjir5b0r1Gg91bKMBzakcBuTS4RqItXuzgc6X0sEPm7Q)

[Template #1 - Tutorial](tutorials/1_template1_style/readme.md)

[Template #1 - CSS](templates/template1_style.css)

[Template #1 - Python](apps/app_1/Page_One.py)

#### Page 2

[Template #2 - Image](media/template2_style.png)

[Template #2 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EVQHO8swd09BgHMDd9-i9mcBPDjxwfHgEElmLC9vSOZ6uA)

[Template #2 - Tutorial](tutorials/2_template2_style/readme.md)

[Template #2 - CSS](templates/template2_style.css)

[Template #2 - Python](apps/app_1/pages/Page_Two.py)

---

### App 2
App 2 is a multi-page Streamlit application that features a chat interface as its primary focus, with a navigation bar to enhance usability and organization across multiple pages.

[App 2 - Image](media/app2_styling.png)

[App 2 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EY5N4ktKLUZFoaK2lS1OulsB6zpg0G5BidIWu8kmaCQktQ)

[App 2 - Tutorial](tutorials/3_app_2_style/readme.md)

[App 2 - Python](apps/app_2/app_2.py)

---

### App 3
App 3 is a single-page chatbot application that focuses on simplicity and functionality. It does not include a sidebar or navigation bar, making it ideal for streamlined user interactions. The app includes custom CSS styling injected directly into the Python script.

[App 3 - Image](media/app3_styling.png)

[App 3 - Demo Video](https://microsoft-my.sharepoint.com/:v:/p/camerjackson/EULxCd30tK9IoLvzkRIsGxoBDZ-A_3u7100yhtsBxo_z8A)

[App 3 - Tutorial](tutorials/4_app_3_style/readme.md)

[App 3 - Python](apps/app_3/app_3.py)