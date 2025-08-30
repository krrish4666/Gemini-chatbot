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
        with st.spinner("Thinking..."):
            # ✅ Streaming Gemini response
            stream = client.models.generate_content_stream(
                model=model,
                contents=[m["content"] for m in st.session_state.messages]
            )
            reply = ""
            placeholder = st.empty()
            for chunk in stream:
                if chunk.text:
                    reply += chunk.text
                    placeholder.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
