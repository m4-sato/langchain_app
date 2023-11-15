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

import json

from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from langchain.prompts import ChatPromptTemplate

schema = {
    "properties": {
        "person_name":{"type":"string"},
        "person_height":{"type":"integer"},
        "person_hair_color":{"type":"string"},
        "dog_name":{"type":"string"},
        "dog_breed":{"type":"string"},
    },
    "required": ["person_name", "person_height"],
}
text = """
Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him.
Claudia is a brunette and Alex is blonde.
Alex's dog Frosty is a labrador and likes to play hide and seek.
"""

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_extraction_chain(schema, chat)

people = chain.run(text)
print(json.dumps(people, indent=2))

# ------------
# LLMによる評価
# ------------

from langchain.chat_models import ChatOpenAI
from langchain.evaluation import load_evaluator

chat = ChatOpenAI(model='gpt-4', temperature=0)

evaluator = load_evaluator("qa", eval_llm=chat)

result = evaluator.evaluate_strings(
    input="私は市場へ行って10このリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それから5つのリンゴを買って1つ食べました。残りは何個ですか?",
    prediction="""1最初に10個のリンゴを買い、その中から隣人と修理工に2つずつ渡しました。そのため、まず手元に残ったリンゴは10-2-2=6個です。
    次に5個のリンゴを買い、その中から1個食べました。そのため、手元に残ったリンゴは6 + 5 - 1=10個です。""",
    reference="10個"
)

print(result)
