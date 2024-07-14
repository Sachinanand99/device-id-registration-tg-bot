from bot import Varun
from pyrogram.types import Message
from pyrogram import filters
from config import *
from datetime import datetime
from helper_func import get_readable_time

@Varun.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Varun, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Varun.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if message.from_user.id in ADMINS:
        print(f"Admin {message.from_user.id} tried to access the useless function.")
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)

