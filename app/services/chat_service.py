# app/services/chat_service.py
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from app.store.session_store import valid_configs

def chat_with_llm(conversation_id: str, user_message: str) -> str:
    # Retrieve saved config for the session
    config = valid_configs.get("session")
    if not config:
        raise ValueError("No valid LLM configuration found for session")

    provider = config["provider"]
    model_name = config["model_name"]
    api_key = config["api_key"]

    # Build config dict per provider (same as test service)
    if provider.lower() == "openai":
        llm_config = {
            "openai_api_key": api_key,
            "model": model_name,
        }
    elif provider.lower() == "huggingface":
        llm_config = {
            "huggingface_api_token": api_key,
            "model": model_name,
        }
    else:
        llm_config = {
            "api_key": api_key,
            "model": model_name,
        }

    llm = init_chat_model({
        "provider": provider,
        "config": llm_config,
    })

    # Create a HumanMessage and invoke LLM
    human_message = HumanMessage(text=user_message)
    response = llm.invoke(human_message)
    return response.content
