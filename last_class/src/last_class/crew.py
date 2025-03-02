from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import  RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import  LTMSQLiteStorage

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

gemini_llm =LLM(
	model="MODEL",
	api_key="GEMINI_API_KEY",

)

@CrewBase
class LastClass():
	"""LastClass crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=gemini_llm
		)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True,
	# 		llm=gemini_llm
	# 	)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
		# )

	@crew
	def crew(self) -> Crew:
		"""Creates the LastClass crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=True,
			embedder={
				"provider": "google",
				"config": {
					"model": 'models/text-embedding-004',
					"api_key":"GEMINI_API_KEY",
				}
			},

			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/

			# Short-term memory for current context using RAG
		short_term_memory = ShortTermMemory(
			storage = RAGStorage(
					embedder_config={
						"provider": "google",
						"config": {
							"model": 'models/text-embedding-004',
							"api_key":"GEMINI_API_KEY",
						}
					},
					type="short_term",
					path="/memory/short_term",
				)
			),
		),
        
		# long_term_memory = LongTermMemory(
		# 	storage = LTMSQLiteStorage(
		# 		path="./memory/long_term/long_term_memory_storage.db",
		# 	)
		# ),
