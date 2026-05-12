from pathlib import Path
import importlib.util
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Dynamically load tool module
tool_path = (
    Path(__file__).parent
    / "skills"
    / "sharepoint-discovery"
    / "tools"
    / "sharepoint_tools.py"
)

spec = importlib.util.spec_from_file_location(
    "sharepoint_tools",
    tool_path
)

if spec is None or spec.loader is None:
    raise ImportError(
        f"Could not load module from {tool_path}"
    )

module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

get_sharepoint_sitecount = module.get_sharepoint_sitecount
get_sharepoint_sites_size = module.get_sharepoint_sites_size

memory_saver = MemorySaver()

agent = create_deep_agent(
    model=model,
    tools=[get_sharepoint_sitecount, get_sharepoint_sites_size],
    skills=["./skills"],
    checkpointer=memory_saver
)

# The thread_id allows the agent to remember your tenant/client_id
config: RunnableConfig = {
    "configurable": {"thread_id": "sharepoint-discovery-session"}
}


print("Agent: Hello! I'm your SharePoint Discovery Assistant. How can I help you?")

while True:
    try:
        user_input = input("Human: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye!")
            break

        # Send message as a list of dictionaries to satisfy the State requirements
        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config
        )

        # The response is the content of the last message in the state
        print(f"Agent: {response['messages'][-1].content}")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")
