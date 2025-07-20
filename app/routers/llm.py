from fastapi import APIRouter
from app.schemas.llm import LLMConfigRequest, LLMTestConnectionResponse
from app.services.llm_service import test_llm_connection
from app.store.session_store import valid_configs

router = APIRouter()

@router.post("/test-connection", response_model=LLMTestConnectionResponse)
async def test_connection(req: LLMConfigRequest):
    is_valid = test_llm_connection(req.provider, req.model_name, req.api_key)
    if is_valid:
        valid_configs["session"] = {
            "provider": req.provider,
            "model_name": req.model_name,
            "api_key": req.api_key,
        }
        return LLMTestConnectionResponse(success=True, detail="Connection successful")
    else:
        return LLMTestConnectionResponse(success=False, detail="Connection failed. Check credentials or model.")
