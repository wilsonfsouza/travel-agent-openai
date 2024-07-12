from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.agent_toolkits.load_tools import load_tools 
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))

query = """"
I will travel to Lima and Cuzco (Peru) mid May 2025 for 7 days.
I want you to create a travel itinerary for me with historical sites, must see viewpoints, and cultural events that will be happening during the trip.
Include the price for flight tickets from Redding, CA, United States to Lima, Peru.
"""

def researchAgent(query, llm):
  tools = load_tools(['ddg-search', 'wikipedia'], llm= llm)
  prompt = hub.pull("hwchase17/react")
  agent = create_react_agent(llm, tools, prompt)
  agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose= True)
  webContext = agent_executor.invoke({"input": query})
  return webContext['output']


print(researchAgent(query, llm))

def loadData():
  loader = WebBaseLoader(
    web_paths= ("https://www.dicasdeviagem.com/inglaterra/"),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("postcontentWrap", "pagetitleloading background-imaged loading-dark")))
  )
  docs = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  splits = text_splitter.split_documents(docs)
  vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings)
  retriever = vectorstore.as_retriever()
  return retriever

def getRelevantDocs(query):
  retriever = loadData()
  relevant_documents = retriever.invoke(query)
  return relevant_documents

def supervisorAgent(query, llm, webContext, relevant_documents):
  prompt_template = """
  You are the surpevisor of a travel agency. Your final answer must be a complete and detailed travel itinerary.
  Use the context of events and flight ticket prices, the user input, and the relevant documents to elaborate the travel itinerary.
  Context: {webContext}
  Relevant documents: {relevant_documents}
  User: {query}
  Assistant:
  """

  prompt = PromptTemplate(
    input_variables=['webContext', 'relevant_documents', 'query'],
    template=prompt_template
  )

  sequence = RunnableSequence(prompt | llm)
  response = sequence.invoke({"webContext": webContext, "relevant_documents": relevant_documents, "query": query})
  return response