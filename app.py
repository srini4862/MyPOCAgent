from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

from tools.sharepoint_tools import get_sharepoint_sites_count


model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

agent = create_deep_agent(
    model=model,
    tools=[
        get_sharepoint_sites_count
    ],
    system_prompt="""
You are a SharePoint Discovery Agent.

Responsibilities:
- Discover SharePoint Online resources
- Use tools when needed
- Return concise enterprise-friendly responses
"""
)


response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Get SharePoint sites count"
            }
        ]
    }
)

print("\n=== FINAL RESPONSE ===\n")

print(response["messages"][-1].content)
