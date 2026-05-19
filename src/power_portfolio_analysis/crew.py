from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Crewai:
    """Power Generation Portfolio Analysis Crew."""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def renewable_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["renewable_analyst"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def thermal_economist(self) -> Agent:
        return Agent(
            config=self.agents_config["thermal_economist"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def portfolio_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["portfolio_strategist"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def renewable_forecast_task(self) -> Task:
        return Task(
            config=self.tasks_config["renewable_forecast_task"],  # type: ignore[index]
        )

    @task
    def thermal_cost_task(self) -> Task:
        return Task(
            config=self.tasks_config["thermal_cost_task"],  # type: ignore[index]
        )

    @task
    def portfolio_decision_task(self) -> Task:
        return Task(
            config=self.tasks_config["portfolio_decision_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Power Generation Portfolio Analysis Crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
