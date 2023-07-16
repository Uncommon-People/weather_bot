import json
from aiogram import Bot
from aiogram.dispatcher import Dispatcher


TOKEN = json.load(open('keys.json'))['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)