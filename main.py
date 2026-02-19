from pyrogram import Client, filters
import asyncio

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION_STRING = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

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
