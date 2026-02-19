from pyrogram import Client, filters
import asyncio

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION_STRING = "PASTE_YOUR_SESSION_STRING"

SOURCE = -1001912679284
DESTINATIONS = [-1003798031630]

app = Client(
    "separate-forwarder",
    session_string=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.chat(SOURCE))
async def forward(client, message):
    for dest in DESTINATIONS:
        try:
            await message.copy(dest)
            print(f"Forwarded {message.id}")
            await asyncio.sleep(0.3)
        except Exception as e:
            print(e)

print("Separate Forwarder Running")
app.run()
