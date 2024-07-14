from aiohttp import web
from plugins import web_server

from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import *

class Varun(Client):
    def __init__(self):
        super().__init__(
            name="Varun",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root" : "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
    
    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        await self.send_message(
            chat_id=OWNER_ID,
            text="Bot has started! 🙌"
        )

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!")
        self.username = usr_bot_me.username

        #web response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
    
    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

