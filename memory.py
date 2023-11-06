from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
import openai
import json
import logging
import langchain

logging.getLogger("openai").setLevel(logging.DEBUG)
langchain.verbose = True
langchain.debug = True

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model_name="gpt-4", temperature=0)
conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory(),
)

while True:
    user_message = input("You:")
    ai_message = conversation.run(input=user_message)
    print(f"AI: {ai_message}")