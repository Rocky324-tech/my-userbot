from pyrogram import Client, filters
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"
SESSION = "PASTE_SESSION_STRING"

SOURCE = -1001912679284
DEST = -1003798031630

app = Client(
    "render-forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

@app.on_message(filters.chat(SOURCE))
async def forward(client, message):
    try:
        await message.copy(DEST)
        print("Forwarded")
    except Exception as e:
        print(e)

# fake web server (important for free plan)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run_web():
    server = HTTPServer(('0.0.0.0', 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_web).start()

print("Render Forwarder Running")
app.run()
