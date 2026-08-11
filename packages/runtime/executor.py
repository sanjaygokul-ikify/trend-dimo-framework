import logging
from typing import List
from ..core.engine import AutonomousReasoningEngine
from ..core.exceptions import DIMOException, EngineError, TimeoutError

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, timeout_duration: int = 60):
        self.engine = AutonomousReasoningEngine()
        self.timeout_duration = timeout_duration

    def execute(self, agent_registrations: List[AgentRegistration], task_assignments: List[TaskAssignment]) -> None:
        logger.info('Executing autonomous reasoning engine')
        for agent_registration in agent_registrations:
            self.engine.register_agent(agent_registration)
        for task_assignment in task_assignments:
            self.engine.assign_task(task_assignment)
            decision = self.engine.make_decision(task_assignment.agent_id, task_assignment.task_id)
            try:
                self.engine.execute_decision(decision)
            except TimeoutError as e:
                logger.error(f'Timeout occurred during decision execution: {e}')
                raise EngineError(f'Timeout occurred during decision execution: {e}')

    def handle_error(self, error: DIMOException) -> None:
        logger.error(f'Error occurred: {error}')
        # Here we handle the error based on its type
        if isinstance(error, DIMOException):
            # Handle DIMOException
            logger.error(f'HANDLING DIMOException: {error}')
        elif isinstance(error, TimeoutError):
            logger.error(f'HANDLING TimeoutError: {error}')
            raise EngineError(f'Timeout occurred during decision execution: {error}')
        else:
            # Handle other exceptions
            logger.error(f'HANDLING OTHER EXCEPTION: {error}')
            raise error
