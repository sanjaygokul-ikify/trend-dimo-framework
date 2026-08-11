from packages.core.types import AgentRegistration, TaskAssignment, DecisionMaking
from packages.core import AutonomousReasoningEngine

from packages.utils import logging

logger = logging.logger

class Orchestrator:
    def __init__(self):
        self.engine = AutonomousReasoningEngine()

    def register_agent(self, agent_registration: AgentRegistration) -> None:
        logger.info(f'Registering agent: {agent_registration.agent_id}')
        self.engine.register_agent(agent_registration)

    def assign_task(self, task_assignment: TaskAssignment) -> None:
        logger.info(f'Assigning task: {task_assignment.task_id} to agent: {task_assignment.agent_id}')
        self.engine.assign_task(task_assignment)

    def make_decision(self, agent_id: str, task_id: str) -> DecisionMaking:
        logger.info(f'Making decision for agent: {agent_id} and task: {task_id}')
        return self.engine.make_decision(agent_id, task_id)

    def execute_decision(self, decision: DecisionMaking) -> None:
        logger.info(f'Executing decision: {decision.action} for agent: {decision.agent_id} and task: {decision.task_id}')
        self.engine.execute_decision(decision)