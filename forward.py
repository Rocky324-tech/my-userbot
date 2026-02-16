from pyrogram import Client, filters
import time

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

SOURCE = -1001912679284
DEST = -1003793224429

app = Client(
    "my_session",
    api_id=api_id,
    api_hash=api_hash,
    sleep_threshold=30,
    workers=10
)

@app.on_message(filters.chat(SOURCE))
def forward(client, message):
    try:
        client.copy_message(
            chat_id=DEST,
            from_chat_id=SOURCE,
            message_id=message.id
        )
        print("Forwarded successfully")

    except Exception as e:
        print("Error:", e)
        time.sleep(5)

print("Userbot started...")
app.run()
