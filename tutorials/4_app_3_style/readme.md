# Tutorial for APP_3

This tutorial focuses on styling the `app_3` Streamlit application. The app is a single-page chatbot interface that does not require a sidebar or navigation bar. The styling is implemented directly in the Python script using custom CSS injected via `st.markdown`. This guide will walk you through the process of customizing the appearance of the app to create a polished and user-friendly interface.

## Learning Objectives
1. [Adding Custom CSS Styling](#custom-css-styling)  
2. [Designing the Header](#designing-the-header)  
3. [Styling Buttons and Other Components](#styling-buttons)  
4. [Configuring the Footer](#configuring-the-footer)  
5. [Practical Implementation](#practical-implementation)  

---

## 1. Adding Custom CSS Styling <a name="custom-css-styling"></a>

In `app_3`, we use the `st.markdown` function to inject CSS directly into the app. This allows us to style elements such as the background, fonts, and layout.

```python
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;  /* Set the font style */
            background-color: #f3f2f1;  /* Set the background color */
        }
        hr {
            border: none;
            border-top: 1px solid #e1e1e1;  /* Add a subtle horizontal line */
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)
```

### Explanation
- **`font-family`**: Sets the font style for the entire app.
- **`background-color`**: Defines the background color of the app.
- **`hr`**: Styles the horizontal rule for visual separation.

---

## 2. Designing the Header <a name="designing-the-header"></a>

The header is styled to include a logo and a title, giving the app a professional look.

```python
st.markdown("""
    <style>
        .main-header {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 0;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .main-header img {
            width: 110px;
            height: auto;
            margin-bottom: -20px;
        }
        .main-header h1 {
            margin: 0;
            font-size: 1.8em;
            color: #000000;
            margin-bottom: -10px;
        }
    </style>
    <div class="main-header">
        <img src="https://logos-world.net/wp-content/uploads/2020/09/Microsoft-Logo-2012-present.jpg" alt="logo">
        <h1>Streamlit UI APP #3</h1>
    </div>
""", unsafe_allow_html=True)
```

### Explanation
- **`.main-header`**: Styles the header container with padding, background color, and a shadow for depth.
- **`img`**: Adjusts the size and alignment of the logo.
- **`h1`**: Sets the font size and color of the title.

---

## 3. Styling Buttons and Other Components <a name="styling-buttons"></a>

Customizing buttons and other interactive components enhances the user experience.

```python
st.markdown("""
    <style>
        .stButton>button {
            background-color: #0078d4;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-size: 14px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #005a9e;
        }
    </style>
""", unsafe_allow_html=True)
```

### Explanation
- **`.stButton>button`**: Targets the Streamlit button element to apply custom styles.
- **`background-color`**: Sets the button's background color.
- **`border-radius`**: Rounds the corners of the button.
- **`:hover`**: Changes the button color when hovered over.

---

## 4. Configuring the Footer <a name="configuring-the-footer"></a>

The footer is styled to include additional information, such as a "Powered by Microsoft" message and a link to Streamlit.

```python
st.markdown("""
    <style>
        .main-header footer {
            text-align: center;
            margin-top: 10px;
            color: #888;
        }
        .main-header footer a {
            color: #0078d4;
            text-decoration: none;
        }
        .main-header footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="main-header">
        <footer>
            <p>Powered by Microsoft | Built with <a href="https://streamlit.io" target="_blank">Streamlit</a></p>
        </footer>
    </div>
""", unsafe_allow_html=True)
```

### Explanation
- **`.main-header footer`**: Styles the footer text with center alignment and a light gray color.
- **`.main-header footer a`**: Styles the footer link with a blue color and removes the underline.
- **`.main-header footer a:hover`**: Adds an underline to the link when hovered over.

---

## 5. Practical Implementation <a name="practical-implementation"></a>

Here’s the `main()` function from the script, which integrates the custom styling and app functionality:

```python
def main():
    """
    The main function that defines the layout, styling, and functionality of the app.
    """
    # Add custom CSS styling for the app
    st.markdown("""
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;  /* Set the font style */
                background-color: #f3f2f1;  /* Set the background color */
            }
            .main-header {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px 0;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .main-header img {
                width: 110px;
                height: auto;
                margin-bottom: -20px;
            }
            .main-header h1 {
                margin: 0;
                font-size: 1.8em;
                color: #000000;
                margin-bottom: -10px;
            }
            .main-header footer {
                text-align: center;
                margin-top: 10px;
                color: #888;
            }
            .main-header footer a {
                color: #0078d4;
                text-decoration: none;
            }
            .main-header footer a:hover {
                text-decoration: underline;
            }
            hr {
                border: none;
                border-top: 1px solid #e1e1e1;
                margin: 20px 0;
            }
            .stButton>button {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-size: 14px;
                cursor: pointer;
            }
            .stButton>button:hover {
                background-color: #005a9e;
            }
        </style>
        <div class="main-header">
            <img src="https://logos-world.net/wp-content/uploads/2020/09/Microsoft-Logo-2012-present.jpg" alt="logo">
            <h1>Streamlit UI APP #3</h1>
            <footer>
                <p>Powered by Microsoft | Built with <a href="https://streamlit.io" target="_blank">Streamlit</a></p>
            </footer>
        </div>
    """, unsafe_allow_html=True)

    st.write('<hr>', unsafe_allow_html=True)  # Add a horizontal line for separation

    # Initialize session state for chat messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []  # Create an empty list to store chat messages

    # Input box for user queries
    question = st.chat_input('Input query here...')

    # Define avatars for user and assistant
    avatars = {
        "assistant": "🤖",  # Avatar for assistant
        "user": "👤"        # Avatar for user
    }

    # Display the chat history
    for message in st.session_state.messages:
        avatar = avatars.get(message["role"], "❓")  # Get the avatar based on the role
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message['content'])  # Render the message content as Markdown

    # Handle new user input
    if question:
        chat(st.session_state.messages, question)  # Process the user's input
        st.write('<hr>', unsafe_allow_html=True)  # Add a horizontal line for separation

    # Add a button to reset the chat session
    clear_chat_placeholder = st.empty()  # Create a placeholder for the reset button
    if clear_chat_placeholder.button(label='🔄', help="Click to start new chat session", key='chat_reset'):
        st.session_state.messages = clear_session(st.session_state.messages)  # Reset the chat session
        clear_chat_placeholder.empty()  # Remove the button after resetting
        st.success("Chat session has been reset.")  # Display a success message
```

---

## Conclusion

This tutorial demonstrated how to style the `app_3` Streamlit application using custom CSS. Key elements include:
1. Customizing the background and fonts.
2. Designing a professional header with a logo and title.
3. Styling buttons for better interactivity.
4. Adding a footer with additional information and links.

By following these steps, you can create a visually appealing and user-friendly chatbot interface tailored to your needs.