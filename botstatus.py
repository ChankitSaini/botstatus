from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os


API_ID = os.environ["API_ID"],
API_HASH = os.environ["API_HASH"],
SESSION_STRING = os.environ["SESSION_STRING"]
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])
GROUP_ID = int(os.environ["GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

app = Client(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main_botstatus():
    async with app:
            while True:
                print("Checking...")
                xxx_botstatus = f"š | **Real-Time Bot Status**"
                for bot in BOT_LIST:
                    try:
                        yyy_botstatus = await app.send_message(bot, "/start")
                        aaa = yyy_botstatus.id
                        await asyncio.sleep(10)
                        zzz_botstatus = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_botstatus:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_botstatus += f"\n\nš¤  @{bot}\n        ā **Down** ā"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"šØ **Beep! Beep!! @{bot} is down** ā")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_botstatus += f"\n\nš¤  @{bot}\n        ā **Alive** ā"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_botstatus += f"\n\nāļø Last checked on: {last_update} ({TIME_ZONE})\n\n<i>ā»ļø Refreshes automatically</i>"
                await app.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, xxx_botstatus)
                await app.send_message(int(GROUP_ID), xxx_botstatus)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(1800)
                        
app.run(main_botstatus())
