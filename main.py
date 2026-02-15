import telebot
import config
import leonardo

bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(content_types=['text'])
def processing_message(message):
    text = message.text
    img = leonardo.generate_image(text)
    bot.send_message(message.chat.id, img)

bot.infinity_polling()