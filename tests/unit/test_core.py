import unittest
from packages.core import AutonomousReasoningEngine
from packages.core.types import AgentRegistration, TaskAssignment, DecisionMaking

import logging

logging.basicConfig(level=logging.INFO)

class TestAutonomousReasoningEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AutonomousReasoningEngine()

    def test_register_agent(self):
        agent_registration = AgentRegistration(agent_id='agent1', capabilities=['capability1', 'capability2'])
        self.engine.register_agent(agent_registration)
        self.assertIn(agent_registration.agent_id, self.engine.agents)

    def test_assign_task(self):
        task_assignment = TaskAssignment(task_id='task1', agent_id='agent1', requirements=['requirement1', 'requirement2'])
        self.engine.assign_task(task_assignment)
        self.assertIn(task_assignment.task_id, self.engine.tasks)

    def test_make_decision(self):
        agent_id = 'agent1'
        task_id = 'task1'
        decision = self.engine.make_decision(agent_id, task_id)
        self.assertIsInstance(decision, DecisionMaking)

    def test_execute_decision(self):
        decision = DecisionMaking(agent_id='agent1', task_id='task1', action='accept')
        self.engine.execute_decision(decision)

if __name__ == '__main__':
    unittest.main()        