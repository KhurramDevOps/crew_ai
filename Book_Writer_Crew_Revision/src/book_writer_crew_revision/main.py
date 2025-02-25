from .agents import MyBookWriterAgent



from crewai import Crew

from .tasks import BookWriterTask

agents = MyBookWriterAgent()
tasks = BookWriterTask()

Topic = "World War 2"


Outline_Writer = agents.Outline_Writer()
Outline_Writer_Task = tasks.Outline_Writer_Task(
    agent=Outline_Writer,
    topic = Topic,
)


crew = Crew(
    tasks = [Outline_Writer_Task],
    agents = [Outline_Writer],
    verbose = True,
)

def BookWriter():
    results = crew.kickoff()
    print(results)