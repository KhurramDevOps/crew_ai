#  Flows in crew ai

# What is flow in crewai?
# Flow in crewai is a concept that represents the movement of information, resources, or tasks within a
# system or organization. It is a way to visualize and manage the flow of work, resources, or
# information across different teams, departments, or systems.

# lets see An EXAMPLE OF FLOW

from crewai.flow.flow import Flow, listen, start 
from litellm import completion 
from dotenv import load_dotenv
import uuid
import os


load_dotenv()
class AnimalFunFact_CRew(Flow):
    model = "cohere/command-r"
    

    @start()
    def generate_animal(self):
        print("Starting Animal Fun Fact Flow")
        # Initialize the flow state with a unique ID
        self.state['id'] = str(uuid.uuid4())
        print(f"Flow State ID: {self.state['id']}")

        # Generate a random animal name
        response = completion(
            model=self.model,
            messages=[
                {"role": "user", 
                 "content": "Return the name of random animal in the world"},

            ],
        )

        random_animal = response["choices"][0]["message"]["content"]
        # store the animal name in the flow state
        self.state["animal"] = random_animal
        print(f"Random Animal: {random_animal}")

        return random_animal
    
    @listen(generate_animal)
    def generate_fun_fact(self, random_animal):
        #  Generate a fun fact about the random animal
        response = completion(
            model=self.model,
            messages=[
                {"role": "user",
                 "content": f"Tell me  a fun fact about {random_animal}"},
            ],
            )
        fun_fact = response["choices"][0]["message"]["content"]
        # As i mentioned above store the fun fact in the flow state
        self.state["fun_fact"] = fun_fact
        print(f"Fun Fact about {random_animal}: {fun_fact}")
        
        return fun_fact
    
#  Create and run teh flow
flow = AnimalFunFact_CRew()
result =flow.kickoff()

print(f"Generated fun fact: {result}")


# Assuming you have a flow instance
flow.plot("my_flow_plot")

