from abc import abstractmethod, ABC

class BaseAgent(ABC):
    """
    This is a baseclass for all agents
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    @abstractmethod
    async def process_query(self, prompt: str, tenant_id: str) -> str:
        """
        All agents must implement this using async def
        """
        pass

class SqlAgent(BaseAgent):
    async def process_query(self, prompt, tenant_id) -> dict:
        return { "SQL Agent | Tenant id" : tenant_id ,  "Prompt - " : prompt }

class DocumentAgent(BaseAgent):
    async def process_query(self, prompt, tenant_id) -> dict:
        return {"Document Agent | Tenant id" : tenant_id , "Prompt - " : prompt}
        