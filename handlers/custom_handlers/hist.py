from telebot.types import Message
from database.core import action
from loader import bot
from database.models import db, History

db_read = action.retrieve()


@bot.message_handler(commands=['hist'])
def bot_hist(message: Message):

    text = '\n'
    user_id = message.from_user.id
    retrieve = db_read(db, History, user_id, History.id, History.create_at, History.message)
    for elem in retrieve:
        text = text + f'{elem.create_at} {elem.message} \n'

    bot.send_message(message.from_user.id, 'Последние 10 запросов:' + text)
