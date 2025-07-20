from langchain.chat_models import init_chat_model

# Mapping provider to their expected API key parameter name in LangChain
API_KEY_PARAM_MAP = {
    "openai": "openai_api_key",
    "cohere": "cohere_api_key",
    "anthropic": "anthropic_api_key",
    "google": "google_api_key",
    "azure": "azure_api_key",
    # add more providers as needed
}

def test_llm_connection(provider: str, model_name: str, api_key: str) -> bool:
    try:
        provider_lower = provider.lower()
        api_key_param = API_KEY_PARAM_MAP.get(provider_lower, "api_key")  # fallback to generic 'api_key'

        # Compose model kwargs with API key param and model
        model_kwargs = {
            api_key_param: api_key,
            "model": model_name,
        }

        llm = init_chat_model(**model_kwargs)
        llm.invoke("Hello")  # simple test call
        return True

    except Exception as e:
        print(f"LLM connection test failed for provider '{provider}' and model '{model_name}': {e}")
        return False
