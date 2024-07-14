import asyncio
from bot import Varun
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMINS, OWNER_ID, WAIT_MSG
from helper_func import progress, register_device, setup_github_and_push

@Varun.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("😊 Help",
                callback_data="help"
                ),
                InlineKeyboardButton("🔒 Close",
                                     callback_data="close"
                )
            ]

        ]
    )
    START_MSG = "Hello {first}\n\nI am a registration bot. 🌸"
    await message.reply_text(
                text=START_MSG.format(
                    first=message.from_user.first_name,
                ),
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                quote=True
            )
    return


@Varun.on_message(filters.command('register') & filters.private)
async def reg_command(client: Varun, message: Message):
    _, _, serial_no = message.text.partition(' ')
    reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ]])
    userid = message.from_user.id
    username = None if not message.from_user.username else '@' + message.from_user.username
    try:
        if not len(serial_no) == 8:
            await client.send_message(chat_id=userid, text="You have given wrong serial no.\nCheck again and try again 😑")
            return
        registered = register_device(serial_no)
        if registered:
            await client.send_message(chat_id=userid, text="You have been registered. 💖",
                            reply_markup=reply_markup
                            )
            await client.send_message(chat_id=OWNER_ID, text=f"User : <code>{userid}</code>\nTag : {username}\nRegistered device <code>{serial_no}</code> successfully. 😺")
        else:
            await client.send_message(chat_id=userid, text="You were not able to register.\nPlease try again 🥺",
                            reply_markup=reply_markup)
            await client.send_message(chat_id=OWNER_ID, text=f"User : <code>{userid}</code>\nTag : {username}\nRegistered device <code>{serial_no}</code> failed. 😵")
            
    except Exception as e:
        await client.send_message(chat_id=message.from_user.id, text="An internal error occurred.\nTry again.😭.",
                reply_markup=reply_markup
            )
        print(e)
    return

@Varun.on_message(filters.command('help') & filters.private)
async def register_command(client: Client, message: Message):
    await message.reply_text(
            text = f"<b>Use command <code>/register &lt;serial no. of your device&gt;</code></b> 📚",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔒 Close", callback_data="close")
            ]])
        )
    return

@Varun.on_message(filters.command('push') & filters.private & filters.user(ADMINS))
async def push_on_github(client: Varun, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    result = setup_github_and_push()
    if result:
        await msg.edit(f"Uploaded to github! 😃")
    else:
        await msg.edit(f"Error in uploading! 😔\nUse <code>/getfile</code> for getting your updated data to you.")


@Varun.on_message(filters.command('getfile') & filters.private & filters.user(ADMINS))
async def sendfile(client: Varun, message:Message):
    try:
        await client.send_document(chat_id=message.chat.id, document="registered.txt",file_name='registered.txt', progress=progress, caption="😺!!")
    except Exception as e:
        print(e)

