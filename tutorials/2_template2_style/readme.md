# Tutorial for template2_style.css
This tutorial is designed to guide users through the process of customizing the template2_style.css file. This template focuses on styling a chat interface for communicating with LLM APIs on the backend (multi-page streamlit apps). Please see `pages/Page_Two.py` for the python code on creating this streamlit interface. Learning objectives include: 
1. [Chat Input Styling](#chat-input-styling)  
2. [Streamlit Menu Styling](#streamlit-menu-styling)  

The tutorial provides clear instructions on how to apply various CSS properties to achieve a cohesive and polished user interface. Each section covers essential CSS classes and attribute selectors, ensuring that users can easily follow along and implement the styles effectively. ***Please see previous tutorial for modifying other additional properties in this template***.

***Note: This template is currently being used for Page 2 on the demo streamlit app***. 

To recreate `template2_style.css` and modify the components, please follow the steps below:

## 1. Chat Input Styling <a name="chat-input-styling"></a>  
***Note: More CSS properties can always be added in each class. For the tutorial, only select properties were modified.***
### stApp .stChatInput
The `.stApp .stChatInput` class is responsible for styling the chat input field. Notice how `.stChatInput` is a nested class within `.stApp`, which means it is a descendant of an element with the class:
```css
.stApp .stChatInput {  
    background-color: #f9f9f9;  
    border: 1px dashed #0c00e6;  
    border-radius: 5px;  
    padding: 0px 0px;  
    font-size: 16px;  
    color: #333;  
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
    transition: border-color 0.3s ease, box-shadow 0.3s ease;  
}  
```
- **background-color**: Gives the chat input a light grey background.
- **border**: Gives the input field a 1px dashed border in a blue color.
- **border-radius**: Gives the input field rounded corners.
- **padding**: Sets the padding inside the input field to 0.
- **font-size**: Sets the text size inside the input field to 16px.
- **color**: Sets the text color inside the input field to a dark grey.
- **box-shadow**: This adds a small shadow to the input field. The shadow is offset 2px down and 4px to the right and has a 10% opacity.
- **transition**: This adds a smooth transition to the border color and shadow of the input field when they change, over a duration of 0.3 seconds.

### .stApp .stChatInput:hover
The `.stApp .stChatInput:hover` selector changes the appearance of the chat input field when it's hovered over:
```css
.stApp .stChatInput:hover {  
    box-shadow: 0 20px 8px rgba(0, 0, 0, 0.15); 
    border-color: #b60000;  
}  
```
- **box-shadow**: Increases the size of the input field's shadow when it's hovered over. The shadow is offset 20px down and 8px to the right and has a 15% opacity.
- **border-color**: Changes the border color of the input field to a dark red when it's hovered over.

## 2. Streamlit Menu Styling <a name="streamlit-menu-styling"></a>  
### .st-emotion-cache-w3nhqi.ef3psqc5
The `.st-emotion-cache-w3nhqi.ef3psqc5` class is responsible for modifying the appearance of the native Streamlit three dots menu in the top right corner. Useful to modify these attributes when you modify appearances of the .stApp class. Example, you set the app background to white, now the streamlit menu icon is not visible. 
```css
.st-emotion-cache-w3nhqi.ef3psqc5 {  
    color: red !important; 
}  
```
- **color: red !important**; - Changes the color of the three dots menu to red. The `!important` flag ensures that this style takes precedence over other styles that might be applied to this element.

## Conclusion 
This tutorial provided detailed instructions for customizing the template2_style.css file used in a Streamlit application. Objectives covered included:

1. [Chat Input Styling](#chat-input-styling)  
2. [Streamlit Menu Styling](#streamlit-menu-styling)   


Each section specifies various CSS classes and attribute selectors, detailing how they can be applied within a Streamlit application to achieve specific visual effects. **Remember this template works best for multi-paged streamlit apps. Please stay tuned to the next tutorial for creating a single page chat template**. 