from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7298907113:AAH8ln3REKeXNpkPSke8TAOo2FJbFBmtJZA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button1)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; '
                              f'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    for_man = 10 * int(data['weight']) + 6,25 * int(data['growth']) - 5 * int(data['age']) + 5
    for_woman = 10 * int(data['weight']) + 6,25 * int(data['growth']) - 5 * int(data['age']) - 161
    await message.answer(f'Норма клорий для мужчин - {for_man}, для женщин - {for_woman}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Могу сделать для тебя расчет нормы калорий', reply_markup=kb)


@dp.message_handler(text=['Привет', 'привет'])
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
