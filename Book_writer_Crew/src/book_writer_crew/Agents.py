from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = LLM(model="gemini/gemini-2.0-flash-exp", api_key=api_key)

class BookWriterAgent:

    def Content_Strategist(self):
        return Agent(
            role ="Content Strategist",
            goal=""" Develop a comprehensive content """,
            backstory="",
            verbose="",
            llm=model,
            allow_delegation=True,

        )
    def Writer(self):
        return Agent(
            role ="Content Strategist",
            goal="",
            backstory="",
            verbose="",
            llm=model,
            allow_delegation=True,

        )
   