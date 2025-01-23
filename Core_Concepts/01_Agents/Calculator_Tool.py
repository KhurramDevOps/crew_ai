from crewai.tools import tool

# Define a calculation tool using the @tool decorator
@tool
def calculate(expression: str) -> str:
    """
    A simple calculator tool to evaluate basic mathematical expressions.
    
    Args:
        expression (str): A string representing a mathematical expression, e.g., "3 + 5 * (2 - 1)".

    Returns:
        str: The result of the evaluated expression or an error message if the input is invalid.
    """
    try:
        # Use eval to calculate the result of the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return f"The result of '{expression}' is: {result}"
    except Exception as e:
        return f"Error evaluating expression '{expression}': {str(e)}"