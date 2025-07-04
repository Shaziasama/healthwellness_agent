from openai import AsyncOpenAI
from agents import Runner
from context import ContextManager

class StreamingChat:
    def __init__(self, config):
        self.config = config
        self.client = AsyncOpenAI(api_key=config["api_key"])
        self.context_manager = ContextManager()

    async def chat(self, agent, user_input):
        """Stream the agent's response in real-time"""
        context = self.context_manager.get_context()
        async for step in Runner.stream(
            starting_agent=agent,
            input=user_input,
            context=context
        ):
            print(step.pretty_output)

