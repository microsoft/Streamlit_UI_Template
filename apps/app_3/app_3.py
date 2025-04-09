# Import necessary libraries
import streamlit as st  # Streamlit is used for building the web-based UI
import time  # Used to simulate processing delays

# Configure the Streamlit page
st.set_page_config(
    page_title="streamlit_ui_app3",  # Sets the title of the web page
    layout="centered",  # Ensures the app starts in a centered layout
    initial_sidebar_state="auto"  # Sidebar is set to auto-expand or collapse
)

def chat(messages, question):
    """
    Handles the chat interaction between the user and the assistant.

    Args:
        messages (list): A list of dictionaries storing the chat history.
        question (str): The user's input question.

    Behavior:
        - Appends the user's question to the chat history.
        - Displays the user's message in the chat UI.
        - Simulates a delay to mimic processing time.
        - Generates a static response and appends it to the chat history.
        - Displays the assistant's response in the chat UI.
    """
    # Add the user's question to the chat history
    messages.append({"role": "user", "content": question})
    # Display the user's message in the chat interface
    with st.chat_message("user", avatar="👤"):
        st.markdown(question)

    # Simulate processing with a spinner
    with st.spinner('Processing...'):
        time.sleep(5)  # Simulate a delay
        response = "Welcome to App 3. **This response simulates your AI model's response**"  # Static response (here is where your API response will go)
        # Add the assistant's response to the chat history
        messages.append({"role": "assistant", "content": response})
        # Display the assistant's response in the chat interface
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)

def clear_session(messages):
    """
    Clears the chat session by resetting the message history and clearing cached data.

    Args:
        messages (list): A list of dictionaries storing the chat history.

    Returns:
        list: An empty list to reset the chat history.
    """
    st.cache_data.clear()  # Clear any cached data in the session
    messages.clear()  # Clear the chat history
    return messages  # Return the cleared list

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

# Entry point for the script
if __name__ == "__main__":
    main()  # Run the main function
