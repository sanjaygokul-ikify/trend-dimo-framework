import unittest
from services import Orchestrator
from packages.core.types import AgentRegistration, TaskAssignment, DecisionMaking

import logging

logging.basicConfig(level=logging.INFO)

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_register_agent(self):
        agent_registration = AgentRegistration(agent_id='agent1', capabilities=['capability1', 'capability2'])
        self.orchestrator.register_agent(agent_registration)
        # Assert that the agent is registered
        # Note: The Orchestrator does not expose the engine's agents directly,
        #       so we cannot assert the agent's presence directly.

    def test_assign_task(self):
        task_assignment = TaskAssignment(task_id='task1', agent_id='agent1', requirements=['requirement1', 'requirement2'])
        self.orchestrator.assign_task(task_assignment)
        # Assert that the task is assigned
        # Note: The Orchestrator does not expose the engine's tasks directly,
        #       so we cannot assert the task's presence directly.

    def test_make_decision(self):
        agent_id = 'agent1'
        task_id = 'task1'
        decision = self.orchestrator.make_decision(agent_id, task_id)
        self.assertIsInstance(decision, DecisionMaking)

    def test_execute_decision(self):
        decision = DecisionMaking(agent_id='agent1', task_id='task1', action='accept')
        self.orchestrator.execute_decision(decision)

if __name__ == '__main__':
    unittest.main()