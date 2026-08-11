import unittest
from services import Orchestrator
from packages.core.types import AgentRegistration, TaskAssignment, DecisionMaking

import logging

logging.basicConfig(level=logging.INFO)

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_register_agent_assign_task_make_decision_execute_decision(self):
        agent_registration = AgentRegistration(agent_id='agent1', capabilities=['capability1', 'capability2'])
        self.orchestrator.register_agent(agent_registration)

        task_assignment = TaskAssignment(task_id='task1', agent_id='agent1', requirements=['requirement1', 'requirement2'])
        self.orchestrator.assign_task(task_assignment)

        decision = self.orchestrator.make_decision('agent1', 'task1')
        self.assertIsInstance(decision, DecisionMaking)

        self.orchestrator.execute_decision(decision)

if __name__ == '__main__':
    unittest.main()