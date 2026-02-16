import asyncio
from pyrogram import Client, filters, idle

# YOUR DETAILS (already filled)
API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"
PHONE_NUMBER = "+916305571497"

SOURCE = -1003798031630
DESTINATION = -1003793224429

# Create client
app = Client(
    "userbot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=PHONE_NUMBER
)

# Copy messages (NO forward tag)
@app.on_message(filters.chat(SOURCE))
async def forward_message(client, message):
    try:
        await message.copy(DESTINATION)
        print(f"Copied message {message.id}")
    except Exception as e:
        print(f"Error: {e}")

# Start bot
async def main():
    await app.start()
    print("✅ Userbot running perfectly and forwarding messages...")
    await idle()

asyncio.run(main())
