import asyncio
import sys
import traceback
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError

# ==============================
# YOUR DETAILS
# ==============================

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

SESSION = "1BVtsOKwBu5X2gfVjyqwUJ2WInr1W4BjuCOjLYGt3_uP1Wz2gjblsCdr28cbmQwpGcz1-tIxy5J0P88-XzsMrGFx6fXGJk0fQBuZfwHMNcwGQmIJAQimoo1z1eEia57MoyoD0pTVS7zlUJVvG8o3mmyl04Q2C_uERf903QUkLLmCI4pWMSY8OEZJigYlFGheRyx5V-o7edsDIoYovv7hlryNyKCGDME77Wanlkb0ZAHr6jy2EVJzA1Jl3W6FvLHq-eTo0T2W5ofiuZEY733vn-a1PjPq2vFBO-5TZjPZXLd5dt-xZpQnL1e2W1NGIGbq-nUEtEUG63NFAz_jO1cJZMhvvBFRZOdo="

SOURCE = -1003798031630
DESTINATION = -1003793224429

# ==============================
# CREATE CLIENT
# ==============================

client = TelegramClient(
    StringSession(SESSION),
    api_id,
    api_hash,
    auto_reconnect=True,
    connection_retries=None,
    retry_delay=5
)

# ==============================
# FORWARD HANDLER
# ==============================

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):

    try:
        msg = event.message

        # forward everything (text, media, files)
        await client.forward_messages(
            DESTINATION,
            msg,
            from_peer=SOURCE
        )

        print(f"Forwarded message ID: {msg.id}")

    except FloodWaitError as e:
        print(f"FloodWait: Sleeping {e.seconds} seconds")
        await asyncio.sleep(e.seconds)

    except Exception as e:
        print("Error occurred:")
        traceback.print_exc()

# ==============================
# MAIN LOOP
# ==============================

async def main():

    while True:

        try:

            print("Connecting to Telegram...")
            await client.start()

            print("SUCCESS: Userbot is running 24/7")
            print(f"Forwarding from {SOURCE} to {DESTINATION}")

            await client.run_until_disconnected()

        except Exception as e:

            print("Connection lost. Reconnecting in 5 seconds...")
            traceback.print_exc()

            await asyncio.sleep(5)

# ==============================
# START BOT
# ==============================

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        print("Stopped by user")
        sys.exit()
