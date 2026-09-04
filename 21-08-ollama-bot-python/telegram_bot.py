import telebot
from ai_agent import processar_pergunta
from ai_agent_dspy import processar_pergunta_dspy

API_TOKEN = '7977106815:AAEH-t39ExQMgQ62HOoP85hdpg1etLx8aao'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg_status = bot.reply_to(message, "⏳ Iniciando agente...")
    def atualizar_mensagem_telegram(texto_passo):
        try:
            bot.edit_message_text(
                chat_id=message.chat.id, 
                message_id=msg_status.message_id, 
                text=texto_passo
            )
        except Exception:
            print("Error")
            # O Telegram dá erro se você tentar editar a mensagem com um texto idêntico ao que já está lá.
            # Esse except ignora esse erro silenciosamente.
            pass
        # 3. Mandamos a pergunta para a IA trabalhar
    try:
        # Passamos a pergunta e a nossa função de edição
        resposta_da_ia = processar_pergunta_dspy(message.text)
        
        # 4. Quando a IA terminar, editamos a mensagem pela última vez com a resposta final
        bot.edit_message_text(
            chat_id=message.chat.id, 
            message_id=msg_status.message_id, 
            text=f"🤖 Resposta:\n\n{resposta_da_ia}"
        )
    except Exception as e:
        # Se der erro no Ollama (ex: falta de memória), avisamos o usuário
        bot.edit_message_text(
            chat_id=message.chat.id, 
            message_id=msg_status.message_id, 
            text=f"❌ Oops, meu cérebro local deu curto-circuito:\n{str(e)}"
        )

print("Bot está online e ouvindo...")
bot.infinity_polling()