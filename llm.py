from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model='gpt-4o', 
        temperature=0.2, 
        
        api_key=os.getenv('openapi_key'))