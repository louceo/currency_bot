import telebot
from config import currency, TOKEN
from extensions import ConvertException, Conversion

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    text = 'Чтобы начать конвертировать валюту введите команду боту в формате: \n<количество> <имя валюты> <в какую валюту нужно конвертировать>.\
\nЧтобы узнать список доступных валют введите /currency'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['currency'])
def handle_currency(message):
    text = 'Список валют: '
    for key in currency.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def handle_conversion(message):
    try:
        attr = message.text.split(' ')
        if len(attr) != 3:
            raise ConvertException('Неверное количество параметров')
            
        amount, quote, base = attr 
        result = Conversion.conversion(amount, quote, base)
    except ConvertException as e: 
        bot.send_message(message.chat.id, e)
    except Exception as e: 
        bot.send_message(message.chat.id, e)
    else:
        bot_message = f'{amount} {quote} в {base} = %.2f ' % result
        bot.send_message(message.chat.id, bot_message)

bot.polling(none_stop=True)
