from aiogram import types, Dispatcher
from weather_API import weather
from create_bot import bot


async def start(message: types.Message):
    await message.answer('Hi')


async def get_weather(message: types.Message):
    if message.text == 'Weather':
        await message.answer(f'Temp: {weather.get_temp()}')
    else:
        await message.answer('Write "Weather", what know info of temperature')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(get_weather)