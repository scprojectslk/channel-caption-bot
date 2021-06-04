# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("☆༺ ──•◈•─ ─•◈•──༻☆
🌀☘ jϴῖͷ ῠϩ ϴͷ ϯϵlϵϭrαϻ ☘🌀

⭐️ ᴛᴄ - @GatayaofficialChannel 

⭐️ ɢʀᴏᴜᴘ - @gatayaofficialnew 

💎🍀 ร♄คгє & รยԹԹ๏гt ยร 🍀💎

😉 ғɪʟᴍs & ᴛᴠ-sᴇʀɪᴇs (ɢᴀᴛᴀʏᴀ ᴏғғɪᴄɪᴀʟ) 😉
☆༺ ──•◈•─ ─•◈•──༻☆",
          
reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("♻️ ᴊᴏɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ ♻️", url="https://t.me/")]
            ]
                                           )
                      )
