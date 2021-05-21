from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\n𝐈 𝐚𝐦 𝐬𝐢𝐦𝐩𝐥𝐞 𝐲𝐞𝐭 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐛𝐨𝐭 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐨𝐧𝐠𝐬 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 \n\n𝘊𝘭𝘪𝘤𝘬 /help 𝘍𝘰𝘳 𝘔𝘰𝘳𝘦 𝘏𝘦𝘭𝘱 𝘖𝘯 𝘔𝘺 𝘜𝘴𝘢𝘨𝘦 ❤".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("📕ABOUT", url="http://telegra.ph/About-05-21-3"),
            InlineKeyboardButton('🔐 CLOSE', callback_data='close')
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
              InlineKeyboardButton(text="UPDATES", url="https://t.me/CoderzHEX")
              ]]
          )
      )


@Client.on_message(filters.command(["help", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        text="""__𝙃𝙤𝙬 𝙏𝙤 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙤𝙣𝙜__

💡 /song 𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴀᴜᴅɪᴏ

💡 /vid 𝐬𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴠɪᴅᴇᴏ

•𝐒𝐞𝐚𝐫𝐜𝐡 𝐬𝐨𝐧𝐠 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐥𝐢𝐧𝐤

💡 /search 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 : ɢᴇᴛ ʏᴏᴜʀ ꜱᴏɴɢ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ

• 𝐎𝐭𝐡𝐞𝐫 𝐰𝐚𝐲𝐬

💡 /deezer 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢꜱ ʏᴏᴜ ᴡᴀɴᴛ Qᴜɪᴄᴋʟʏ ᴠɪᴀ ᴅᴇᴇᴢᴇʀ

💡 /saavn 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢꜱ ʏᴏᴜ ᴡᴀɴᴛ Qᴜɪᴄᴋʟʏ ᴠɪᴀ ꜱᴀᴀᴠɴ

**@CoderzHex**
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="📫UPDATES", url="https://t.me/CoderzHEX")
              ]]
          )
      )
