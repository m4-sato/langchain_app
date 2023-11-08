import os
from dotenv import load_dotenv
import openai
import json
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
tools = load_tools(["terminal"])
agent_chain = initialize_agent(
    tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

result = agent_chain.run("sample_dataディレクトリにあるファイルの一覧を教えて")
print(result)