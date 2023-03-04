# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot
# License Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot/blob/Auto-Approved-Bot/LICENSE

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = environ["5630873709:AAHtEhH9rsZslFQw3dHngt37jjwkNdK16qc"],
    api_id = int(environ["22359038"]),
    api_hash = environ["b3901895dc193c30c808ba4f1b550ed0"]
)

CHAT_ID = [int(pr0fess0r_99) for pr0fess0r_99 in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Adish4:Adish4@cluster0.dyhrj0e.mongodb.net/?retryWrites=true&w=majority")
SUDO = list(map(int, getenv("SUDO").split(5531461861)))

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("🗯 Channel", url="https://t.me/MOVIE_BOTX"), InlineKeyboardButton("Updates 📢", url="https://t.me/MOVIE_BOTX") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group Channnl](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo https://t.me/MOVIE_BOTX||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")
    
@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("Auto Approved Bot")
pr0fess0r_99.run()
