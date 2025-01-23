import os
from crewai import Agent , Crew ,Task
from dotenv import load_dotenv
from Calculator_Tool import calculate


load_dotenv()

Genai_key = os.getenv("GEMINI_API_KEY")
Model_name = os.getenv("MODEL")

print("###---WElcome to the MATh Whiz---####")
math_input = input("\033[34m Enter Your math problem: \033[0m")

math_agent = Agent(
    # THESE ARE MOST IMPORTANT USED ATTRIBUTES 
    role  = "MATH Magician",
    goal  = "You are able to evaluate any math expression",
    backstory = "YOU ARE A MATH WHIZ",
    verbose= True, # Print out the agent's thoughts and whats happening the in the background by default it is FALSE
    tools = [calculate], # it always take list of tools, but you can add more tools later
   memory = True , # memory attribute is used if you want to remember the previous conversations
    

    # THE FOLLOWING BELOW ARE THE AGENTS FURTHER ATTRIBUTES
    # The following attributes are used to MAKE THE AGENT MORE ACCURATE

    #llm="gpt-4",  # Default: OPENAI_MODEL_NAME or "gpt-4"
    function_calling_llm=None,  # Optional: Separate LLM for tool calling
    allow_delegation=False,  # Default: False
    max_iter=20,  # Default: 20 iterations
    max_rpm=None,  # Optional: Rate limit for API calls
    max_execution_time=None,  # Optional: Maximum execution time in seconds
    max_retry_limit=2,  # Default: 2 retries on error
    allow_code_execution=False,  # Default: False
    code_execution_mode="safe",  # Default: "safe" (options: "safe", "unsafe")
    respect_context_window=True,  # Default: True
    use_system_prompt=True,  # Default: True
    knowledge_sources=None,  # Optional: List of knowledge sources
    embedder_config=None,  # Optional: Custom embedder configuration
    system_template=None,  # Optional: Custom system prompt template
    prompt_template=None,  # Optional: Custom prompt template
    response_template=None,  # Optional: Custom response template
    step_callback=None,  # Optional: Callback function for monitoring

# THE DEFAULT VALUES ARE USED IF YOU DONT SPECIFY ANYTHING
# YOU CAN CHANGE THEM AS PER YOUR NEEDS
)




# TASK Is explained in more detailed in the next section
task = Task(
    description = f"Evaluate the math expression: {math_input}",
    expected_output =  "Give Full description in Bullet Points",
    agent = math_agent,

)
crew = Crew(
    agents= [math_agent],
    tasks = [task],
    verbose = True,
    
    )

result = crew.kickoff()
print(result)  # prints the result of the math problem




