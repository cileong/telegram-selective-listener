#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Telegram App: Selective Listener """

from telethon import TelegramClient, events
from pathlib import Path
import yaml


# Load the script configurations.

PATH = Path("config.yaml")
assert PATH.exists(), "Configuration file not found."

with PATH.open(mode="r") as f:
    cfg = yaml.safe_load(f)

API_ID = cfg["api_id"]
API_HASH = cfg["api_hash"]
TARGETS = cfg["targets"]


# Initialize client.
client = TelegramClient("selective-listener", API_ID, API_HASH)


@client.on(events.NewMessage(from_users=TARGETS))
async def on_message_received(event):
    print(event.message.message)


# Initiate main loop.
# Selectively listen for new messages until the client disconnect.

client.start()
client.run_until_disconnected()
