<h1><strong>AGENTS IN </strong> <img src="https://i.postimg.cc/G3xn0D6W/crew-only-logo.png](https://postimg.cc/F1zB3Yrp)" style="width: 25%;" alt="Crew AI Logo"></h1>

## **Overview**

An Agent in Crew AI represents an intelligent entity that can:

- Perform specific tasks
- Make decisions based on its role and goal
- Use tools to accomplish objectives
- Communicate and collaborate with other agents
- Maintain memory of interactions
- Delegate tasks when allowed

Agents are integral parts of the Crew AI system and interact with tasks, tools, and other agents to achieve goals. In this section, we will explore the key attributes of agents, their role in Crew AI, and how to build an agent using Crew AI.

---

## **Key Attributes of an Agent in Crew AI**

An Agent in Crew AI has multiple attributes that define its behavior and role in the system.

### **Main Attributes:**

- **role**: The role of the agent, describing its function and responsibility.
- **goal**: The agent’s mission or objective.
- **backstory**: The context and history that defines the agent's personality and approach.

![Agent in Crew AI](https://i.postimg.cc/WbDk9ZxB/Screenshot-2025-01-20-at-00-38-18.png)

---

->

### **Agent Role**

Each agent has a role that defines its purpose in the Crew AI system. For example, in the case of a math-solving agent:

- **Role**: Math Magician
- **Goal**: To evaluate and solve any mathematical expression.

This helps establish the agent's function within the system.

---

## **Code Example: Simple Agent for Math Problem Solving**

Here’s an example of creating a Math Agent that can evaluate mathematical expressions using a tool.

```python
from crewai import Agent
from Calculator_Tool import calculate  # Assuming this is your custom tool

# Define the math agent
math_agent = Agent(
    role="MATH Magician",
    goal="You are able to evaluate any math expression",
    backstory="YOU ARE A MATH WHIZ",
    verbose=True,  # Print out the agent's thoughts and actions
    tools=[calculate],  # Tools that the agent can use (e.g., calculate tool)
    memory=True  # Use memory to remember previous interactions
)


```

## **Agent Tool**

An agent in Crew AI can use tools to achieve its goal. A tool is a function or external resource that the agent can utilize to perform a specific task. In the math agent example, `calculate` is a tool that helps the agent evaluate math expressions.

### **The Role of Tools:**

- **Perform specific tasks**: Tools enable the agent to carry out its objectives (e.g., solving math problems).
- **Decision making**: Tools help agents make informed decisions.
- **Collaboration**: Agents can communicate with each other and use tools to share knowledge.
- **Memory management**: Some tools enable agents to store or recall information from past interactions.

---

## **Advanced Attributes of an Agent**

In addition to the core attributes (role, goal, backstory), Crew AI agents support several optional attributes for fine-tuning and advanced functionality. Here's an overview of some of the advanced attributes:

- **llm**: Specifies the language model used by the agent (e.g., `"gpt-4"`). Default: `OPENAI_MODEL_NAME` or `"gpt-4"`.
- **function_calling_llm**: Optional attribute for using a separate LLM for tool calling.
- **allow_delegation**: Allows the agent to delegate tasks to other agents. Default: `False`.
- **max_iter**: Specifies the maximum number of iterations the agent will run. Default: `20`.
- **max_rpm**: Optional attribute for rate limiting API calls.
- **max_execution_time**: Optional attribute for setting a maximum execution time in seconds.
- **max_retry_limit**: Specifies the number of retries on error. Default: `2`.
- **allow_code_execution**: Allows the agent to execute code. Default: `False`.
- **code_execution_mode**: Defines the mode for code execution. Default: `"safe"` (options: `"safe"`, `"unsafe"`).
- **respect_context_window**: Whether the agent should respect the context window of its conversations. Default: `True`.
- **use_system_prompt**: Whether to use a system prompt template. Default: `True`.
- **knowledge_sources**: Optional list of knowledge sources that the agent can refer to.
- **embedder_config**: Optional custom configuration for embedding.
- **system_template**: Optional custom system prompt template.
- **prompt_template**: Optional custom prompt template.
- **response_template**: Optional custom response template.
- **step_callback**: Optional callback function for monitoring agent progress.

## **Example of an Advanced Agent**

```python
from crewai import Agent

advanced_agent = Agent(
    llm="gpt-4",  # The language model used for interactions (default: "gpt-4")
    function_calling_llm=None,  # Optional: Separate LLM for tool calling
    allow_delegation=False,  # Optional: Whether to delegate tasks to other agents
    max_iter=20,  # Maximum iterations the agent will run
    max_rpm=None,  # Rate limit for API calls
    max_execution_time=None,  # Maximum time the agent can run
    max_retry_limit=2,  # Retry on error
    allow_code_execution=False,  # Allow or disallow code execution
    code_execution_mode="safe",  # Code execution mode (safe or unsafe)
    respect_context_window=True,  # Respect the context window of conversation
    use_system_prompt=True,  # Use system-defined prompts
    knowledge_sources=None,  # Custom knowledge sources
    embedder_config=None,  # Custom embedder configuration
    system_template=None,  # Custom system prompt template
    prompt_template=None,  # Custom prompt template
    response_template=None,  # Custom response template
    step_callback=None,  # Optional callback function for monitoring
)
```

This example demonstrates how to create an advanced agent with specific attributes. Note that some attributes have default values.

## **Tool Code Example: calculate Tool**

The tool `calculate` is used by the agent to evaluate mathematical expressions. Below is the basic structure for the `calculate` tool:

#### **MODIFIED IF YOU WANT TO USE A DIFFERENT TOOL**

```python
# Import necessary modules
import math

# Tool function for evaluating mathematical expressions
def calculate(expression: str) -> str:
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        return f"The result of the expression '{expression}' is: {result}"
    except Exception as e:
        return f"Error evaluating expression '{expression}': {str(e)}"
```

- This function allows the agent to compute math expressions given as strings. It can be expanded with more advanced error handling or functionality as needed.

## **How the Code Works**

The code initiates an agent with the role of a "Math Magician" and equips it with the `calculate` tool. It then takes an input from the user (the math problem) and assigns the task to the agent. The agent then evaluates the math problem and returns the result.

### **Steps:**

1. The agent is created with the `Agent` class.
2. The math problem is provided by the user.
3. The `Task` class is used to define what needs to be done — in this case, evaluating the math expression.
4. The `Crew` class brings together the agent and the task, and then the task is executed using the `crew.kickoff()` method.

```bash
###--- Welcome to the Math Magician ---###

Enter Your math problem: 2 * (3 + 5) / (7 - 5)

Task Description: Solve a complex math expression and validate the result.
--------------------------------------------------
Math Magician Agent is thinking...
Evaluating the expression: 2 * (3 + 5) / (7 - 5)

Result: The result of the expression 2 * (3 + 5) / (7 - 5) is: 8.0
```
