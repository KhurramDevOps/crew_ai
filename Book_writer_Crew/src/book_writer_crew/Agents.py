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
            goal="""Develop a comprehensive content strategy for a user defined word book, including chapter outlines""",
            backstory="Seasoned content strategist with 10 years of experience in planning and organizing large-scale content projects. Skilled in audience analysis, content mapping, and SEO best practices.",
            verbose=True,
            llm = model,
            # allow_delegation=True,

        )
    def Writer(self):
        return Agent(
            role = "Writer",
            goal = """ Draft the user defined words book based on the content strategy ensuring the writing is compelling and accessible. """,
            backstory= "Professional writer with a portfolio of published works, including books, articles, and blogs. Skilled in engaging storytelling and clear, concise communication.",
            verbose=True,
            llm = model,
            # allow_delegation=True,

        )
   