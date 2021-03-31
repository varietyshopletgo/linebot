import requests
import os
import json
from datetime import datetime, timezone, timedelta
import dateutil.parser

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
    
    # UTC→JSTに時間を変換
    date_str.replace('Z', '+00:00')
    t = dateutil.parser.parse(date_str)
    JST = timezone(timedelta(hours=+9))
    t_jst = t.astimezone(JST)
    
    # 文章のパーツに必要な状態に整形
    tt_month = t_jst.strftime("%-m")
    tt_day = t_jst.strftime("%-d")
    ret = tt_month + '/' + tt_day
    for event in data['data']:
        tt_event = event['attributes']['title']
        tt_time = event['attributes']['start_at']
        tt_msg += time_jst(tt_time) + ' ' + tt_event + '\n'
    tt_longmsg = 'こんなの見つけたよ\n\n' + tt_msg
    
    return tt_longmsg