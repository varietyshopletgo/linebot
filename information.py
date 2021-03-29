import json
import requests
from linebot.models import (
   CarouselColumn, CarouselTemplate, FollowEvent,
   LocationMessage, MessageEvent, TemplateSendMessage,
   TextMessage, TextSendMessage, UnfollowEvent, URITemplateAction
)

# APIに接続するための情報
API_Endpoint = "https://api.adalo.com/v0/apps/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0/collections/t_afgpkmk2t6gcfqqbu80c7xm3a?offset=0&limit=100"
API_Key = "Bearer cnlvj28xxxkfyam2kxjty6hqr"

# APIに送信する情報
headers = {'Content-Type': 'application/json', 'Authorization':API_Key}

# API接続の実行
result = requests.get(API_Endpoint, headers=headers).json()

#頭の'record'が邪魔
jsn = result['records']

def handle_message():
	#カルーセルに渡す形に変換
	columns = [
        CarouselColumn(
            thumbnail_image_url=column["image"],
            title=column["Name"],
            text=column["discription"],
            actions=[
                URITemplateAction(
                    label='遊びに行く',
                    uri=column["url"],
                )
            ]
        )
        for column in jsn
    ]


	#メッセージ作成
	messages = TemplateSendMessage(alt_text="料理について提案しまた。", template=CarouselTemplate(columns=columns))
	return messages