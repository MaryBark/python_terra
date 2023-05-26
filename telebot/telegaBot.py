# создадим бота, который на команду старт пишет "Привет, чем я могу тебе помочь?"
import telebot

bot = telebot.TeleBot('5853388630:AAFu9QtF0JOx2ip-k0uVLh16GVp3bzWSNs0')

@bot.message_handler(commands=['start'])
def send_start_text(message):
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

bot.polling(none_stop=True, interval=0)