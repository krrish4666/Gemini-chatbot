import os
import streamlit as st
from google import genai

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("⚡ Gemini Streaming Chat")

# Sidebar controls
with st.sidebar:
    st.subheader("Settings")
    default_model = "gemini-2.5-pro"
    model = st.text_input("Model", value=default_model)

    if "GEMINI_API_KEY" not in os.environ:
        gemini_key = st.text_input("Gemini API Key", type="password")
        if gemini_key:
            os.environ["GEMINI_API_KEY"] = gemini_key

    if st.button("Reset chat"):
        st.session_state.messages = []

# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = []

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Render history
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Chat input
if prompt := st.chat_input("Ask anything"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Reformat the history for the Gemini API
        api_history = []
        for msg in st.session_state.messages:
            # The API expects the role 'model' for the assistant's messages
            role = "model" if msg["role"] == "assistant" else msg["role"]
            api_history.append({"role": role, "parts": [{"text": msg["content"]}]})
        
       
        *_, last_message = api_history
        
        with st.spinner("Thinking..."):
            # Initialize the model and generate content
            gen_model = genai.GenerativeModel(model) # Initialize the model
            stream = gen_model.generate_content(
                api_history,
                stream=True
            )
            
            reply = ""
            placeholder = st.empty()
            for chunk in stream:
                if chunk.text:
                    reply += chunk.text
                    placeholder.markdown(reply + "▌") 
            placeholder.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
