import requests
import os
import json
from datetime import datetime, timezone, timedelta
import dateutil.parser
from linebot.models import (
    TemplateSendMessage, ButtonsTemplate, URIAction
    
)


def getTimetree():
    # トークンの設定
    ACCESS_TOKEN = os.environ["TT_ACCESS_TOKEN"]

    # ヘッダーの設定
    headers = {
     'Accept': 'application/vnd.timetree.v1+json',
     'Authorization': 'Bearer ' + ACCESS_TOKEN
     }
    # エンドポイントの設定
    URL = 'https://timetreeapis.com/calendars/EGSvfRNr2Kw9/upcoming_events?timezone=Asia/Tokyo&days=7'
    
    # リクエスト
    r = requests.get(URL, headers=headers)
    data = r.json()
    tt_msg =""

    for event in data['data']:
        tt_event = event['attributes']['title']
        tt_time = event['attributes']['start_at']
        
        # UTC→JSTに時間を変換
        tt_time.replace('Z', '+00:00')
        t = dateutil.parser.parse(tt_time)
        JST = timezone(timedelta(hours=+9))
        t_jst = t.astimezone(JST)
        
        # 文章のパーツに必要な状態に整形
        tt_month = t_jst.strftime("%-m")
        tt_day = t_jst.strftime("%-d")
        ret = tt_month + '/' + tt_day        
        tt_msg += ret + ' ' + tt_event + '\n'
        tt_longmsg = tt_msg + 'があるらしい'
    
    return tt_longmsg

def tt_return_msg():
    buttons_template_message = TemplateSendMessage(
    alt_text='予定表見に行く？',
    template=ButtonsTemplate(
        text='気になる催し物あった？君もなにかするとき掲示したらいいよ。予想外の誰かが来たら面白そうじゃない？',
        actions=[
            URIAction(
                label='掲示スペースに立ち寄る',
                uri='https://timetr.ee/s/RrHpwO_-XUfL1DUmyFmWOCt-EvRdKx9K'
            )
        ]
    )
    )
    return buttons_template_message