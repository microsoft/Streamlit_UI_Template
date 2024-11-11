import streamlit as st  
import time  
  
def chat(messages, question):  
    messages.append({"role": "user", "content":question})  
    with st.chat_message("user", avatar="👤"):  
        st.markdown(question)  
    with st.spinner('Processing...'):  
        time.sleep(5)  
        response = "Welcome to App 2!" 
        messages.append({"role": "assistant", "content":response})  
        with st.chat_message("assistant", avatar="🤖"):  
            st.markdown(response)  
  
def clear_session(messages):  
    # Clear necessary session state variables  
    st.cache_data.clear()  
    messages.clear()  
    return messages  
  
def home():  
    st.markdown('<h1 class="title">Streamlit UI APP2</h1>', unsafe_allow_html=True) 
  
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
        st.write('-'*50)  
  
    clear_chat_placeholder = st.empty()  
    if clear_chat_placeholder.button('Start New Session'):  
        st.session_state.messages = clear_session(st.session_state.messages)  
        clear_chat_placeholder.empty()  
        st.success("Chat session has been reset.")  