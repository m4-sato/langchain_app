import os
from dotenv import load_dotenv
import openai
import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model_name="text-davinci-003", temperature=0)

result = llm("自己紹介をしてください。")
print(result)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちわ！私はジョンです。"),
    AIMessage(content="こんにちわ、ジョンさん！どのようなお手伝いができますか?"),
    HumanMessage(content="私の名前を知っていますか？"),
]

result = chat(messages)
print(result.content)

chat = ChatOpenAI(model_name="gpt-3.5-turbo",
                temperature=0,
                streaming=True,
                callbacks=[StreamingStdOutCallbackHandler()],
                )

messages = [HumanMessage(content="自己紹介をしてください。")]
result = chat(messages)

template = """
以下の料理のレシピを教えてください。

料理名：{dish}
"""

prompt = PromptTemplate(
    input_variables=["dish"],
    template=template,
)

result = prompt.format(dish="カレー")
print(result)

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("あなたは{country}料理のプロフェッショナルです。"),
    HumanMessagePromptTemplate.from_template("以下の料理レシピを教えてください\n\n料理名: {dish}")
])

messages = chat_prompt.format_prompt(country="イギリス", dish = "肉じゃが").to_messages()
print(messages)

class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the fish")
    steps: list[str] = Field(description="steps to make the dish")
    
parser = PydanticOutputParser(pydantic_object=Recipe)

format_instructions = parser.get_format_instructions()

print(format_instructions)

template = """料理のレシピを教えてください。
{format_instructions}
料理名: {dish}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["dish"],
    partial_variables={"format_instructions": format_instructions}
)

formatted_prompt = prompt.format(dish="カレー")

print(formatted_prompt)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
messages = [HumanMessage(content=formatted_prompt)]
output = chat(messages)
print(output.content)

recipe = parser.parse(output.content)
print(type(recipe))
print(recipe)