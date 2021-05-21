from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\n𝐈 𝐚𝐦 𝐬𝐢𝐦𝐩𝐥𝐞 𝐲𝐞𝐭 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐛𝐨𝐭 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐒𝐨𝐧𝐠𝐬 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 \n\n𝘊𝘭𝘪𝘤𝘬 /help 𝘍𝘰𝘳 𝘔𝘰𝘳𝘦 𝘏𝘦𝘭𝘱 𝘖𝘯 𝘔𝘺 𝘜𝘴𝘢𝘨𝘦❤".format(message.from_user.mention),
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
        text="""**How To Download Song**
•To Audio 
👉 `/song` - Song Name :Download your song to audio

•To Video 
👉 `/vid` - Video Name : Download your song to Video 

•Search song YouTube link 
👉 `/search` - song name : Get your Song Youtube link 

•Other ways 
👉 `/deezer` - song name : __download songs you want quickly via deezer__
👉 `/saavn` - song name : __download songs you want quickly via saavn__
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="UPDATES", url="https://t.me/CoderzHEX")
              ]]
          )
      )
