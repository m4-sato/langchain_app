import os
from dotenv import load_dotenv
import openai
import json
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)
tools = load_tools(["terminal"])
agent_chain = initialize_agent(
    tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# result = agent_chain.run("langchain_appフォルダ内のファイルの一覧を教えて")
# print(result)

from langchain.tools import Tool

def my_super_func(param):
    return "42"

tools = [
    Tool.from_function(
        func=my_super_func,
        name="The_Answer",
        description="生命、宇宙、そして万物についての究極の疑問の答え"
    ),
]

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain

summarize_template = """以下の文章を結論だけ一言に要約してください。

{input}
"""
summarize_prompt = PromptTemplate(
    input_variables=["input"],
    template=summarize_template,
)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)
summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)

tools = [
    Tool.from_function(
        func=summarize_chain.run,
        name="Summarizer",
        description="Text summarization tool"
    )
]

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["terminal"])
agent_chain = initialize_agent(
    tools, chat, agent=AgentType.OPENAI_FUNCTIONS
)

# result = agent_chain.run("langchain_appフォルダ内のファイルの一覧を教えて")
# print(result)

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["ddg-search"])
agent_chain = initialize_agent(
    tools, chat, agent=AgentType.OPENAI_MULTI_FUNCTIONS
)

result = agent_chain.run("東京と大阪の天気を教えて")
print(result)