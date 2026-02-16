from pyrogram import Client, filters
import asyncio

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

source_chat = -1003798031630
destination_chat = -1003793224429

app = Client("my_session", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_chat))
async def forward(client, message):
    try:
        await message.copy(destination_chat)
        print("Message forwarded instantly")
    except Exception as e:
        print(e)

print("Userbot running 24/7 perfectly...")

app.run()
