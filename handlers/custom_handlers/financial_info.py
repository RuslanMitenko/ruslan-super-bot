from database.core import action
from database.models import db, History
from loader import bot
from states.fin_info import FinInfoState
from telebot.types import Message
from keyboards.reply.fin_info_params import fin_info_params
from keyboards.reply.sort_params import sort_params
from api.fin_info import fin_info

db_write = action.create()


@bot.message_handler(commands=['financial_info'])
def bot_search(message: Message):
    bot.send_message(message.from_user.id, 'Введите компанию или тикер для вывода финансовой информации по компании.')
    bot.set_state(message.from_user.id, FinInfoState.name, message.chat.id)


@bot.message_handler(state=FinInfoState.name)
def get_company(message: Message):

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text

    bot.send_message(message.from_user.id, 'Выберете финансовый показатель:', reply_markup=fin_info_params())
    bot.set_state(message.from_user.id, FinInfoState.purpose, message.chat.id)


@bot.message_handler(content_types=['text'], state=FinInfoState.purpose)
def get_param(message: Message):

    if message.text == 'Доход (revenue)':
        purpose = 'revenue'
    elif message.text == 'Операционные расходы (operating expense)':
        purpose = 'operating_expense'
    elif message.text == 'Чистая прибыль (net income)':
        purpose = 'net_income'
    elif message.text == 'Рентабельность по чистой прибыли (net profit margin)':
        purpose = 'net_profit_margin'
    elif message.text == 'Прибыль на акцию (earning per share)':
        purpose = 'earning_per_share'
    elif message.text == 'EBITDA':
        purpose = 'EBITDA'

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['purpose'] = purpose
        data['purpose text'] = message.text

    bot.send_message(message.from_user.id, 'Установите параметры:',
                     reply_markup=sort_params())
    bot.set_state(message.from_user.id, FinInfoState.param, message.chat.id)


@bot.message_handler(content_types=['text'], state=FinInfoState.param)
def get_purpose(message: Message):

    if message.text == 'По возрастанию, ежеквартально':
        period = 'QUARTERLY'
        reverse = False
    elif message.text == 'По убыванию, ежеквартально':
        period = 'QUARTERLY'
        reverse = True
    elif message.text == 'По возрастанию, ежегодно':
        period = 'ANNUAL'
        reverse = False
    elif message.text == 'По убыванию, ежегодно':
        period = 'ANNUAL'
        reverse = True

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['period'] = period
        data['reverse'] = reverse

    js = fin_info(symbol=data['name'], period=period)

    if len(js['data']) > 0:
        sorted_tuple = sorted(js['data']['income_statement'], key=lambda elem: elem[data['purpose']],
                              reverse=data['reverse'])

        if data['period'] == 'QUARTERLY':
            text = ''
            for elem in sorted_tuple:
                text = text + f"{elem['year']} год    {elem['quarter']} квартал:    {elem[data['purpose']]}\n"

        elif data['period'] == 'ANNUAL':
            text = ''
            for elem in sorted_tuple:
                text = text + f"{elem['year']} год:    {elem[data['purpose']]}\n"

        bot.send_message(message.from_user.id, text)

        data = [{"message": f"Запрос показателя {data['purpose text']} по компании {data['period']}",
                 "user": message.from_user.id}]
        db_write(db, History, data)

    else:
        bot.send_message(message.from_user.id, 'К сожалению, не удалось найти информацию.'
                                               ' Попробуйте ещё раз.')

    bot.delete_state(message.from_user.id, message.chat.id)
