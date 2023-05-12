import telebot
import requests

bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт!')


@bot.message_handler(commands=['search'])
def search_p2p(message):
    query = message.text[8:]
    response = requests.get('https://github.com/dimon09711/bot.py/raw/master/bot.py', params={'query': query})
    if response.status_code == 200:
        results = response.json()
        bot.send_message(message.chat.id, 'Результати пошуку:\n{}'.format(results))
    else:
        bot.send_message(message.chat.id, 'Помилка при виконанні пошуку')


# Запуск бота
bot.polling()