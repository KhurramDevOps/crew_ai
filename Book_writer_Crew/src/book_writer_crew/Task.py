from crewai import Task , LLM 
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

research_Tool= SerperDevTool()

class BookWriterTasks():

    def Content_Strategist_Task(self, agent,Book_Title,Author_Name, Target_Audience, Writing_Style):
        return Task(
            description="",
            agent=agent,
            tools = [research_Tool],
            expected_output="",
            
        )

    def Writer_Task(self, agent, context ):
        return Task(
            description="",
            agent=agent,
            context= context,
            expected_output="",
            )
    
    