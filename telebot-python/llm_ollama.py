from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
 
model = LiteLLMModel(model_id="ollama_chat/gemma4:e2b", api_key="ollama")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
 
agent.run('Hello!')