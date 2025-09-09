from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List


@CrewBase
class FinancialResearcher:
    """FinancialResearcher crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"], verbose=True, tools=[SerperDevTool()])  # type: ignore

    @agent
    def analyst(self) -> Agent:
        return Agent(config=self.agents_config["analyst"], verbose=True)  # type: ignore

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])  # type: ignore

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config["analysis_task"])  # type: ignore

    @crew
    def crew(self) -> Crew:
        """Creates the FinancialResearcher crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
