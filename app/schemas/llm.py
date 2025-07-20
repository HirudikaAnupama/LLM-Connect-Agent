from pydantic import BaseModel

class LLMConfigRequest(BaseModel):
    provider: str
    model_name: str
    api_key: str

class LLMTestConnectionResponse(BaseModel):
    success: bool
    detail: str
