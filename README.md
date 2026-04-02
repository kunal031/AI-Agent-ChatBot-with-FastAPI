# LangGraph AI Agent Chatbot with FastAPI

This project is an AI-powered chatbot that uses LangGraph, Groq, and Tavily to provide intelligent and conversational responses. The backend is built with FastAPI and the frontend is a user-friendly interface created with Streamlit.

# Tools and Technologies

- LangGraph React Agents
- FastAPI for API calls
- Groq and OpenAI for LLM
- Streamlit for UI
- Langchain for tools
- Tavily for web search tool
- Uvicorn for hosting
- Python 3.10+
- VS Code

# Architecture

![AI Agent Architecture](Architecture.png)

## Demo

Here is a video demonstrating the chatbot in action:

https://youtu.be/e5g6OP7kAy4

## Features

- **Conversational AI:** Powered by state-of-the-art LLMs from Groq and OpenAI.
- **Web Search:** Agent can perform web searches using Tavily to provide up-to-date information.
- **Customizable:** You can define the agent's personality and behavior with a system prompt.
- **Easy to Use:** The Streamlit frontend provides a simple and intuitive interface for interacting with the chatbot.
- **FastAPI Backend:** The robust and scalable backend is built with FastAPI.

## Screenshot

![AI Agent UI](AI%20Agent%20UI.png)

## Getting Started

### Prerequisites

- Python 3.11 or later
- An active virtual environment
- API keys for Groq, Tavily, and OpenAI

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/kunal031/AI-Agent-ChatBot-with-FastAPI.git
    cd AI-Agent-ChatBot-with-FastAPI
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** in the root of the project and add your API keys:
    ```
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    TAVILY_API_KEY="YOUR_TAVILY_API_KEY"
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

### Usage

1.  **Start the backend server:**

    ```bash
    python backend.py
    ```

2.  **In a new terminal, start the frontend application:**

    ```bash
    streamlit run frontend.py
    ```

3.  Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Project Structure

```
.
├── ai_agent.py         # Core logic for the AI agent
├── backend.py          # FastAPI backend
├── frontend.py         # Streamlit frontend
├── .gitignore          # Files and directories to ignore
├── requirements.txt    # Project dependencies
└── README.md           # This file
```
