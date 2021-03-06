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
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .


import asyncio
import glob
import inspect
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import dotenv
from datetime import datetime as dt
import logging
from logging.handlers import RotatingFileHandler
#from logging import DEBUG, INFO, basicConfig, getLogger, warning
from pathlib import Path

import requests
import telethon.utils
from decouple import config
from html_telegraph_poster import TelegraphPoster
from telethon import Button, TelegramClient, errors, events, functions, types
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ExportChatInviteRequest as cl
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name

FREE_USER_MAX_FILE_SIZE = 2097152000

LOG_FILE_ZZGEVC = "log.txt"

if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)


dotenv.load_dotenv("config.env")
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
