# import telebot
# import config
# import requests
# from bs4 import BeautifulSoup
#
#
# # bot = telebot.TeleBot(config.token)
#
# @bot.message_handler(commands=['start'])  # Запускаем бот
# def welcome_start(message):
#     bot.send_message(message.chat.id, 'Приветствую! Если вы хотите узнать курс покупки(вами) нажмите /buy, \n '
#                                       'если вы хотите узнать курс продажи(вами) нажмите /sell \n'
#                                       'Узнать сколько валюты вы можете купить на ваши рубли /change')
#
# @bot.message_handler(commands=['sell', 'buy', 'change'])  # Выводим список команд
# def kurs(message):
#     url = 'https://bankdabrabyt.by/currency_exchange/'
#     print(message.text)
#     if message.text == '/buy':
#         url_Euro = 'https://bankchart.by/servisy/konverter_valyut/1064/1000/0/974/978'
#         url_USD = 'https://bankchart.by/servisy/konverter_valyut/1064/1/0/974/840'
#         source_Euro = requests.get(url_Euro)
#         source_USD = requests.get(url_USD)
#         parced_site = BeautifulSoup(source_Euro.text, 'lxml')
#         table = parced_site.find('div', {'class': 'cc-table'})
#         table_elem = table.find('div', {'data-sort-row-index': '2'})
#         elem_kurs = table_elem.find('div', {'class': 'cc-col cc-col_rate'})
#         elem_kurs_value = elem_kurs.find('p')
#         parced_site_USD = BeautifulSoup(source_USD.text, 'lxml')
#         table_USD = parced_site_USD.find('div', {'class': 'cc-table'})
#         table_elem_USD = table_USD.find('div', {'data-sort-row-index': '2'})
#         elem_kurs_USD = table_elem_USD.find('div', {'class': 'cc-col cc-col_rate'})
#         elem_kurs_value_USD = elem_kurs_USD.find('p')
#         USD_kurs = elem_kurs_value_USD.text
#         EUR_kurs = elem_kurs_value.text
#         print(USD_kurs)
#         print(EUR_kurs)
#         bot.send_message(message.chat.id, f'Курс покупки доллара = {USD_kurs} '
#                                           f'Курс покупки евро = {EUR_kurs}' )
#     elif message.text == '/sell':
#         url_Euro = 'https://bankchart.by/servisy/konverter_valyut/1064/1/0/978/974'
#         url_USD = 'https://bankchart.by/servisy/konverter_valyut/1064/1/0/840/974'
#         source_Euro = requests.get(url_Euro)
#         source_USD = requests.get(url_USD)
#         parced_site = BeautifulSoup(source_Euro.text, 'lxml')
#         table = parced_site.find('div', {'class': 'cc-table'})
#         table_elem = table.find('div', {'data-sort-row-index': '2'})
#         elem_kurs = table_elem.find('div', {'class': 'cc-col cc-col_rate'})
#         elem_kurs_value = elem_kurs.find('p')
#         parced_site_USD = BeautifulSoup(source_USD.text, 'lxml')
#         table_USD = parced_site_USD.find('div', {'class': 'cc-table'})
#         table_elem_USD = table_USD.find('div', {'data-sort-row-index': '2'})
#         elem_kurs_USD = table_elem_USD.find('div', {'class': 'cc-col cc-col_rate'})
#         elem_kurs_value_USD = elem_kurs_USD.find('p')
#         USD_kurs = elem_kurs_value_USD.text
#         EUR_kurs = elem_kurs_value.text
#         bot.send_message(message.chat.id,f'Курс продажи доллара = {USD_kurs} '
#                                           f'Курс продажи евро = {EUR_kurs}')
#     elif message.text == '/change':
#         bot.send_message(message.chat.id, 'Введите сумму в рублях')
#
#         @bot.message_handler(content_types=['text'])
#         def change(message):
#             url_Euro = 'https://bankchart.by/servisy/konverter_valyut/1064/1000/0/974/978'
#             url_USD = 'https://bankchart.by/servisy/konverter_valyut/1064/1/0/974/840'
#             source_Euro = requests.get(url_Euro)
#             source_USD = requests.get(url_USD)
#             parced_site = BeautifulSoup(source_Euro.text, 'lxml')
#             table = parced_site.find('div', {'class': 'cc-table'})
#             table_elem = table.find('div', {'data-sort-row-index': '2'})
#             elem_kurs = table_elem.find('div', {'class': 'cc-col cc-col_rate'})
#             elem_kurs_value = elem_kurs.find('p')
#             parced_site_USD = BeautifulSoup(source_USD.text, 'lxml')
#             table_USD = parced_site_USD.find('div', {'class': 'cc-table'})
#             table_elem_USD = table_USD.find('div', {'data-sort-row-index': '2'})
#             elem_kurs_USD = table_elem_USD.find('div', {'class': 'cc-col cc-col_rate'})
#             elem_kurs_value_USD = elem_kurs_USD.find('p')
#             USD_kurs = elem_kurs_value_USD.text
#             EUR_kurs = elem_kurs_value.text
#             print(USD_kurs)
#             print(EUR_kurs)
#             a = list(USD_kurs)
#             a[1] = '.'
#             USD_kurs = ''.join(a)
#             b = list(EUR_kurs)
#             b[1] = '.'
#             EUR_kurs = ''.join(b)
#             USD_summa = int(message.text)/float(USD_kurs)
#             EUR_summa = int(message.text)/float(EUR_kurs)
#             bot.send_message(message.chat.id,
#                              'Сумма в долларах = ' + str(USD_summa) + '\n' + 'Сумма в евро = ' + str(EUR_summa))
#
#
# bot.polling()  # запускаем бота