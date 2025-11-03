import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("Filestore", "")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/AniReal_Chat_Group_Asia")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/fdc4357abfaba23255e98-24d1bbfa3888cdfcfe.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/5fb2a9e904ae7870b8862-fb58603ada523ac527.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>⚡ This is a <u>Private Premium Bot</u> – Only admins & management can operate it.\n🔐 To get the bot link and access its features, join our mentioned channel and click the direct link provided.\n🎯 This bot is exclusively for <b>VIP & special users</b>, giving you instant file access securely and privately!</blockquote></b>\n\n<b>•Join Our Main Channrl: @AniReal_Anime_Zone\nFore More Information Use /help</b>"
ABOUT_TXT = "<b>🤖 Kaoruko Waguri Bot - About</b>\n\n<b><blockquote>💡 Bot Status: <code>Online 24/7</code>\n🚀 Features: Instant Anime & File Access, Special Channel Links.\n🔗 Access: Get files directly via special links.\n⚡ Uptime: Always active for your convenience.\n🌐 Channels: Join to explore more anime content.</blockquote></b>\n<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href="https://t.me/AniReal_Support">Eʀᴇɴ Yᴇᴀɢᴇʀ</a> ◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ: <a href="https://t.me/AniReal_Anime_Zone">AniReal - Anime Zone</a> ◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/AniReal_Team">AniReal - Team</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>💖 Hᴇʟʟᴏ {first}!🥀\n\n<blockquote>I ᴀᴍ Kaoruko Waguri ✨ Your Personal Anime & File Access Bot🚀 I ᴄᴀɴ sᴀᴠᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ ᴄʜᴀɴɴᴇʟs🔗 & Gɪᴠᴇ ʏᴏᴜ ᴀᴄᴄᴇss via a Special Link</blockquote>\n<blockquote>🔰 Check Out Our Channels & Get Files Instantly! 🔰</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @AniReal_Anime_Zone</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
USER_ROAST_TEXT = "<b>ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ? Kɴᴏᴡ ʏᴏᴜʀ ᴘʟᴀᴄᴇ ғɪʀsᴛ.</b>"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
