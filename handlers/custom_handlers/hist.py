from telebot.types import Message

from database.core import action
from loader import bot
from database import actions, core
from database.models import db, History

db_read = action.retrieve()


@bot.message_handler(commands=['hist'])
def bot_hist(message: Message):
    text = ''
    retrieve = (db, History, History.id, History.create_at, History.message)
    print(retrieve)
    for elem in retrieve:
        # text = text + f'elem.id elem.message \n'
        print(History.message)

    bot.send_message(message.from_user.id, 'История запросов: ' + text)
