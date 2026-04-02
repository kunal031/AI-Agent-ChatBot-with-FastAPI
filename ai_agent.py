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



# Step 3 : Setup AI Agent with search tool functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage



def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
  if provider=="Groq":
    llm = ChatGroq(model=llm_id)
  elif provider=="OpenAI":
    llm = ChatOpenAI(model=llm_id)

  tools = [TavilySearchResults(max_results=2)] if allow_search else []
  
  agent_executor = create_react_agent(llm, tools=tools)

  messages = [SystemMessage(content=system_prompt), HumanMessage(content=query)]
  
  response = agent_executor.invoke({"messages": messages})
  
  return response["messages"][-1].content