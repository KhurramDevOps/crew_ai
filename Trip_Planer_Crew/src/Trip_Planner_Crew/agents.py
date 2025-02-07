from crewai import Agent
from textwrap import dedent
import os
from dotenv import load_dotenv
from .tools.search_tool import SearchTools
from .tools.calculator_tool import CalculatorTools
from crewai import LLM

load_dotenv()


"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
 - Create a 7-day Trip with detailed per-day plans,
 including budget, packing suggestions, and safety tips.
 

Captain/Manager/Boss:
-Expert Travel Agent


Employees/Experts to hire:
-City Selection Expert
-Local Travel Agent 

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


















class TravelAgents:
    def __init__(self):
        google_api_key = os.getenv("GEMINI_API_KEY")  # Ensure API key is set in the environment

        self.OpenAIGPT35 = LLM(
            model="gemini/gemini-2.0-flash-exp", temperature=0.7, api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c",

        )
        self.OpenAIGPT4 = LLM(
            model="gemini/gemini-2.0-flash", temperature=0.7, api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c",

        )

            # Instantiate tools
        self.search_tool = SearchTools()
        self.calculator_tool = CalculatorTools()


    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in Travel planning and logistics.
                              i have decades of experience making travel Trips  """),
            goal=dedent(f"""Create a 7-day Trip with detailed per-day plans,
                        include budget , packing suggestions and safety requirements"""),
            tools=[SearchTools.search_internet,
                   CalculatorTools.calculate],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="city_selection_expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f""" Select the best cities based on weather ,  season , prices , and traveler  interest"""),
            tools=[SearchTools.search_internet,
                   ],            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def Local_tour_guide(self):
        return Agent(
            role="Local_tour_guide",
            backstory=dedent(f"""Knowledge local guide with extensive information about the city , its attractions and customs"""),
            goal=dedent(f""" Provide the best insights about the selected city """),
            tools=[SearchTools.search_internet,],            verbose=True,
            llm=self.OpenAIGPT35,
        )