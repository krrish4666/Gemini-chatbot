
# ⚡ Gemini Streaming Chatbot

A simple, interactive chatbot built with Python, Streamlit, and the Google Gemini API. This application provides a chat interface with history and supports customization of Gemini models.

---

## Features

* **Interactive Chat**: Ask anything and get responses from Gemini.
* **Conversation History**: Full chat history is preserved during a session.
* **Secure API Key Handling**: Uses system environment variables for the API key, with a secure password input field as fallback.
* **Customizable Model**: Choose your Gemini model (default: `gemini-2.5-pro`) via the settings panel.
* **Reset Chat**: Clear the chat history and start fresh with one click.

---

## Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API** (`google-generativeai`)

---

## Setup and Installation

Follow these steps to run the application locally.

### Prerequisites

* Python 3.8+
* A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/krrish4666/Gemini-chatbot.git
   cd Gemini-chatbot
   ```

2. **Install Dependencies**
   Install all the required libraries directly (we’re not using `venv` here).

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Your API Key**
   For the best security, set your Gemini API key as a system environment variable named `GEMINI_API_KEY`.

   * **macOS/Linux**:

     ```sh
     export GEMINI_API_KEY='your_api_key_here'
     ```
   * **Windows (Command Prompt)**:

     ```sh
     set GEMINI_API_KEY=your_api_key_here
     ```
   * **Windows (PowerShell)**:

     ```sh
     $env:GEMINI_API_KEY="your_api_key_here"
     ```

   👉 Alternatively, you can run the app and paste the key into the password field in the sidebar.

4. **Run the Streamlit App**

   ```sh
   streamlit run app.py
   ```

   The application will automatically open in your web browser.

---

⚡ **That’s it!** You now have a working Gemini chatbot running on Streamlit.
