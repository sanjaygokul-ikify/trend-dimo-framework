import argparse
from services import Orchestrator

parser = argparse.ArgumentParser(description='Distributed Multi-Agent Orchestration Framework')

parser.add_argument('--register-agent', help='Register an agent')
parser.add_argument('--assign-task', help='Assign a task')
parser.add_argument('--make-decision', help='Make a decision')
parser.add_argument('--execute-decision', help='Execute a decision')

args = parser.parse_args()

orchestrator = Orchestrator()

if args.register_agent:
    # Register an agent
    agent_id = args.register_agent
    orchestrator.register_agent(AgentRegistration(agent_id=agent_id, capabilities=['capability1', 'capability2']))
    print(f'Agent {agent_id} registered successfully')

elif args.assign_task:
    # Assign a task
    task_id = args.assign_task
    orchestrator.assign_task(TaskAssignment(task_id=task_id, agent_id='agent1', requirements=['requirement1', 'requirement2']))
    print(f'Task {task_id} assigned successfully')

elif args.make_decision:
    # Make a decision
    agent_id, task_id = args.make_decision.split(',')
    decision = orchestrator.make_decision(agent_id, task_id)
    print(f'Decision made: {decision.action} for agent {decision.agent_id} and task {decision.task_id}')

elif args.execute_decision:
    # Execute a decision
    decision = DecisionMaking(agent_id='agent1', task_id='task1', action='accept')
    orchestrator.execute_decision(decision)
    print(f'Decision executed: {decision.action} for agent {decision.agent_id} and task {decision.task_id}')
