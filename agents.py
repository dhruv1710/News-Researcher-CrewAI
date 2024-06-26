from crewai import Agent
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',verbose=True,temerature=0.5,google_api_key=os.getenv('GOOGLE_API_KEY'))

news_researcher = Agent(role = "Senior Researcher", goal="Uncover ground breaking technologies in {topic}",verbose=True, memory=True,backstory = "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world.",tools=[tool],llm=llm,allow_delegation=True, )

writer_agent = Agent(role = "Writer", goal="Narrate compelling tech stories about {topic}",verbose=True, memory=True,backstory = "You're a talented writer, able to craft compelling stories that captivate your audience.",llm=llm,allow_delegation=False, )