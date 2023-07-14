"""

This is a echo bot.

It echoes any incoming text messages.

"""


from aiogram import Bot, Dispatcher, types
from bot.src.settings import BOT_TOKEN
from bot.src.database.create_table import execute_query
from zoneinfo import ZoneInfo
from datetime import datetime


# Initialize bot and dispatcher

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """

    This handler will be called when user sends `/start` or `/help` command

    """
    time_now = datetime.now(tz=ZoneInfo('UTC')).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, user_id, message_time)"
                    f"VALUES ('{message.text}', {message.from_user['id']}, '{time_now}')")
    execute_query(insert_query)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:

    # await bot.send_message(message.chat.id, message.text)
    time_now = datetime.now(tz=ZoneInfo('UTC')).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, user_id, message_time)"
                    f"VALUES ('{message.text}', {message.from_user['id']}, '{time_now}')")
    execute_query(insert_query)
    await message.answer(message.text)



