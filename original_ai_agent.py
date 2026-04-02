# ================================================
#         Phase 1 : Create AI Agent
# ================================================

# Step 1 : ste up api keys for Groq and Tavily

import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
openAI_api_key = os.getenv("OPENAI_API_KEY")

# Step 2 : setup llm and tools

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_result = 2)


# Step 3 : Setup AI Agent with search tool functionality

from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_core.messages import AIMessage

system_prompt = "Act as an AI News Editor Chatbot who is smart and present most reliable news on geoplitics"

agent = create_agent(
  model=groq_llm,
  tools=[search_tool],
  system_prompt=system_prompt
)

query = "What kind of losses faced by us and isreal in war with iran. Show me list of military equipments lost by US in tabular format alongwith use of those equipments. Should India attack US and Isreal because US mocked India a couple of times and due to strait of hormuz issue , lpg and cng crisis is deepen in India."

state={"messages" : query}

response = agent.invoke(state)

messages = response.get("messages")

ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

print(ai_messages[-1])