import logging
from typing import List, Dict
from .types import AgentRegistration, TaskAssignment, DecisionMaking
from .exceptions import DIMOException, EngineError

logger = logging.getLogger(__name__)

class AutonomousReasoningEngine:
    def __init__(self):
        self.agents = {}
        self.tasks = {}

    def register_agent(self, agent_registration: AgentRegistration) -> None:
        logger.info(f'Registering agent: {agent_registration.agent_id}')
        self.agents[agent_registration.agent_id] = agent_registration

    def assign_task(self, task_assignment: TaskAssignment) -> None:
        logger.info(f'Assigning task: {task_assignment.task_id} to agent: {task_assignment.agent_id}')
        self.tasks[task_assignment.task_id] = task_assignment

    def make_decision(self, agent_id: str, task_id: str) -> DecisionMaking:
        logger.info(f'Making decision for agent: {agent_id} and task: {task_id}')
        # Here we use a simple decision-making algorithm based on the agent's capabilities and the task's requirements
        agent_capabilities = self.agents[agent_id].capabilities
        task_requirements = self.tasks[task_id].requirements
        decision = DecisionMaking(
            agent_id=agent_id,
            task_id=task_id,
            action='accept' if all(requirement in agent_capabilities for requirement in task_requirements) else 'reject'
        )
        return decision

    def execute_decision(self, decision: DecisionMaking) -> None:
        logger.info(f'Executing decision: {decision.action} for agent: {decision.agent_id} and task: {decision.task_id}')
        # Here we execute the decision based on the action
        if decision.action == 'accept':
            # Execute the task
            logger.info(f'Executing task: {decision.task_id} on agent: {decision.agent_id}')
        elif decision.action == 'reject':
            # Reject the task
            logger.info(f'Rejecting task: {decision.task_id} for agent: {decision.agent_id}')

    def handle_error(self, error: EngineError) -> None:
        logger.error(f'Error occurred: {error.message}')
        # Here we handle the error based on its type
        if isinstance(error, DIMOException):
            # Handle DIMOException
            logger.error(f'HANDLING DIMOException: {error.message}')
        else:
            # Handle other exceptions
            logger.error(f'HANDLING OTHER EXCEPTION: {error.message}')
            raise error
