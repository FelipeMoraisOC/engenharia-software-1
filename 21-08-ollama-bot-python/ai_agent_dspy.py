import os
import dspy

dspy.configure(lm=dspy.LM('ollama_chat/gemma4:e2b'))

def suma(a: int, b: int) -> str:
    """Sum a number with another number, A + B = Result"""
    print(f"\n⚙️ [AÇÃO DA IA] Ferramenta 'suma' acionada! Somando: {a} + {b}")
    resultado = a + b
    print(f"✅ [RESULTADO] A ferramenta retornou: {resultado}")
    return f"Sum, {resultado}."

def sub(a: int, b: int) -> str:
    """Subtraction of two number, A - B = Result"""
    print(f"\n⚙️ [AÇÃO DA IA] Ferramenta 'sub' acionada! Subtraindo: {a} - {b}")
    resultado = a - b
    print(f"✅ [RESULTADO] A ferramenta retornou: {resultado}")
    return f"Subtraction {resultado}."

def multiply(a: int, b:int) ->str:
    """Multiply 2 numbers, A * B = Result"""
    print(f"\n⚙️ [AÇÃO DA IA] Ferramenta 'multiply' acionada! Multiplicando: {a} * {b}")
    resultado = a * b
    print(f"✅ [RESULTADO] A ferramenta retornou: {resultado}")
    return f"Multiply {resultado}."
    


print("🚀 Inicializando o agente ReAct...")
support = dspy.ReAct(
    "question->answer",
    tools=[suma, sub, multiply]
)



def processar_pergunta_dspy(pergunta: str) -> str:
    print(f"🧠 Enviando pergunta para a IA: '{pergunta}'")
    print("⏳ Aguardando o raciocínio da IA...\n")
    # Executa o agente
    result = support(question=pergunta)
    print("\n" + "="*50)
    print(f"🎯 RESPOSTA FINAL DA IA: {result.answer}")
    print("="*50)
    return result.answer



# Bônus: Mostra o "monólogo interno" completo da IA
print("\n🔍 INSPECIONANDO O PENSAMENTO COMPLETO (Prompt e Geração):")
dspy.inspect_history(n=1)