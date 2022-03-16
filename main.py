import telebot
import config
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])  # Запускаем бот
def welcome_start(message):
    bot.send_message(message.chat.id, 'Приветствую! Если вы хотите узнать курс покупки(вами) нажмите /buy, \n '
                                      'если вы хотите узнать курс продажи(вами) нажмите /sell \n'
                                      'Узнать сколько валюты вы можете купить на ваши рубли /change')

@bot.message_handler(commands=['sell', 'buy', 'change'])  # Выводим список команд
def kurs(message):
    url = 'https://bankdabrabyt.by/currency_exchange/'
    print(message.text)
    if message.text == '/buy':
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        table = soup.find('table', {'class': 'courses-table'})
        tr = table.find_all('td')
        USD_kurs = tr[4].text
        EUR_kurs = tr[9].text
        print(USD_kurs)
        print(EUR_kurs)
        bot.send_message(message.chat.id, 'Курс покупки доллара = ' + str(USD_kurs) + '\n' + 'Курс покупки евро = ' + str(EUR_kurs))
    elif message.text == '/sell':
        source = requests.get(url)
        soup = BeautifulSoup(source.text)
        table = soup.find('table', {'class': 'courses-table'})
        tr = table.find_all('td')
        USD_kurs = tr[3].text
        EUR_kurs = tr[8].text
        bot.send_message(message.chat.id, 'Курс продажи доллара = ' + str(USD_kurs) + '\n' + 'Курс продажи евро = ' + str(EUR_kurs))
    elif message.text == '/change':
        bot.send_message(message.chat.id, 'Введите сумму в рублях')

        @bot.message_handler(content_types=['text'])
        def change(message):
            source = requests.get(url)
            soup = BeautifulSoup(source.text, 'lxml')
            table = soup.find('table', {'class': 'courses-table'})
            tr = table.find_all('td')
            USD_kurs = tr[4].text
            EUR_kurs = tr[9].text
            print(USD_kurs)
            print(EUR_kurs)
            USD_summa = int(message.text)/float(USD_kurs)
            EUR_summa = int(message.text)/float(EUR_kurs)
            bot.send_message(message.chat.id,
                             'Сумма в долларах = ' + str(USD_summa) + '\n' + 'Сумма в евро = ' + str(EUR_summa))


bot.polling()  # запускаем бота