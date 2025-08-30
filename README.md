# ⚡ Gemini Streaming Chatbot

A simple, interactive chatbot built with Python, Streamlit, and the Google Gemini API. This application provides a real-time, streaming chat experience and includes a user-friendly interface for interacting with Google's powerful language models.



## Features

-   **Real-time Streaming**: Responses from the Gemini API are streamed word-by-word for a dynamic user experience.
-   **Conversation History**: The app maintains and displays the full conversation history.
-   **Secure API Key Handling**: The app prioritizes using system environment variables for the API key, with a secure password input field as a fallback.
-   **Customizable Model**: Users can specify which Gemini model they want to use through the settings panel.
-   **Reset Chat**: A simple "Reset chat" button to clear the conversation history and start fresh.

## Tech Stack

-   **Python**
--   **Streamlit**
-   **Google Gemini API** (`google-generativeai`)

## Setup and Installation

Follow these steps to run the application locally.

### Prerequisites

-   Python 3.8+
-   A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Steps

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/krrish4666/Gemini-chatbot.git](https://github.com/krrish4666/Gemini-chatbot.git)
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all the required libraries from the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set Your API Key**
    For the best security, set your API key as a system environment variable named `GEMINI_API_KEY`.

    -   **macOS/Linux**:
        ```sh
        export GEMINI_API_KEY='your_api_key_here'
        ```
    -   **Windows (Command Prompt)**:
        ```sh
        set GEMINI_API_KEY=your_api_key_here
        ```
    Alternatively, you can run the app and paste the key into the password field in the sidebar.

5.  **Run the Streamlit App**
    ```sh
    streamlit run app.py
    ```
    The application will open in your web browser.
