
from Script import script
from info import LOG_CHANNEL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 📢', url=f'https://t.me/Malayalam_requester_bot')
            ],
            [
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿 ',callback_data="help")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        disable_web_page_preview = True,
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.B_LINK), reply_markup=reply_markup)
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, message.chat.username, total, temp.U_NAME, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title, message.chat.username)
        return
