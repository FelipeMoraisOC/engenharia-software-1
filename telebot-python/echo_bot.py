import telebot

API_TOKEN = '7977106815:AAEH-t39ExQMgQ62HOoP85hdpg1etLx8aao'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_hi(message):
  print(str(message))
  if message.text == 'eae vacilao':
    bot.reply_to(message, "Que foi truta, ta me tirano?")
  elif message.text == 'eae men':
    bot.reply_to(message, "eae meu parceiro")
  else:
    bot.reply_to(message, "ta ligado que vacilão morre cedo")
    
  
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.reply_to(message, "que comando oq mano?")

bot.infinity_polling()