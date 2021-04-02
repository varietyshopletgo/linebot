#必要なライブラリを読み込む
import requests #APIリクエストに必要
import json #jsonを扱うのに必要
import datetime #時間をとってくるのに必要
import os
from linebot.models import (
    TextSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

def callapi():
    #変数各種設定
    normal_today = datetime.date.today() #2021-01-01
    today = str(normal_today) + 'T00:00:00.000Z' #2021-01-01T00:00:00.000Z

    # APIで令和市ホームページから情報をとってくる
    API_Endpoint = "https://api.adalo.com/v0/apps/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0/collections/t_c1ppsxdkptbbgkfglwcet1lbq"
    API_Key = os.environ["ADALO_ACCESS_TOKEN"]
    headers = {'Content-Type': 'application/json', 'Authorization':API_Key}
    result = requests.get(API_Endpoint, headers=headers).json()
    jsn = result['records']
    title = getValue(today, 'Name', jsn) #記念日の名前
    text_discription = getValue(today, 'discription', jsn) #記念日の説明
    message = '今日は' + title + 'だよ'
    text_msg = TextSendMessage(text=message)
    return text_msg
# とってきた情報(JSON)から必要な値を取り出す関数
# [{key:tokyo, value:apple}{key:chiba, value:banana}]こういう形のJSONだった。親キーがないパターン。
def getValue(today, value, items):
    values = [x[value] for x in items if 'New Property' in x and value in x and x['New Property'] == today]
    return values[0] if values else "なんでもない日"

def getmsg():
    buttons_template_message = TemplateSendMessage(
    alt_text='暦を見に行く？',
    template=ButtonsTemplate(
        text="暦を見に行く？",
        actions=[
            URIAction(
                label='ホームページに行く',
                uri='https://previewer.adalo.com/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0'
            )
        ]
    )
    )
    return buttons_template_message