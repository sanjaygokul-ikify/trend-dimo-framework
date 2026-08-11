from dataclasses import dataclass
from typing import List

@dataclass
class AgentRegistration:
    agent_id: str
    capabilities: List[str]

@dataclass
class TaskAssignment:
    task_id: str
    agent_id: str
    requirements: List[str]

@dataclass
class DecisionMaking:
    agent_id: str
    task_id: str
    action: str
