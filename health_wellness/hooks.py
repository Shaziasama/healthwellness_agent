from typing import Dict, Any
from datetime import datetime

class HookManager:
    """Simple hook manager for tracking tool and agent usage"""
    
    def __init__(self):
        self.activity_log = []
        self.metrics = {
            'total_interactions': 0,
            'tool_usage': {},
            'handoffs': {}
        }

    def log_agent_start(self, agent_name: str):
        """Log when an agent starts"""
        self.activity_log.append({
            'timestamp': datetime.now().isoformat(),
            'event': 'agent_start',
            'agent': agent_name
        })
        self.metrics['total_interactions'] += 1
        print(f"🤖 Agent started: {agent_name}")

    def log_tool_start(self, tool_name: str):
        """Log when a tool is triggered"""
        self.activity_log.append({
            'timestamp': datetime.now().isoformat(),
            'event': 'tool_start',
            'tool': tool_name
        })

        if tool_name not in self.metrics['tool_usage']:
            self.metrics['tool_usage'][tool_name] = 0
        self.metrics['tool_usage'][tool_name] += 1
        print(f"🔧 Tool started: {tool_name}")

    def log_handoff(self, from_agent: str, to_agent: str):
        """Log a handoff from one agent to another"""
        self.activity_log.append({
            'timestamp': datetime.now().isoformat(),
            'event': 'handoff',
            'from_agent': from_agent,
            'to_agent': to_agent
        })

        handoff_key = f"{from_agent}_to_{to_agent}"
        if handoff_key not in self.metrics['handoffs']:
            self.metrics['handoffs'][handoff_key] = 0
        self.metrics['handoffs'][handoff_key] += 1
        print(f"🔄 Handoff: {from_agent} → {to_agent}")

    def get_metrics(self) -> Dict[str, Any]:
        """Return all collected metrics"""
        return self.metrics

    def get_activity_log(self) -> list:
        """Return raw activity logs"""
        return self.activity_log



hook_manager = HookManager()

