<h1><strong>CORE CONCEPT : CREWS IN </strong> <img src="https://i.postimg.cc/G3xn0D6W/crew-only-logo.png](https://postimg.cc/F1zB3Yrp)" style="width: 25%;" alt="Crew AI Logo"></h1>

## **CREWS**

Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.

## **WHAT IS A CREW?**

A **Crew** in CrewAI is a collection of agents and tasks that work together to accomplish a common objective. Crews can be customized with various attributes to control how they operate and execute tasks.

## **CREW EXECUTION PROCESS**

### Crew Attributes.

- **Sequential Process**: Tasks are executed one after another, allowing for a linear flow of work.

- **Hierarchical Process**: A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding.

  > **Note**: A `manager_llm` or `manager_agent` is required for this process and it’s essential for validating the process flow.

- Here’s a breakdown of the key attributes of a Crew:

| Attribute                           | Parameters             | Description                                                                                                                                                                                   |
| ----------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tasks**                           | `tasks`                | A list of tasks assigned to the crew.                                                                                                                                                         |
| **Agents**                          | `agents`               | A list of agents that are part of the crew.                                                                                                                                                   |
| **Process (optional)**              | `process`              | The process flow (e.g., sequential, hierarchical) the crew follows. Default is sequential.                                                                                                    |
| **Verbose (optional)**              | `verbose`              | The verbosity level for logging during execution. Defaults to False.                                                                                                                          |
| **Manager LLM (optional)**          | `manager_llm`          | The language model used by the manager agent in a hierarchical process. Required when using a hierarchical process.                                                                           |
| **Function Calling LLM (optional)** | `function_calling_llm` | If passed, the crew will use this LLM to perform function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew’s LLM for function calling. |
| **Config (optional)**               | `config`               | Optional configuration settings for the crew, in JSON or `Dict[str, Any]` format.                                                                                                             |
| **Max RPM (optional)**              | `max_rpm`              | Maximum requests per minute the crew adheres to during execution. Defaults to None.                                                                                                           |
| **Language (optional)**             | `language`             | Language used for the crew, defaults to English.                                                                                                                                              |
| **Language File (optional)**        | `language_file`        | Path to the language file to be used for the crew.                                                                                                                                            |
| **Memory (optional)**               | `memory`               | Utilized for storing execution memories (short-term, long-term, entity memory).                                                                                                               |
| **Memory Config (optional)**        | `memory_config`        | Configuration for the memory provider to be used by the crew.                                                                                                                                 |
| **Cache (optional)**                | `cache`                | Specifies whether to use a cache for storing the results of tools’ execution. Defaults to True.                                                                                               |
| **Embedder (optional)**             | `embedder`             | Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.                                                                    |
| **Full Output (optional)**          | `full_output`          | Whether the crew should return the full output with all tasks outputs or just the final output. Defaults to False.                                                                            |
| **Step Callback (optional)**        | `step_callback`        | A function that is called after each step of every agent. This can be used to log the agent’s actions or to perform other operations.                                                         |
| **Task Callback (optional)**        | `task_callback`        | A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.                                                              |
| **Share Crew (optional)**           | `share_crew`           | Whether you want to share the complete crew information and execution with the CrewAI team.                                                                                                   |
| **Output Log File (optional)**      | `output_log_file`      | Whether you want to have a file with the complete crew output and execution. Defaults to `logs.txt`.                                                                                          |
| **Manager Agent (optional)**        | `manager_agent`        | Sets a custom agent that will be used as a manager.                                                                                                                                           |
| **Prompt File (optional)**          | `prompt_file`          | Path to the prompt JSON file to be used for the crew.                                                                                                                                         |
| **Planning (optional)**             | `planning`             | Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks.                                              |
| **Planning LLM (optional)**         | `planning_llm`         | The language model used by the AgentPlanner in a planning process.                                                                                                                            |

### Example Code Snippet for Creating a Crew

Here’s an example of how to create a Crew with agents and tasks:

```python
from crewai import Agent, Crew, Task, Process

class CreativeContentCrew:
    def content_creator(self) -> Agent:
        return Agent(
            role="Content Creator",
            goal="Develop Creative and engaging content for marketing campaigns",
            backstory="A visionary creator with expertise in crafting compelling narratives and visuals.",
            verbose=True
        )

    def campaign_planner(self) -> Agent:
        return Agent(
            role="Campaign Planner",
            goal="Strategize and Outline marketing campaign timelines and goals",
            backstory="A meticulous planner with a track record of executing successful campaigns.",
            verbose=True
        )

    def task_brainstorm_ideas(self) -> Task:
        return Task(
            description="Brainstorm creative ideas for a new product launch campaign.",
            expected_output="A list of 5 unique and innovative marketing ideas for the project launch.",
            agent=self.content_creator()
        )

    def task_plan_campaign(self) -> Task:
        return Task(
            description="Create a detailed plan for implementing the selected marketing ideas.",
            expected_output="A step-by-step campaign plan, including timelines, milestones, resources, and budget.",
            agent=self.campaign_planner()
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.content_creator(), self.campaign_planner()],
            tasks = [self.task_brainstorm_ideas(),self.task_plan_campaign()],
            process = Process.sequential,
            verbose = True)
```

### Example Code Snippet for Running a Crew

Here’s an example of how to run a Crew:

```python
crew_instance = CreativeContentCrew().crew()

result = crew_instance.kickoff() # kickoff mean start the crew's task execution

print(f"Crew Execution Result: {result}")
```

## **Crew Output**

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class. This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models. The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

## **Crew Output Attributes**

| Attribute    | Parameters     | Type                       | Description                                                                                          |
| ------------ | -------------- | -------------------------- | ---------------------------------------------------------------------------------------------------- |
| Raw          | `raw`          | `str`                      | The raw output of the crew. This is the default format for the output.                               |
| Pydantic     | `pydantic`     | `Optional[BaseModel]`      | A Pydantic model object representing the structured output of the crew.                              |
| JSON Dict    | `json_dict`    | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the crew.                                               |
| Tasks Output | `tasks_output` | `List[TaskOutput]`         | A list of TaskOutput objects, each representing the output of a task in the crew.                    |
| Token Usage  | `token_usage`  | `Dict[str, Any]`           | A summary of token usage, providing insights into the language model’s performance during execution. |

### Crew Output

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class. This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models. The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

## ACCESSING CREW OUTPUT

You can access the output of a crew using the `CrewOutput` class. Here’s an
example:

```python
print(f"Raw Output: {crew_instance.raw}") #The raw output of the crew. This is the default format for the output.

print(f"Tasks Output: {result.tasks_output}") #A list of TaskOutput objects, each representing the output of a task in the crew.

print(f"Token Usage: {result.token_usage}") # A summary of token usage, providing insights into the language model’s performance during execution.
```

# Different Ways to Kick Off a Crew

Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.

1. **`kickoff()`**: Starts the execution process according to the defined process flow.
2. **`kickoff_for_each()`**: Executes tasks for each agent individually.
3. **`kickoff_async()`**: Initiates the workflow asynchronously.
4. **`kickoff_for_each_async()`**: Executes tasks for each agent individually in an asynchronous manner.

- EXAMPLE OF KICKOFF FOR EACH

```python
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = crew_instance.kickoff_for_each(inputs=inputs_array)
for result in results:
     print(result)

```

- EXAMPLE OF KICKOFF ASYNC
- MAKE SURE TO HANDLE THE ASYNC RESULT PROPERLY
- YOU CAN USE `asyncio` TO HANDLE THE ASYNC RESULT
- WITH OUT `async` function the `kickoff_async` will return a coroutine object . And you need to use `await` to get the result.

```python
inputs = {'topic': 'FACE CREAM PRODUCT LAUNCH'}
async def run_async_task():
async_result = await crew_instance.kickoff_async(inputs=inputs)
print(async_result)
asyncio.run(run_async_task())
```

- Example of using kickoff_for_each_async
- AS I MENTIONED ABOVE
- MAKE SURE TO HANDLE THE ASYNC RESULT PROPERLY

```python
inputs_array = [{'topic': 'AI EFFECT ON EDUCATION'}, {'topic': 'AI in finance'}]
async def run_for_each_task():
     async_results = await crew_instance.kickoff_for_each_async(inputs=inputs_array)
     for async_result in async_results:
         print(async_result)

asyncio.run(run_for_each_task())
```

## **Replaying from a Specific Task Using the CLI**

To use the replay feature, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your CrewAI project is located.
3. Run the following command:
4. To view the latest kickoff task IDs, use:

```Terminal
crewai log-tasks-outputs
```

5. To replay a specific task, use:

```Terminal
crewai replay -t <task_id>
```

# **Conclusion on Crews Core Concept in CrewAI**

The core concept of crews in CrewAI revolves around the collaboration of specialized agents and structured tasks to achieve specific goals. Crews enable efficient workflow management by combining diverse expertise, assigning tasks strategically, and following a defined process flow. This approach ensures seamless execution of creative and operational objectives, making it a powerful framework for complex projects and campaigns.

- ## **Related Resources**

- [Crew AI Documentation](https://crew-ai-docs.com)
- [Crew AI GitHub Repository](https://github.com/crew-ai)

## **Summary of the Code**

1. **Imports Modules**: The code imports necessary libraries (`crewai` for agents and tasks, `dotenv` for environment variables, and `os` and `asyncio` for system interactions).

2. **Loads Environment Variables**: It loads sensitive information like API keys from a `.env` file using `load_dotenv()`.

3. **Defines `CreativeContentCrew` Class**: This class contains methods to create agents (content creator and campaign planner) and tasks that they will execute.

4. **Creates Crew**: In the `crew` method, it initializes a `Crew` instance with the defined agents and tasks, specifying a sequential processing flow.

5. **Starts Execution**: The `kickoff()` method is called on the crew instance to execute the tasks, and the result of the execution is printed.
