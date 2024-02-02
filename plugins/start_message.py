from pyrogram import *
from pyrogram.types import *
from pyrogram.errors.exceptions import *
from datetime import datetime, timezone
from persiantools.jdatetime import JalaliDateTime
from io import *
from dateutil import tz
import requests , json , time , qrcode , html , re , pytz

#------------------------------------- JSON INFO -------------------------------------#

with open('config.json', 'r', encoding='utf-8') as file:
    CONFIG = json.load(file)

ADMIN_TGBOT = int(CONFIG['admin_telegram_bot'])
PANEL_USER = CONFIG['marzban_panel_username']
PANEL_PASS = CONFIG['marzban_panel_password']
PANEL_DOMAIN = CONFIG['marzban_panel_domain']

#------------------------------------- ON MESSAGE & ONE LEN MESSAGE -------------------------------------#

@Client.on_message(filters.private & filters.command("start"))
async def START_MESSAGE (client: Client, message: Message) :
    CHATID = message.chat.id
    try :
        USER_FIRST_NAME = message.from_user.first_name
        if CHATID == ADMIN_TGBOT :
            TEXT = f"<b>درود رئیس 🙌🏻 به هولدربات خوش اومدی!❤️</b>\n\n\nشما در حال حاضر از نسخه ی <b>3.0</b> هولدربات استفاده میکنید ، جهت دریافت آپدیت و ویژگی های جدید با ستاره ⭐️ دادن به پروژه در <a href='https://github.com/erfjab/holderbot'>گیت هاب</a> ، مارو حمایت و تشویق کنید. <b>برای ریلیز آپدیت بعدی حداقل به 150 ستاره نیاز داریم...</b>\n\n\nچنل @ErfjabHolderbot جهت ارائه آموزش ها ، اطلاع رسانی های آپدیت ها ، نظرسنجی ها برای اضافه شدن ویژگی های جدید و از این قبیل تشکیل شده است.\n\n\nبرای هرگونه سوال ، گزارش باگ و پیشنهادات میتوانید در <a href='https://github.com/erfjab/holderbot/issues'>گیت هاب</a> ایشو کنید. ممنونیم 🫶🏻"
        else :
            TEXT = f"درود {USER_FIRST_NAME} عزیز\nجهت آمارگیری لطفا لینک خود را ارسال کنید."
        await client.send_message(chat_id=CHATID, text=TEXT, parse_mode=enums.ParseMode.HTML) 

    except Exception as e :
        ERROR_MESSAGE = f"<b>❌ ارور :</b>\n<code>{str(e)}</code>"
        await client.send_message(chat_id=CHATID, text=ERROR_MESSAGE, parse_mode=enums.ParseMode.HTML) 

    
