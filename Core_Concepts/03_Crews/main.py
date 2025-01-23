# Creating Crews 
# ==============
#
# This module contains functions for creating crews.

from crewai import Agent, Crew, Task, Process 
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
# Load environment variables from .env file
# This is used to store sensitive information such as API keys
# and database credentials.

gen_ai_key = os.getenv("GEMINI_API_KEY")
Model = os.getenv("MODEL")

class CreativeContentCrew:
    def content_creator(self ) -> Agent:
        return Agent(
            role= "Content Creator",
            goal= "Develop Creative and engaging content for marketing campaigns",
            backstory = "A visionary creator with expertise in crafting compelling narratives and visuals, ",
            verbose = True
        )
    
    def campaign_planner(self)->Agent:
        return Agent(
        role = "Campaign Planner",
        goal = "Strategize and Outline marketing campaign timelines and goals  ",
        backstory = "A meticulous planner with a track record or executing successful campaigns.  ",
        verbose = True
        )
    
    def task_brainstorm_ideas(self)-> Task:
        return Task(
        description = "Brainstorm creative ideas fro a new product launch campaign.",
        expected_output = "A list of 5 unique and innovative marketing ideas for the project launch.",
        agent = self.content_creator()
        )
    
    def task_plan_campaign(self) -> Task:
        return Task(
            description = " Create a detailed plan for implementing the selected marketing ideas.",
            expected_output = "A step-by-step campaign plan , including timelines, milestones, resources, and budget.",
            agent = self.campaign_planner()
        )
    
    # Define the crew
    # A crew is a collection of tasks and agents that work together to achieve a common goal.
    
    # THE CREW HAVE SOME ATTRIBUTES WHICH ARE USED TO DETERMINE HOW THEY WORK TOGETHER
    # AGENTS,
    # TASKS,
    # PROCESS
    # THE FIRST TWO ARE COMPULSORY TO RUN THE CREW 
    def crew(self) -> Crew:
        return Crew(
            agents = [self.content_creator(),self.campaign_planner()],
            tasks = [self.task_brainstorm_ideas(),self.task_plan_campaign()],
            process = Process.sequential,
            verbose = True # Optional, default is False
            # USING VERBOSE = TRUE WILL PRINT OUT THE DETAILS OF THE CREW
            
        )
        
        
crew_instance = CreativeContentCrew().crew()

result = crew_instance.kickoff() # kickoff mean start the crew's task execution

print(f"Crew Execution Result: {result}")  # Output: {'agents': ['Content Creator', 'Campaign Planner'], 'tasks


# Accessing the crew output
# NOW THeSE ARE NOT ACCESSIBLE DIRECTLY FROM THE CREW INSTANCE
# BUT WE CAN ACCESS THEM FROM THE RESULT

# print(f"Raw Output: {crew_instance.raw}") #The raw output of the crew. This is the default format for the output.

#print(f"Tasks Output: {result.tasks_output}") #A list of TaskOutput objects, each representing the output of a task in the crew. 

#print(f"Token Usage: {result.token_usage}") # A summary of token usage, providing insights into the language model’s performance during execution.


# DIFFERENT WAYS TO KICKOFF A CREW
# 1. kickoff()
# 2. kickoff_for_each()      
# 3. kickoff_async()
# 4. kickoff_for_each_async()

# FOR MORE DETAILS OF THIS CHECK THE README FILE THANK YOU.  # noqa: E501

# the first one is written above

# Example of using kickoff_for_each
# inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
# results = crew_instance.kickoff_for_each(inputs=inputs_array)
# for result in results:
#     print(result)

# Example of using kickoff_async
# Make sure to run this in a async environment
# inputs = {'topic': 'FACE CREAM PRODUCT LAUNCH'}
# async def run_async_task():
#     async_result = await crew_instance.kickoff_async(inputs=inputs)
#     print(async_result)

# asyncio.run(run_async_task())

# # Example of using kickoff_for_each_async
# Make sure to run this in a async environment

# inputs_array = [{'topic': 'AI EFFECT ON EDUCATION'}, {'topic': 'AI in finance'}]
# async def run_for_each_task():
#     async_results = await crew_instance.kickoff_for_each_async(inputs=inputs_array)
#     for async_result in async_results:
#         print(async_result)

# asyncio.run(run_for_each_task())

