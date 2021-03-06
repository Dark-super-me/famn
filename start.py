#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in <https://github.com/1Danish-00/CompressorBot/blob/main/License> .

import logging
from logging.handlers import RotatingFileHandler
from helper._get import *


#LOG = -1001472251228

LOG_FILE_ZZGEVC = "log.txt"

if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)
FREE_USER_MAX_FILE_SIZE = 2097152000

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

LOGS = logging.getLogger(__name__)

LOGS.info("Starting...")



######## Connect ########


try:
    cbot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()


####### GENERAL CMDS ########


@cbot.on(events.NewMessage(pattern="/start"))
async def _(e):
    await start(e)
    
@cbot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@cbot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)

@cbot.on(events.NewMessage(pattern="/log"))
async def _(e):
    user = await e.get_chat()
    if user.id in OWNER:
        await e.client.send_file(e.chat_id, LOG_FILE_ZZGEVC)
    else:
        return
    
@cbot.on(events.NewMessage(pattern="/off"))
async def _(e):
    user = await e.get_chat()
    if user.id in OWNER:
        await e.reply("Shutting Down ...")
        cbot.disconnect()
        quit(1)
    else:
        return    
######## Callbacks #########


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sshot(.*)")))
async def _(e):
    await screenshot(e)

@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sao(.*)")))
async def _(e):
    await sao(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gsmpl(.*)")))
async def _(e):
    await sample(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"encc(.*)")))
async def _(e):
    await encc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sencc(.*)")))
async def _(e):
    await sencc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ccom(.*)")))
async def _(e):
    await ccom(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)
@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"anidl(.*)")))
async def _(e):
    await anidl(e)

########## Direct ###########


@cbot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@cbot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)
    
@cbot.on(events.NewMessage(pattern="/auth"))
async def _(e):
    await auth(e)
@cbot.on(events.NewMessage(pattern="/revoke"))
async def _(e):
    await revoke(e)
########## AUTO ###########


@cbot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


########### Start ############

LOGS.info("Malbook Bot has started.")
cbot.run_until_disconnected()
