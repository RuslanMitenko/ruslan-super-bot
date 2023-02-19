from telebot.types import Message
from database.core import action
from database.models import db, History
from loader import bot
from states.company import CompanyInfoState
from api.search_ticker import search_ticker

db_write = action.create()


@bot.message_handler(commands=['search'])
def bot_search(message: Message):
    bot.send_message(message.from_user.id, 'Введите компанию или тикер для вывода информации по бумаге')
    bot.set_state(message.from_user.id, CompanyInfoState.name, message.chat.id)


@bot.message_handler(state=CompanyInfoState.name)
def get_company(message: Message):

    js = search_ticker(query=message.text)

    ticker_length = len(js['data']['stock'])
    if ticker_length > 0:
        for i_elem in range(ticker_length):
            name = js['data']['stock'][i_elem].get('name')
            price = js['data']['stock'][i_elem].get('price')
            currency = js['data']['stock'][i_elem].get('currency')
            country_code = js['data']['stock'][i_elem].get('country_code')
            exchange = js['data']['stock'][i_elem].get('exchange')
            change = js['data']['stock'][i_elem].get('change')
            change_percent = js['data']['stock'][i_elem].get('change_percent')
            previous_close = js['data']['stock'][i_elem].get('previous_close')

            bot.send_message(message.from_user.id, f'Основное инфо по компании:\n'
                                                   f'Имя: {name}\n'
                                                   f'Страна: {country_code}\n'
                                                   f'Биржа: {exchange}\n'
                                                   f'Цена: {price} {currency}\n'
                                                   f'Изменение к прошлому дню (абс.): {change} {currency}\n'
                                                   f'Изменение к прошлому дню (отн.): {change_percent} %\n'
                                                   f'Предыдущая цена: {previous_close} {currency}\n')

            data = [{"message": f'Инфо по бумагам {name}', "user": message.from_user.id}]
            db_write(db, History, data)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text

        bot.delete_state(message.from_user.id, message.chat.id)

    else:
        bot.send_message(message.from_user.id, 'К сожалению, не удалось найти информацию.'
                                               ' Попробуйте сформулировать точнее')
