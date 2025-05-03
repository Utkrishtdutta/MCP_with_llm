from dotenv import load_dotenv
from langchain_groq import Chatgroq

from mcp_use import MCPAgent, MCPClient
import os

async def run_memory_chat():
    load_dotenv()
    os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

    config_file = 'browser_mcp.json'

    print("Intializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm = Chatgroq(model='qwen-qwq-32b')
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_step=15,
        memory_enabled=True
    )

