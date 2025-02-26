from crewai.flow.flow import Flow, start, listen

from multiple_agents.crews.devcrew.dev_crew import Devcrew




class DevFlow(Flow):

    @start()
    def run_dev_crew(self):
        output = Devcrew().crew().kickoff(
            inputs={
                "problem":"write python code for addition two number"
            }
        )
        # Store the output in the flow's state
        self.state['result'] = output.raw
        print(f"Dev Crew Result: {self.state['result']}")
    


def kickoff():
    dev = DevFlow()
    dev.kickoff()


if __name__ == "__main__":
    try:
        kickoff()
    except Exception as e:
        print(f"An error occurred: {str(e)}")