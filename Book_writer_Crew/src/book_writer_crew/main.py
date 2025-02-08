from .Agents import BookWriterAgent
from .Task import BookWriterTasks
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


model = LLM(model="gemini/gemini-2.0-flash-exp", api_key=api_key)



word_count = 2000
Book_Title = "The Era of Artificial Intelligence"
Author_Name= "Muhammad Khurram"
Target_Audience = "Youngsters"
Writing_Style = "Narrative"


# obj
agents= BookWriterAgent()

tasks = BookWriterTasks()

Content_Strategist =  agents.Content_Strategist()
Writer = agents.Writer()

# Tasks

Content_Strategist_Task = tasks.Content_Strategist_Task(
    agent = Content_Strategist,
    word_count = word_count,
    Book_Title = Book_Title,
    Author_Name = Author_Name,
    Target_Audience = Target_Audience,
    Writing_Style = Writing_Style
)

Writer_Task = tasks.Writer_Task(
    agent = Writer,
    context = [Content_Strategist_Task],
)

crew = Crew(
    agents = [Content_Strategist, Writer],
    tasks = [Content_Strategist_Task, Writer_Task],
    verbose = True,
    process = Process.hierarical,
    manager_llm = model 


)