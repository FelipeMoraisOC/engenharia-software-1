import smolagents
from smolagents import LiteLLMModel, CodeAgent
# Makesure you already have OPENAI_API_KEY in your environment
# llm_model = LiteLLMModel(model_id="ollama_chat/gemma4:e2b", api_key="ollama")
#teste remoto
llm_model = LiteLLMModel(model_id="ollama_chat/qwen3.5:9b", api_key="ollama")

caminho_arquivo_csv = "data/delivery_food_mock.csv"

query = 'Send me a graph of quantity of payment_method used over time. '

system_prompt = f"""
## Instructions
You are acting as a expert data analyst.
Given a pandas DataFrame.

## Analytics Steps
1. Load the provided CSV file {caminho_arquivo_csv} into a pandas DataFrame.
2. Perform exploratory data analysis (EDA) on the DataFrame.
3. Generate visualizations to summarize the data.
4. Provide a summary of the findings.

## Data information
# [Provide column names, data types (numerical/categorical), and brief descriptions here]

## User Question:
{query}
"""

agent = CodeAgent(
    tools=[],  # Empty list since we'll use built-in tools only
    model=llm_model,  # Connect to our GPT-4 Mini model
    add_base_tools=True,  # Enable standard Python execution capabilities
    additional_authorized_imports=[  # SECURITY: Strictly limit allowed libraries
        "pandas", "numpy", "datetime",
        "matplotlib", "plotly", "seaborn", "sklearn", "matplotlib.pyplot"
    ]
)
agent.run(system_prompt)
