from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *
from database import *

@Client.on_message(filters.command("start") & filters.incoming)
async def start_command(client, message):
    userMention = message.from_user.mention() 
    # Check for forced subscription requirement
    if FSUB and not await get_fsub(client, message):
        return

    welcome_message = (
        "**👋 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴋʀɪsʜ ᴀɪ!**\n\n"
        " ɪ'ᴍ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴀɪ ᴀssɪsᴛᴀɴᴛ, ᴄʀᴀғᴛᴇᴅ ᴡɪᴛʜ ʟᴏᴠᴇ ʙʏ ⏤͟͟͞͞ 🇮🇳 ᴋʀɪsʜ ᴛᴇᴀᴍ.\n\n"
        " ʜᴇʀᴇ’s ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ ғᴏʀ ʏᴏᴜ:**\n"
        "ᴊᴜsᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ ᴏɴ ᴛʜɪs ᴇxᴄɪᴛɪɴɢ ᴊᴏᴜʀɴᴇʏ! 🚀"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(" 🔥ʜᴇʟᴘ", callback_data="help"),
         InlineKeyboardButton(" ᴀʙᴏᴜᴛ", callback_data="about")],
        [InlineKeyboardButton("🥀 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/KRISHSUPPORT"),
         InlineKeyboardButton("🥀 sᴜᴘᴘᴏʀᴛ", url="https://t.me/krishnetwork")]
    ])

    await client.send_photo(chat_id=message.chat.id, photo="https://envs.sh/c2T.png", caption=welcome_message, reply_markup=keyboard)

@Client.on_callback_query()
async def handle_button_click(client, callback_query):
    if callback_query.data == "help":
        help_message = "**🔍 Choose a category for assistance:**\nLet's navigate through the possibilities together! 🌐"
        help_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 Cʜᴀᴛ Wɪᴛʜ Aɪ", callback_data="chatwithai"),
             InlineKeyboardButton("🖼️ ɪᴍᴀɢᴇ", callback_data="image")],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start")]
        ])
        await edit_message(client, callback_query, help_message, help_keyboard)

    elif callback_query.data == "start":
        welcome_message = (
            "**👋 Welcome to Response By Ai!**\n\n"
            "🤖 I'm your personal AI ᴀssɪsᴛᴀɴᴛ, ᴄʀᴀғᴛᴇᴅ ᴡɪᴛʜ ʟᴏᴠᴇ ʙʏ ⏤͟͟͞͞ 🇮🇳 ᴛᴇᴀᴍ ᴋʀɪsʜ.\n\n"
            "✨ **Here’s what I ᴄᴀɴ ᴅᴏ ғᴏʀ you:**\n"
            "Just click the ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ on ᴛʜɪs ᴇxᴄɪᴛɪɴɢ ᴊᴏᴜʀɴᴇʏ! 🚀"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" 🔥 ʜᴇʟᴘ", callback_data="help"),
             InlineKeyboardButton(" ᴀʙᴏᴜᴛ", callback_data="about")],
            [InlineKeyboardButton("🥀 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/krishnetwork"),
             InlineKeyboardButton("🥀 sᴜᴘᴘᴏʀᴛ", url="https://t.me/krishnetwork")]
        ])

        await edit_message(client, callback_query, welcome_message, keyboard)

    elif callback_query.data == "chatwithai":
        chat_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🥀 sᴜᴘᴘᴏʀᴛ", url="https://t.me/krishnetwork")]
        ])
        chat_message = (
            "**💬 Let’s ᴅɪᴠᴇ ɪɴᴛᴏ ᴀ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴ ᴡɪᴛʜ ᴀɪ!**\n\n ✌️**ʀᴇᴀᴅʏ ᴛᴏ ᴇxᴘʟᴏʀᴇ?** ᴊᴜsᴛ ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ʙᴇʟᴏᴡ ᴛᴏ ᴜɴʟᴏᴄᴋ ᴇɴᴅʟᴇss ᴘᴏssɪʙɪʟɪᴛɪᴇs! 🪐\n\n✔️ **ɢᴏᴛ ᴀ ǫᴜᴇsᴛɪᴏɴ?** \n sᴇɴᴅ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴜsɪɴɢ **/ask**, ᴀɴᴅ ɢᴇᴛ ᴠᴀʟᴜᴀʙʟᴇ ᴀɴsᴡᴇʀs ғʀᴏᴍ sᴇᴀʀᴄʜ ᴡɪᴛʜ ᴀɪ! 💡\n\ɴᴊᴏɪɴ ᴛʜᴇ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴ ᴀɴᴅ sᴇᴇ ᴡʜᴀᴛ ᴡᴏɴᴅᴇʀs ᴀᴡᴀɪᴛ!"
        )
        await edit_message(client, callback_query, chat_message, chat_keyboard)

    elif callback_query.data == "image":
        image_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/krishnetwork")]
        ])
        await edit_message(client, callback_query, "**🖼️ Your Creative Journey Starts Here!**\n\n\n**🎨 Unleash Your Creativity!** \n Type **/draw** followed by your vision, like “A futuristic city at sunset,” and watch as your imagination comes to life with stunning AI-generated artwork! ✨\n\n**📸 Transform Your Ideas!** \nGet ready for Image, you’ll be able to type **/scan_ph** along with your image description to let our AI create detailed descriptions and captivating images based on your prompts. 🔍✨\n\n\n**Get started now and see what magic awaits!**", image_keyboard)

    elif callback_query.data == "about":
        about_message = (
            "**ℹ About This Bot**\n\n"
            "**Owner:** ⏤͟͟͞͞ 🇮🇳 ᴋʀɪsʜ ᴛᴇᴀᴍ  </>\n"
            " **Functionality:**\n"
            "- Fast and accurate answers to your questions! ⚡\n"
            "- Generate beautiful images based on your prompts! 🎨\n"
            "- Engage in chat to learn and explore more! 💬\n\n"
            " **Powered by:** [ᴋʀɪsʜ ɴᴇᴛᴡᴏʀᴋ]\n\n"
            " ᴊᴏɪɴ ᴍᴇ ɪɴ ᴛʜɪs adventure and ʟᴇᴛ ᴇxᴘʟᴏʀᴇ ᴛʜᴇ ʟɪᴍɪᴛʟᴇss ᴘᴏssɪʙɪʟɪᴛɪᴇs ᴛᴏɢᴇᴛʜᴇʀ!"
        )
        about_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" ʙᴀᴄᴋ", callback_data="help"),
             InlineKeyboardButton("🔗 ʀᴇᴘᴏ", url="https://graph.org/file/5922a83b355489ba0853a.mp4")]
        ])
        await edit_message(client, callback_query, about_message, about_keyboard)

async def edit_message(client, callback_query, caption, reply_markup):
    try:
        await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)
    except Exception as e:
        print("Error editing message caption:", e)

    await client.answer_callback_query(callback_query.id)
