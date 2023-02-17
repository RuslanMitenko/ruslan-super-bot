from telebot.types import Message

from database.core import action
from loader import bot
from database import actions, core
from database.models import db, History

db_read = action.retrieve()


@bot.message_handler(commands=['hist'])
def bot_hist(message: Message):
    text = ''
    # retrieve = (db, History, History.id, History.create_at, History.message)
    # print(retrieve)
    # for elem in retrieve:
        # text = text + f'elem.id elem.message \n'
        # print(History.message)

    text = ''
    with db:
        query = History.select().where(History.user == message.from_user.id).order_by(History.id.desc()).limit(10)
        for hist in query:
            text = text + f'\n{hist.create_at}     {hist.message}'

    bot.send_message(message.from_user.id, 'Последние 10 запросов:' + text)
