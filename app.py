from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import DocumentAgent, SqlAgent


app = FastAPI()

class QueryRequest(BaseModel):
    prompt: str
    tenant_id: str

sql_worker = SqlAgent(agent_id="agent_sql_01")
doc_worker = DocumentAgent(agent_id="agent_document_01")

agent_registry = {
    "sql" : sql_worker,
    "sales" : doc_worker
}

@app.post("/query")
async def post_query(query_request: QueryRequest) -> dict:
    chosen_agent = None
    for key_word, agent in agent_registry.items():
        if key_word in query_request.prompt.lower():
            chosen_agent = agent
            break
    if chosen_agent:
        agent_response = await chosen_agent.process_query(prompt=query_request.prompt, tenant_id=query_request.tenant_id)
        return { "status" : "success" , "response": agent_response }
    
    raise HTTPException(
        status_code=404, 
        detail=f"No specialized data agent could be found to handle the prompt: '{query_request.prompt}'"
    )