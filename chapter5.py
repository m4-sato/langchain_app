import os
from dotenv import load_dotenv
import openai
import json
from langchain.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def file_filter(file_path):
    return file_path.endswith(".mdx")

loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path = "./langchain",
    branch = "master",
    file_filter=file_filter,
    )

raw_docs = loader.load()
print(len(raw_docs))

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=0)

docs = text_splitter.split_documents(raw_docs)
len(docs)

embeddings = OpenAIEmbeddings()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか?"

vector = embeddings.embed_query(query)
print(len(vector))
print(vector)

db = Chroma.from_documents(docs, embeddings)

retriever = db.as_retriever()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか?"
context_docs = retriever.get_relevant_documents(query)
print(f"len = {len(context_docs)}")

first_doc = context_docs[0]
print(f"metadata = {first_doc.metadata}")
print(first_doc.page_content)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever = retriever)
result = qa_chain.run(query)
print(result)