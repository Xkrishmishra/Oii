from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *

async def get_fsub(bot, message):
    target_channel_id = AUTH_CHANNEL  # Your channel ID
    user_id = message.from_user.id
    try:
        # Check if user is a member of the required channel
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        # Generate the channel invite link
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        join_button = InlineKeyboardButton("🔔 Join Our Channel", url=channel_link)

        # Display a message encouraging the user to join
        keyboard = [[join_button]]
        await message.reply(
            f"<b>👋 Hello {message.from_user.mention()}, Welcome!</b>\n\n"
            "🥀 <b>ᴇxᴄʟᴜsɪᴠᴇ ᴀᴄᴄᴇss ᴀʟᴇʀᴛ!</b> ✨\n\n"
            "To ᴜɴʟᴏᴄᴋ ᴀʟʟ ᴛʜᴇ ᴀᴍᴀᴢɪɴɢ ғᴇᴀᴛᴜʀᴇs I ᴏғғᴇʀ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ. "
            "ᴛʜɪs ʜᴇʟᴘs ᴜs ᴋᴇᴇᴘ ʏᴏᴜ ɪɴғᴏʀᴍᴇᴅ ᴀɴᴅ ᴇɴsᴜʀᴇs ᴛᴏᴘ sᴇʀᴠɪᴄᴇ ᴊᴜsᴛ ғᴏʀ ʏᴏᴜ! \n\n"
            "<i>🚀 ᴊᴏɪɴ ɴᴏᴡ ᴀɴᴅ ᴅɪᴠᴇ ɪɴᴛᴏ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ ᴀɴᴅ ᴄʀᴇᴀᴛɪᴠɪᴛʏ!</i>",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return False
    else:
        return True
