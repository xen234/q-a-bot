import logging
from os import environ
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from api import JikanWrapper
from database import PostgreDB


bot = Bot(token=environ['TOKEN'])
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')

database = PostgreDB()
api = JikanWrapper()
