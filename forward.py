import os
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION")

source = int(os.getenv("SOURCE"))
destination = int(os.getenv("DESTINATION"))

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=source))
async def handler(event):
    await client.send_message(destination, event.message)

client.start()
client.run_until_disconnected()
