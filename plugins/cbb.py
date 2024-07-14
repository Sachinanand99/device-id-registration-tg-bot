from bot import Varun
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@Varun.on_callback_query()
async def cb_handler(bot: Varun, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=f"<b>Use command <code>/register &lt;serial no. of your device&gt;</code></b>\nBot designed by @savoryrabbit 🧑‍🎓",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
