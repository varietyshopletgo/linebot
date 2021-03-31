import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from linebot.models import (
    ImageSendMessage, TextSendMessage
)

def countdown():
    dt1 = datetime.datetime.now()
    dt2 = datetime.datetime(2021,7,24)
    dt3 = dt2 - dt1
    days = dt3.days + 2
    str_days = "今日はETA-" + str(days) + "。\n令和市が消滅するまであと" + str(days) +"日だよ"
    text_message = TextSendMessage(str_days)
    return text_message

def countdown2():
    dt1 = datetime.datetime.now()
    dt2 = datetime.datetime(2021,7,24)
    dt3 = dt2 - dt1
    days = dt3.days + 2
    str_day = str(days)
    return str_day

def add_centered_text(base_img, text, font_path, font_size, font_color, height):
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(base_img)
    draw.text(((base_img.size[0] - draw.textsize(text, font=font)[0]) / 2, height), text, font_color, font=font,)
    return base_img

def cd_imagemaker(str_day, yourname):
    #背景とアイコンのファイルを指定
    ogp_base_img_path = 'bg.png'

    #フォントを指定
    font_bold_path = "NotoSansJP-Bold.otf"
    font_medium_path = "NotoSansJP-Medium.otf"

    msg1 = 'ETA-' + str_days
    msg2 = 'for' + yourname
    base_img = Image.open(ogp_base_img_path).copy()
    base_img = add_centered_text(base_img, msg1, font_bold_path, 48, (48, 48, 48), 280)
    base_img = add_centered_text(base_img, msg2, font_medium_path, 22, (120, 120, 120), 580)

    return base_img
    #base_img.show()
    #base_img.save(cdimage.png)

def cd_sendmsg(strday, yourname):
    img_urls = cd_imagemaker
    image_message = ImageSendMessage(
        original_content_url=img_urls,
        preview_image_url= img_urls
    )
    return image_messege