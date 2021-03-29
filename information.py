import json
import os
import requests
from linebot.models import (
   CarouselColumn, CarouselTemplate, FollowEvent,
   LocationMessage, MessageEvent, TemplateSendMessage,
   TextMessage, TextSendMessage, UnfollowEvent, URITemplateAction
)

# APIに接続するための情報
API_Endpoint = "https://api.adalo.com/v0/apps/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0/collections/t_afgpkmk2t6gcfqqbu80c7xm3a?offset=0&limit=100"
API_Key = os.environ["API_Key"]

# APIに送信する情報
headers = {'Content-Type': 'application/json', 'Authorization':API_Key}

# API接続の実行
result = requests.get(API_Endpoint, headers=headers).json()



#頭の'record'が邪魔
jsn = result['records']

Names = [i['Name'] for i in jsn]
urls = [i['url'] for i in jsn]
images = [i['image'] for i in jsn]
discriptions = [i['discription'] for i in jsn]

def handle_message():
	#カルーセルに渡す形に変換
  carousel_columns = [
        CarouselColumn(
            thumbnail_image_url=image,
            title=Name,
            text=discription,
            actions=[
                URITemplateAction(
                    label='遊びに行く',
                    uri=url,
                )
            ]
        ) for Name, url, image, discription in (
            zip(Names, urls, images, discriptions)
        )
    ]
  messages = TemplateSendMessage(alt_text="carousel template", template=CarouselTemplate(columns=carousel_columns))
  return messages