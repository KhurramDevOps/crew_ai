from crewai import Agent, LLM 

from dotenv import load_dotenv


load_dotenv()

model= LLM(model="gemini/gemini-2.0-flash-exp")

class MyBookWriterAgent:

    def Outline_Writer(self):
        return Agent(
            role ="Outline_Writer",
            goal=" Develop a detailed outline for the book",
            backstory=" I am a season expert in writing book outlines, I have 10+ years of experience in writing book outlines for various genres",
            verbose=True,
            llm = model,
        )

    
