import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)

from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "pdf",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )


LIST = {}

@app.on_message(filters.command(['start']))
async def start(client, message):
 await message.reply_text(text =f"""ʜᴇʟʟᴏ  ᴅᴇᴀʀ  {message.from_user.first_name } ᴡʟᴄᴍ ᴛᴏ ɪᴍᴀɢᴇ ᴛᴏ  ᴘᴅғ ᴄᴏɴᴠᴇʀᴛᴏʀ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @itz_mst_boy 

ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ɪᴍɢ ᴛᴏ ᴘᴅғ  sᴏ ᴅᴏɴᴛ ᴡᴀsᴛᴇ ᴜʀ ᴛɪᴍᴇ ᴅɪʀᴇᴄᴛʟʏ sᴇɴᴅ ᴍᴇ ɪᴍɢ ғʀᴏᴍ ᴀɴʏᴡʜᴇʀᴇ  ғʀᴏᴍ ɢᴀʟʟᴇʀʏ ɪ ᴡɪʟʟ ᴄᴏɴᴠᴇʀᴛ  ɪᴍᴀɢᴇ  ᴛᴏ ᴘᴅғ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄ ᴀᴛ ʟᴀsᴛ ᴛʏᴘᴇ  /convert.

ᴛʜɪs  ʙᴏᴛ  ɪs  ᴄʀᴇᴀᴛᴇᴅ  ʙʏ  @iTz_mSt_bOy """,reply_to_message_id = message.message_id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ❤" ,url="https://t.me/mukhushi_official") ],
                 [InlineKeyboardButton("ᴘᴏᴡᴇʀᴇᴅ  ʙʏ  🤗", url="https://t.me/mastermind_network_official") ],
                 [InlineKeyboardButton("ᴘᴏᴡᴇʀᴇᴅ  ʙʏ  🤗", url="https://t.me/mastermind_network_official") ]       ]        ) )




@app.on_message(filters.private & filters.photo)
async def pdf(client,message):
 
 if not isinstance(LIST.get(message.from_user.id), list):
   LIST[message.from_user.id] = []

  
 
 file_id = str(message.photo.file_id)
 ms = await message.reply_text("ᴄᴏɴᴠᴇʀᴛɪɴɢ  ᴛᴏ  ᴘᴅғ  ʙʏ  @itz_mst_boy ......")
 file = await client.download_media(file_id)
 
 image = Image.open(file)
 img = image.convert('RGB')
 LIST[message.from_user.id].append(img)
 await ms.edit(f"{len(LIST[message.from_user.id])} ɪᴍᴀɢᴇ    sᴜᴄᴄᴇssғᴜʟʟʏ  ᴄʀᴇᴀᴛᴇᴅ  ɪɴᴛᴏ ᴘᴅғ  ɪғ ʏᴏᴜ  ᴡᴀɴᴛ  ᴀᴅᴅ  ᴍᴏʀᴇ  ɪᴍᴀɢᴇ sᴇɴᴅ ᴍᴇ  ᴏɴᴇ  ʙʏ  ᴏɴᴇ \n\n **ɪғ ᴅᴏɴᴇ  ᴄʟɪᴄᴋ  ʜᴇʀᴇ  👉 /convert** ")
 

@app.on_message(filters.command(['convert']))
async def done(client,message):
 images = LIST.get(message.from_user.id)

 if isinstance(images, list):
  del LIST[message.from_user.id]
 if not images:
  await message.reply_text( "ɴᴏ  ɪᴍᴀɢᴇ ғᴏᴜɴᴅ  ʟᴏʟ  ʀᴇᴀᴄʜᴇᴀᴋ  ɪᴛ  ᴏʀ ᴄᴏɴᴛᴀᴄᴛ  ᴍᴇ ᴀᴛ @friend_warriors!!")
  return

 path = f"{message.from_user.id}" + ".pdf"
 images[0].save(path, save_all = True, append_images = images[1:])
 
 await client.send_document(message.from_user.id, open(path, "rb"), caption = "ʜᴇʀᴇ  ɪs ʏᴏᴜʀ ᴘᴅғ Support  @mukhushi_official !!")
 os.remove(path)
 
 
 
 
app.run()
