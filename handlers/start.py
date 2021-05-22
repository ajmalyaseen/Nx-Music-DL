from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="Hello 👋🏻 {}!\n\n𝐈 𝐚𝐦 𝐬𝐢𝐦𝐩𝐥𝐞 𝐲𝐞𝐭 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐛𝐨𝐭 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐨𝐧𝐠𝐬 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 \n\n𝘊𝘭𝘪𝘤𝘬 /cmdlist 𝘍𝘰𝘳 𝘔𝘰𝘳𝘦 𝘏𝘦𝘭𝘱 𝘖𝘯 𝘔𝘺 𝘜𝘴𝘢𝘨𝘦 ❤".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("📕ABOUT", callback_data= "about"),
            InlineKeyboardButton("🔐 CLOSE", callback_data= "close")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online ✅**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )


@Client.on_message(filters.command(["cmdlist", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""𝙃𝙤𝙬 𝙏𝙤 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙤𝙣𝙜

💡 /song 𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴀᴜᴅɪᴏ

💡 /vid 𝐬𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴠɪᴅᴇᴏ

•𝐒𝐞𝐚𝐫𝐜𝐡 𝐬𝐨𝐧𝐠 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐥𝐢𝐧𝐤

💡 /search 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 : ɢᴇᴛ ʏᴏᴜʀ ꜱᴏɴɢ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ


@CoderzHex
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="📫UPDATES", url="https://t.me/CoderzHEX"),
              InlineKeyboardButton("🔐CLOSE", callback_data = "close")
              ]]
          )
      )
