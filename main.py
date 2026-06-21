import asyncio
from agents import SqlAgent, DocumentAgent

async def main():
    sql_worker = SqlAgent(agent_id="sql-agent-01")
    doc_worker = DocumentAgent(agent_id="doc-agent-01")
    agent_registry = {"crypto" : sql_worker, 
                      "sales" : doc_worker}
    #prompt = " what is the value of crypto"
    prompt = "show me the sales figures"
    chose_agent = None
    for keyword, agent in agent_registry.items():
        if keyword in prompt.lower():
            chose_agent = agent
            break
    if chose_agent:
        response = await chose_agent.process_query(prompt=prompt, tenant_id="tenant-123")
        print(response)
    else:
        print("No agent found")

if __name__ == "__main__" :
    asyncio.run(main())