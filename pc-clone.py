import os
from telethon import TelegramClient, events

api_id = int(os.environ["33477255"])
api_hash = os.environ["c28a9f60651fec7d570badf4fe5f23c1"]
session_str = os.environ.get("SESSION")

OFFLINE_MSG = "🙏 এখন আমি অফলাইনে আছি। অনলাইনে আসলে রিপ্লাই দেবো। ধন্যবাদ!"

client = TelegramClient("sess", api_id, api_hash)
offline = {"mode": True}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and offline["mode"]:
        await event.reply(OFFLINE_MSG)

@client.on(events.NewMessage(outgoing=True, pattern=r"^/off$"))
async def go_off(e):
    offline["mode"] = True
    await e.edit("✅ Offline ON")

@client.on(events.NewMessage(outgoing=True, pattern=r"^/on$"))
async def go_on(e):
    offline["mode"] = False
    await e.edit("✅ Online")

async def main():
    await client.start()
    print("Bot চলছে!")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())