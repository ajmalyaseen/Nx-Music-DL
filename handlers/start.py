from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\n! I am simple yet powerful bot to download Songs Audio And Video\n\n**Click /help For More Help On My Usage❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("CREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("ABOUT", url="https://telegra.ph/Music-Bot-05-07"),
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
