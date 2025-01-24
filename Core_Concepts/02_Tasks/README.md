<h1><strong>TASKS IN </strong> <img src="https://i.postimg.cc/G3xn0D6W/crew-only-logo.png](https://postimg.cc/F1zB3Yrp)" style="width: 25%;" alt="Crew AI Logo"></h1>

# **Overview**

In Crew AI, a **Task** represents a unit of work or an objective that needs to be achieved. Tasks are essential for agents to perform specific actions or operations that contribute to the overall goal of the system. Tasks are assigned to agents, and agents use their skills and tools to execute them.

`"Tasks"` can vary in complexity, ranging from simple requests (such as evaluating a math expression) to more complex processes that involve multiple steps or collaboration between several agents. The Task class helps define the work and its expected output, which agents use to guide their behavior.

Tasks in Crew AI enable the delegation of work, ensure that the right agents are handling specific jobs, and track progress toward achieving broader goals.

---

->

## **Task Execution Flow**

Tasks can be executed in two ways:

1. **Sequential**: Tasks are executed in the order they are defined.
2. **Hierarchical**: Tasks are assigned to agents based on their roles and expertise.

```python
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential  # or Process.hierarchical
)
```

# **Task Attributes**

Tasks in Crew AI are defined by several key attributes that describe their purpose and execution.

## **Main Attributes**:

- **description**: A string that describes the task and what needs to be done.
- **expected_output**: A string that specifies the expected outcome from executing the task.
- **agent**: The agent responsible for executing the task.

## **Additional Attributes**:

- **tools**: Optional tools that the agent can use to complete the task.
- **verbose**: A boolean flag to control whether detailed logs of the task's execution are displayed.

[![Screenshot-2025-01-20-at-00-38-34.png](https://i.postimg.cc/8zJmr91r/Screenshot-2025-01-20-at-00-38-34.png)](https://postimg.cc/7542FBJx)

## **Code Example: Research and Reporting Tasks**

Below is an example demonstrating how to define tasks for a **Researcher Agent** and a **Reporting Analyst Agent**. The `research_task` involves gathering information about AI Agents, and the `reporting_task` involves creating a detailed report based on the research findings.

```python
# Define the researcher_Agent
researcher_agent  = Agent(
  role= "{topic} Senior Data Researcher",
  goal="Uncover cutting-edge developments in {topic}",
  backstory= """You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner."""
)

# Define the reporting_analyst_agent
reporting_analyst_agent = Agent(
  role="{topic} Reporting Analyst",
  goal="Create detailed reports based on {topic} data analysis and research findings",
  backstory="""You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.""")

```

---

## **Task Output Attributes**

Understanding task outputs is crucial for building effective AI workflows. Crew AI provides a structured way to handle task results through the **TaskOutput** class, which supports multiple output formats and can be easily passed between tasks.

Here’s how you can access and display task outputs:

```python
# Retrieve task output
task_output = research_task.output

# Print task details
print(f"Task Description : {task_output.description}")
print(f"Task Summary : {task_output.summary}")
print(f"Raw Output : {task_output.raw}") # raw output is the actual output of the task

# Optionally, check if the output is in JSON format
if task_output.json_dict():
    print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
else:
    print("No JSON output available")

# Optionally, check if the output is in Pydantic format
if task_output.Pydantic():
    print(f"Pydantic Output: {task_output.pydantic}")
else:
    print("No Pydantic output available")
```

---

# **Conclusion**

`Tasks` in Crew AI play a crucial role in delegating work to agents, ensuring that tasks are executed systematically and effectively. By combining agents, tasks, and tools, Crew AI allows for the creation of intelligent systems that can handle a wide variety of operations. The flexibility in task definition (sequential or hierarchical execution) and the powerful task output handling (through various formats like raw, JSON, or Pydantic) ensures that Crew AI is highly adaptable for real-world applications.

- ## **Related Resources**

- [Crew AI Documentation](https://crew-ai-docs.com)
- [Crew AI GitHub Repository](https://github.com/crew-ai)

# Explanation

- **Import Libraries**: The required libraries, including Crew AI, dotenv, and json, are imported to manage the task execution and environment variables.
- **Define Agents**: Two agents are created — a researcher and a reporting analyst, each with specific roles and goals.
- **Define Tasks**: Two tasks are defined — one for conducting research and another for reporting the findings.
- **Create Crew**: The tasks are assigned to the agents, and the Crew object is created to manage the execution.
- **Handling Output**: Task outputs are retrieved and printed, with options to display them in raw, JSON, or Pydantic formats.
