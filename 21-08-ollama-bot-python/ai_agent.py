import smolagents
from smolagents import LiteLLMModel, CodeAgent

# Configuração do modelo (deixamos fora da função para carregar apenas uma vez)
llm_model = LiteLLMModel(
    model_id="ollama_chat/gemma4:e2b", 
    api_key="ollama",
    api_base="http://localhost:11434"
)

def processar_pergunta(query, funcao_atualizar_status):
    system_prompt = f"""
    ##Instructions:
    01. You are a bot that respond easy answers from my users in telegram.
    02. You must be simple in your explanations.
    03. Don't overthink any explanation.

    ## User Question:
    {query}
    """

    contador_passos = [0] # Usamos uma lista para poder alterar o valor dentro da função abaixo

    # Esta é a mágica: o smolagents vai chamar essa função a cada passo que ele der
    def notificar_passo(step_log):
        contador_passos[0] += 1
        mensagem_status = f"⚙️ STEP {contador_passos[0]} - Executando código e raciocinando..."
        
        # Chama a função que enviamos do Telegram para atualizar a tela do usuário
        funcao_atualizar_status(mensagem_status)

    agent = CodeAgent(
        tools=[],  
        model=llm_model,  
        add_base_tools=True,  
        additional_authorized_imports=[  
            "pandas", "numpy", "datetime",
            "matplotlib", "plotly", "seaborn", "sklearn", "matplotlib.pyplot"
        ],
        step_callbacks=[notificar_passo] # Conectamos o nosso "espião" aqui!
    )
    
    # Roda o agente e guarda a resposta final
    resposta_final = agent.run(system_prompt)
    return resposta_final