from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools 
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))

tools = load_tools(['ddg-search', 'wikipedia'], llm= llm)

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
  llm,
  tools,
  prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose= True)

query = """"
I will travel to Lima and Cuzco (Peru) mid May 2025 for 7 days.
I want you to create a travel itinerary for me with historical sites, must see viewpoints, and cultural events that will be happening during the trip.
Include the price for flight tickets from Redding, CA, United States to Lima, Peru.
"""

agent_executor.invoke({"input": query})