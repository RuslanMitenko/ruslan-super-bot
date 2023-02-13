from telebot.handler_backends import State, StatesGroup


class FinInfoState(StatesGroup):
    name = State()
    purpose = State()
    param = State()
