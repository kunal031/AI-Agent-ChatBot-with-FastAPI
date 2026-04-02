# ===========================================================
#           Phase 2 : setup backend (with FastAPI)
# ===========================================================

# Step 1 : setup pydantic model ( schema validation )

''' when two systems communicate with each other specially through api calls, then there is fixed standard , standard means fixed predefined way of how to send data and how to recieve data. '''

""" to communicate through api calls , there is some specific format which defines how to send request and how to recieve output.

***.  Unlike a natural conversation, APIs require structured data formats (usually JSON or XML) and set rules, where every request must include specific components—like authentication, headers, and a body—to be understood by the server

** why specific structure exists :-
1. Consistency: It allows different software systems, potentially written in different programming languages, to understand each other without ambiguity.

2. Security: Structured requests allow servers to easily validate authentication tokens and API keys.

3. Efficiency: It enables the server to process high volumes of requests quickly without storing session memory
"""

# ======================================================================================

# Q: what is Pydentic?
# -> Pydentic is a popular, high-performance library in python used for data validation.
# -> Pydantic is a Data Validation library. Its only job is to ensure that the data entering your Python code matches the "shape" and "type" you expect.
# -> Pydentic ensures data entering your application is valid and raise errors immidiately if validation fails.
# -> It uses standard type hints to enforce data types, structures, and constraints.

# Data Validation: 
#         Uses Python type hints to validate data at runtime, ensuring it matches the   expected structure.

# ======================================================================================

from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

'''
->   When you guide an LLM to act as an agent, the LLM often makes mistakes—it might forget a field or provide a string where you need a number.

< == > Pydantic's BaseModel acts as the "Contract":
            1. It validates the LLM's output.

            2. If the LLM fails the validation, Pydantic catches the error.

            3. You can then send that error back to the LLM and say, "Your output didn't match the BaseModel, try again.


--- How it works :-
      When you create an instance of a class that inherits from BaseModel, Pydantic triggers this hidden process.
'''
'agar specified format m data nhi ayega to backend error throw karega'
class RequestState(BaseModel):
    model : str
    model_provider : str
    system_prompt : str
    message : List[str]
    allow_search : bool
'''jb frontend se koi information payload uthayega aur information iss specified format m nahi hoga to backend fir usko process nhi k skta'''

# Step 2 : setup AI Agent from FronEnd Request
'''ab hame endpoint banana hai , jis endpoint p hamara frontend message bhejega'''
from fastapi import FastAPI


ALLOWED_MODEL_NAME = ["llama-3.3-70b-versatile","mistral-8x7b-32768","gpt-4o-mini"]
'''
ab hame ak app setup krna hai backend ki so that jo v information aye wo ak endpoint p jaye processing k liye
'''
app = FastAPI(title="LangGraph AI Agent") 
'create instance of fastapi'

@app.post("/chat")     # ak post endpoint setup krna h, so jb v frontend se post request aye to kis endpoint p recieve ho

def chat_endpoint(request:RequestState):
    '''
      what is this chat endpoint ?

      Api endpoint to interact with chatbot using LangGraph and search tool.
      It dynamically selects model specified in request.
    '''
    if request.model not in ALLOWED_MODEL_NAME:
        return {"error":"Invalid model name. Kindly select a valid AI model"}
    
    # create ai agent and get response from it

    llm_id = request.model
    provider = request.model_provider
    system_prompt = request.system_prompt
    allow_search = request.allow_search
    query = request.message[-1]

    response = get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)
    return {"response" : response}
    

# Step 3 : Run app and explore swagger UI docs

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app,host="127.0.0.1",port=9999)
