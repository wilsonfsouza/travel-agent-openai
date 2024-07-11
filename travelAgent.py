from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools 
from langchain.agents import initialize_agent

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))

tools = load_tools(['ddg-search', 'wikipedia'], llm= llm)

agent = initialize_agent(
  tools,
  llm,
  agent='zero-shot-react-description',
  verbose = True
)

query = """"
I will travel to Lima and Cuzco (Peru) mid May 2025 for 7 days.
I want you to create a travel itinerary for me with historical sites, must see viewpoints, and cultural events that will be happening during the trip.
Include the price for flight tickets from Redding, CA, United States to Lima, Peru.
"""

agent.run(query)