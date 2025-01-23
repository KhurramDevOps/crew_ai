# import json
import os
from crewai import Agent, Task, Crew ,Process
from dotenv import load_dotenv

load_dotenv()
Gen_Ai_Key = os.getenv("GEMINI_API_KEY")
Model_name = os.getenv("MODEL")

# define the researcher_Agent

researcher_agent  = Agent(
  role= "{topic}Senior Data Researcher",
  goal="Uncover cutting-edge developments in {topic}",
  backstory= """You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.""")

# define the reporting_Analyst_agent 
reporting_analyst_agent = Agent(
  role = 
    "{topic} Reporting Analyst",
  goal = 
    "Create detailed reports based on {topic} data analysis and research findings",
  backstory = 
    """You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.""")

# NOW WE ASSIGN THE AGENTS TO THE TASKS

# LEARNING AND IMPLEMENTING TASKS DEEPLY !

# 
research_task = Task(
    description="""
        Conduct a thorough research about AI Agents.
        Make sure you find any interesting and relevant information given
        the current year is 2024.
    """,
    expected_output="""
        A list with 10 bullet points of the most relevant information about AI Agents
    """,
    agent=researcher_agent )

reporting_task2 = Task(
      description="""
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
    """,
    expected_output="""
        A fully fledge reports with the mains topics, each with a full section of information.
        Formatted as markdown without '```'
    """,
    agent=reporting_analyst_agent,
    # output_file="Report.md"  # we specify the output file name and it will be saved in the current directory
)

crew = Crew(
    agents = [researcher_agent,reporting_analyst_agent],
    tasks = [research_task,reporting_task2],
    verbose = True
)

result = crew.kickoff()
# print(result)

# TASK OUTPUT ATTRIBUTES
#Understanding task outputs is crucial for building effective AI workflows. 
# CrewAI provides a structured way to handle task results through the TaskOutput class, 
# which supports multiple output formats and can be easily passed between tasks.

# Let's see how to use TaskOutput to handle task results:

task_output = research_task.output

print(f"Task Description : {task_output.description}")
print(f"Task Summary : {task_output.summary}")
print(f"RAw Output : {task_output.raw}") # raw output is the actual output of the task

# checking if the output in json_dict format 
# if task_output.json_dict():
#     print(f"JSON OUTput: {json.dumps(task_output.json_dict, indent = 2)}")
# else:
#     print("No JSON output available")


# checking if the output in Pydantic format
# if task_output.Pydantic():
#     print(f"Pydantic Output: {task_output.pydantic}")
# else:
#     print("No Pydantic output available")