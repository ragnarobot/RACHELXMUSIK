#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class MusikkuBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "Musikku",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot Started"
            )
        except:
            LOGGER(__name__).error(
                "Bot gagal mengakses Grup log. Pastikan Anda telah menambahkan bot ke saluran log dan dipromosikan sebagai admin!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        b = await self.get_chat_member(config.MUST_JOIN, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Tolong promosikan Bot sebagai Admin di Grup Logger"
            )
            sys.exit()
        if b.status != "administrator":
            LOGGER(__name__).error(
                f"Tolong promosikan Bot sebagai Admin di Grup @{config.MUST_JOIN}"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
