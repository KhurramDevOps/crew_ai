from crewai import Task , LLM 
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

research_Tool= SerperDevTool()

class BookWriterTasks():

    def Content_Strategist_Task(self, agent,word_count,Book_Title,Author_Name, Target_Audience, Writing_Style):
        return Task(
           description= f"""Plan the content for a  {word_count}-word book by analyzing the audience, mapping out chapters, conducting keyword research, and creating an outline.
            
            Parameters :

            Book_Title : {Book_Title},
            Author_Name : {Author_Name},
            Target_Audience : {Target_Audience},
            Writing_Style : {Writing_Style},
            word_count : {word_count},

            
            """,

            tools=[research_Tool],
            agent=agent,
            expected_output= " A detailed strategy document including chapter outlines and keyword list.",

            
        )

    def Writer_Task(self, agent, context ,callback):
        return Task(
           description= "Write the book based on the strategy and expert content, ensuring engaging and accessible writing.",
            context = context,
            agent=agent,
            expected_output= " A compelling book draft.",
            callback=callback
            )
    
    