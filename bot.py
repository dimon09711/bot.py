import telebot
import requests

bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot('5910129143:AAFvbmkFe1n42pI3E7hzQlA1UEXSqOIAg9Q')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт!')


@bot.message_handler(commands=['search'])
def search_p2p(message):
    query = message.text[8:]
    response = requests.get('https://api.p2pplatform.com/search', params={'query': query})
    if response.status_code == 200:
        results = response.json()
        bot.send_message(message.chat.id, 'Результати пошуку:\n{}'.format(results))
    else:
        bot.send_message(message.chat.id, 'Помилка при виконанні пошуку')


# Запуск бота
bot.polling()
