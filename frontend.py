# Step 1 : Setup UI with streamlit (model_provider,model,system_prompt,query)

import streamlit as st

st.set_page_config(page_title="LangGraph AI Agent",layout="centered")
st.title("AI Chatbot Agent")
st.write("Create and Interact with AI Agent")


system_prompt = st.text_area("Define your AI Agent : ",height=70,placeholder="Type your system prompt here ....")

MODEL_NAME_GROQ=["llama-3.3-70b-versatile","mistral-8x7b-32768"]
MODEL_NAME_OPENAI=["gpt-4o-mini"]

provider = st.radio("Select Provider :",("Groq","OpenAI"))

if provider == "Groq":
  selected_model = st.selectbox("Select Groq Model :",MODEL_NAME_GROQ)
elif provider == "OpenAI":
  selected_model = st.selectbox("Select Groq Model :",MODEL_NAME_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter Your Query Here : ",height=150,placeholder="Ask Anything")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask AI Agent"):
  # Step 2 : Connect with bakend via URL
  import requests
  payload = {
    "model" : selected_model,
    "model_provider" : provider,
    "system_prompt" : system_prompt,
    "message" : [user_query],
    "allow_search" : allow_web_search
  }

  response = requests.post(API_URL,json=payload)

  # get response from ai agent
  if response.status_code == 200:
    response_data = response.json()
    if "error" in response_data:
      st.error(response_data["error"])
    else :
      st.subheader("Agent Response")
      st.markdown(f"*** final response *** {response_data['response']}")

