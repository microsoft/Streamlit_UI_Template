# Tutorial for template1_style.css
This tutorial is designed to guide users through the process of customizing the template1_style.css file to enhance the visual appeal and functionality of a Streamlit application. Learning objectives include: 
1. [Main App Styling](#main-app-styling)  
2. [Form Element Styling](#form-element-styling)  
3. [Sidebar Styling](#sidebar-styling)  
4. [Navigation Styling](#navigation-styling)  
5. [Success Message Styling](#success-message-styling)  
6. [Main Title Styling](#main-title-styling)  
7. [Button Styling](#button-styling)  
8. [Text Input Styling](#text-input-styling)  
9. [Select Box Styling](#select-box-styling)  

The tutorial provides clear instructions on how to apply various CSS properties to achieve a cohesive and polished user interface. Each section covers essential CSS classes and attribute selectors, ensuring that users can easily follow along and implement the styles effectively.

***Note: This template is currently being used for Page 1 on the demo streamlit app***. 

To recreate `template1.css` and modify the components, please follow the steps below:

## 1. Main App Styling <a name="main-app-styling"></a>  
***Note: More CSS properties can always be added in each class. For the tutorial, only select properties were modified.***
### .stApp
The `.stApp` class is responsible for the overall styling of the application. Here's the breakdown:
```css
.stApp{    
    background-color: #d4d3d3;    
    color:#000000;    
    padding:20px;  
}    
```
- **background-color: #d4d3d3**; - This gives the application a light grey background.
- **color:#000000**; - This sets the default color of the text in the application to black.
- **padding:20px**; - This creates a space of 20px around the content inside the application, separating it from the edges.

### .stApp > header 
The `>` inside of `.stApp > header `is a child combinator, meaning it only selects direct children. So this rule applies to header elements directly inside elements with the .stApp class.
```css
.stApp > header {    
    background-color: #a7a7a7;  
    color:#f8f8f8;    
    padding:2rem;    
}    
```
- **background-color**: #a7a7a7; - This gives the header a darker grey background.
- **color:#f8f8f8**; - This sets the color of the text in the header to a light grey.
- **padding:2rem**; - This creates a space of 2rem around the content inside the header.

## 2. Form Element Styling <a name="form-element-styling"></a>  
### .stTextInput and .stSelectbox
If you have multiple form elements (text inputs & select boxes in this case) that need similiar structures, grouping them together ensures they all receive the same styling with minimal code.
```css
.stTextInput, .stSelectbox{    
    margin-bottom: 20px;  
}    
```
- **margin-bottom: 20px**; - This creates a space of 20px beneath these elements, useful for separating consecutive form elements.

***Note: Added to provide extra space between these select elements and other elements in the streamlit application.***

## 3. Sidebar Styling <a name="sidebar-styling"></a>  
### [data-testid="stSidebar"]
The sidebar styling is controlled by the `[data-testid="stSidebar]`attribute selector. This styles the entire sidebar area.
```css
[data-testid="stSidebar"]{    
    background-color: #a7a7a7;  
    color: #ffffff;    
}   
```
- **background-color**: #a7a7a7; - This sets the background color of the sidebar to a dark grey.
- **color**: #ffffff; - This sets the color of the text inside the sidebar to white. (***Does not apply to page titles for multi-paged apps.***)

## 4. Navigation Styling <a name="navigation-styling"></a>   
### [data-testid="stSidebarNav"]
The sidebar navigation is styled with the `[data-testid="stSidebarNav"]` attribute selector. This styles the navigation section within the sidebar.
```css
[data-testid="stSidebarNav"] {    
    background-image: url(https://logolook.net/wp-content/uploads/2021/06/Microsoft-Logo.png);    
    background-repeat: no-repeat;    
    padding-top: 100px;    
    background-position: 20px -10px;    
    background-size: 300px;    
}    
```
- **background-image**: url(...); - This sets the background image of the navigation to a specific URL.
- **background-repeat**: no-repeat; - This prevents the background image from repeating.
- **padding-top**: 100px; - This creates a space of 100px at the top of the navigation.
- **background-position**: 20px -10px; - This positions the background image 20px from the left and -10px from the top of the navigation.
- **background-size**: 300px; - This sets the size of the background image.

### [data-testid="stSidebarNav"]::before
The pseudo-element `::before` following `[data-testid="stSidebarNav"]` is used to add content before the navigation.
```css
[data-testid="stSidebarNav"]::before {    
    content: "";    
    margin-left: 60px;    
    margin-top: 20px;    
    font-size: 20px;    
    position: relative;    
    top: -300px;    
    font-weight: bold;    
    text-align: center;    
}   
```
- **content**: " "; - This sets the content to be inserted. In this case, it's an empty string. (***Add extra text to the sidebar. Requires some reordering of elements in the Python file.***)
- **margin-left**: 60px; and margin-top: 20px; - These add space to the left and top of the content.
- **font-size**: 20px; - This sets the font size of the content.
- **position**: relative; - This sets the position of the content relative to its normal position.
- **top**: -300px; - This moves the content 300px above its normal position.
- **font-weight**: bold; - This makes the content bold.
- **text-align**: center; - This centers the content.

## 5. Success Message Styling <a name="success-message-styling"></a> 
### .success-message
The `.success-message` class is used for styling success messages. 
```css
.success-message {    
    text-align: center;    
    margin: 20px 0;    
}    
```
- **text-align**: center; - This centers the success message.
- **margin**: 20px 0; - This adds 20px of space to the top and bottom of the success message, and no space to the left and right.

## 6. Main Title Styling <a name="main-title-styling"></a> 
The `h1` tag is used to modify the main title on the streamlit page.
```css
h1 {    
    color: #000400;    
    text-align: center;    
    margin-bottom: 20px;    
    font-family:cursive;  
    font-size: 50px;  
}    
```
- **color**: #000400; - This sets the color of the title text to a very dark green.
- **text-align**: center; - This centers the title text.
- **margin-bottom**: 20px; - This adds 20px of space beneath the title text.
- **font-family**:cursive; - This sets the font of the title text to a cursive style.
- **font-size**: 50px; - This sets the size of the title text to 50px.

## 7. Button Styling <a name="button-styling"></a>  
### .stButton
The `.stButton` button selector styles buttons in the streamlit application.
```css
.stButton button {    
    background-color: #0073e6;    
    color: white;    
    border-radius: 5px;    
    padding: 10px 20px;    
    font-size: 16px;    
    border: none;    
    cursor: pointer;    
}    
```
- **background-color**: #0073e6; - This sets the button's background color to a shade of blue.
- **color**: white; - This sets the button's text color to white.
- **border-radius**: 5px; - This gives the button rounded corners.
- **padding**: 10px 20px; - This adds space around the button's content.
- **font-size**: 16px; - This sets the button's text size.
- **border**: none; - This removes the button's border.
- **cursor**: pointer; - This changes the cursor to a pointer when hovering over the button.

### .stButton button:hover
When the button is hovered over, its style changes as specified in `.stButton button:hover`:
```css
.stButton button:hover {    
    background-color: #005bb5;    
    color: yellow;  
}    
```
- **background-color**: #005bb5; - The button's background color becomes a darker shade of blue.
- **color**: yellow; - The button's text color changes to yellow.

## 8. Text Input Styling <a name="text-input-styling"></a> 
### .stTextInput:hover
Targets the entire element with the class `.stTextInput`. This does not include what is inside of the element. Modifies properties when this class is hovered over.
```css
.stTextInput:hover {  
    box-shadow: 0 20px 8px rgba(0, 0, 0, 0.15); 
}  
```
- **box-shadow**: 0 20px 8px rgba(0, 0, 0, 0.15); - This adds a shadow to the text input field container when it is hovered over. The shadow is offset 20px down and 8px to the right and has a 15% opacity.

### .stTextInput:focus
Targets the entire element with the class `.stTextInput`. This does not include what is inside of the element. Modifies properties when this class is focused, meaning it's active and ready to receive input.
```css 
.stTextInput:focus {    
    border-color: #0a00b6;   
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);   
}    
```
- **border-color**: #0a00b6; - This changes the border color of the text input field to a dark blue when it's in focus.
- **box-shadow**: 0 4px 8px rgba(0, 0, 0, 0.15); - This adds a shadow to the text input field when it's in focus. The shadow is offset 4px down and 8px to the right and has a 15% opacity.

### .stTextInput input
Targets the input element inside the class `.stTextInput`. This does not include the outside properties of the element. The `.stTextInput` input selector styles the text input field.
```css
.stTextInput input {    
    border: 1px dashed #0c00e6;   
    border-radius: 5px;   
    padding: 8px 12px;   
    background-color: #f9f9f9;   
    font-size: 16px;   
    color: #333;   
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);   
    transition: border-color 0.3s ease, box-shadow 0.3s ease;   
}    
```
- **border**: 1px dashed #0c00e6; - This gives the input field a 1px dashed border in a blue color.
- **border-radius**: 5px; - This gives the input field rounded corners.
- **padding**: 8px 12px; - This adds 8px of space on the top and bottom of the content inside the input field and 12px of space on the left and right.
- **background-color**: #f9f9f9; - This gives the input field a light grey background color.
- **font-size**: 16px; - This sets the text size inside the input field to 16px.
- **color**: #333; - This sets the text color inside the input field to a dark grey.
- **box-shadow**: 0 2px 4px rgba(0, 0, 0, 0.1); - This adds a small shadow to the input field. The shadow is offset 2px down and 4px to the right and has a 10% opacity.
- **transition**: border-color 0.3s ease, box-shadow 0.3s ease; - This adds a smooth transition to the border color and shadow of the input field when they change, over a duration of 0.3 seconds.

### .stTextInput input:hover
The `.stTextInput input:hover` selector changes the appearance of the input field when it's hovered over:
```css
.stTextInput input:hover {    
    box-shadow: 0 20px 8px rgba(0, 0, 0, 0.15);   
    border-color: #b60000;    
}    
```
- **box-shadow**: 0 20px 8px rgba(0, 0, 0, 0.15); - This increases the size of the input field's shadow when it's hovered over. The shadow is offset 20px down and 8px to the right and has a 15% opacity.
- **border-color**: #b60000; - This changes the border color of the input field to a dark red when it's hovered over.

## 9. Select Box Styling <a name="select-box-styling"></a>  
### .stSelectbox
The .stSelectbox selector styles the select box:
```css
.stSelectbox {    
    border: 1px solid #0c00e6;   
    border-radius: 5px;   
    padding: 8px 12px;   
    background-color: #f9f9f9;   
    font-size: 16px;   
    color: #333;   
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);   
    transition: border-color 0.3s ease, box-shadow 0.3s ease;   
}    
```
- **border**: 1px solid #0c00e6; - This gives the select box a 1px solid border in a blue color.
- **border-radius**: 5px; - This gives the select box rounded corners.
- **padding**: 8px 12px; - This adds 8px of space on the top and bottom of the content inside the select box and 12px of space on the left and right.
- **background-color**: #f9f9f9; - This gives the select box a light grey background color.
- **font-size**: 16px; - This sets the text size inside the select box to 16px.
- **color**: #333; - This sets the text color inside the select box to a dark grey.
- **box-shadow**: 0 2px 4px rgba(0, 0, 0, 0.1); - This adds a small shadow to the select box. The shadow is offset 2px down and 4px to the right and has a 10% opacity.
- **transition**: border-color 0.3s ease, box-shadow 0.3s ease; - This adds a smooth transition to the border color and shadow of the select box when they change, over a duration of 0.3 seconds.

### .stSelectbox:hover
The .stSelectbox:hover selector changes the appearance of the select box when it's hovered over:
```css
.stSelectbox:hover {    
    border-color: #b60000;   
    box-shadow: 0 20px 8px rgba(0, 0, 0, 0.15);   
}    
```
- **border-color**: #b60000; - This changes the border color of the select box to a dark red when it's hovered over.
- **box-shadow**: 0 20px 8px rgba(0, 0, 0, 0.15); - This increases the size of the select box's shadow when it's hovered over. The shadow is offset 20px down and 8px to the right and has a 15% opacity.

### .stSelectbox:focus
The .stSelectbox:focus selector changes the appearance of the select box when it's in focus, meaning it's active and ready to receive input:
```css
.stSelectbox:focus {    
    border-color: #0a00b6;   
    outline: none;   
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);   
}    
```
- **border-color**: #0a00b6; - This changes the border color of the select box to a dark blue when it's in focus.
- **outline**: none; - This removes the default browser outline from the select box when it's in focus.
- **box-shadow**: 0 4px 8px rgba(0, 0, 0, 0.15); - This increases the size of the select box's shadow when it's in focus. The shadow is offset 4px down and 8px to the right and has a 15% opacity.

## Conclusion 
This tutorial provided detailed instructions for customizing the template1_style.css file used in a Streamlit application. Objectives covered included:

1. [Main App Styling](#main-app-styling)  
2. [Form Element Styling](#form-element-styling)  
3. [Sidebar Styling](#sidebar-styling)  
4. [Navigation Styling](#navigation-styling)  
5. [Success Message Styling](#success-message-styling)  
6. [Main Title Styling](#main-title-styling)  
7. [Button Styling](#button-styling)  
8. [Text Input Styling](#text-input-styling)  
9. [Select Box Styling](#select-box-styling)  


Each section specifies various CSS classes and attribute selectors, detailing how they can be applied within a Streamlit application to achieve specific visual effects.