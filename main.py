from flask import Flask, request, abort
import os
import adalo
import countdown
import information
import quick_reply
import random
import timetree
from template import button_event
from template import carousel_event

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,MessageAction,
    QuickReply, PostbackEvent,CarouselTemplate, ImageCarouselTemplate,
    CarouselColumn, ImageCarouselColumn,QuickReplyButton, URIAction,TemplateSendMessage
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

#新しいLinebotApi instanceをつくる
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# メッセージが返ってきたときの反応
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if event.message.text == "今日はなんの日だっけ？":
        result1 = adalo.callAPI()
        result2 = adalo.get_msg()
        line_bot_api.reply_message(event.reply_token,[result1, result2])
    elif event.message.text == "おーい、サボテン":
        result = saboten()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result))
    elif event.message.text == "そういえば令和市が終わるまであと何日？":
        yourname = username_search(event)
        result1 = countdown.countdown()
        #str_day = countdown.countdown2()
        #result2 = countdown.cd_sendmsg() #(str_day,yourname)
        line_bot_api.reply_message(event.reply_token,result1)
    elif event.message.text == "近々なにかある？":
        result1 = timetree.get_timetree()
        result2 = timetree.get_msg()
        line_bot_api.reply_message(event.reply_token,[result1, result2]) #,
    elif event.message.text == "サボテン話そう":
        result = quick_reply.response_message()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="どの言語が好きですか？", quick_reply=QuickReply(items=result)))
    elif event.message.text == "執事診断":
        line_bot_api.reply_message(event.reply_token,button_event.Additional_question().question_a())
    elif event.message.text == "ホームページとかどこだっけ？":
        result = all_sns()
        line_bot_api.reply_message(event.reply_token, result)
    elif event.message.text == "そろそろ出かけようかな":
        result = response_message()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="OK！今日はどこに行く？",quick_reply=QuickReply(result)))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

#値が返って来たときの反応
@handler.add(PostbackEvent)
def on_postback(event):
    reply_token = event.reply_token
    user_id = event.source.user_id

    #postback_msg : method名を文字列で
    postback_msg = event.postback.data

    #additional_question : classオブジェクト
    additional_question = button_event.Additional_question()

    #クラスオブジェクトと文字列で取得したメソッド名から、メソッドオブジェクトを作成
    question = getattr(additional_question, postback_msg)
    line_bot_api.reply_message(event.reply_token, question())

def response_message():
  places = ['令和市民大学', '令和市みらいの文化センター', 'ふぃろと愉快な仲間たち', '令和市note直通特急', '思考の渦', 'ゆかりの部屋', '令和他力本願寺',  '蟹家飯店', '令和市郵便局', '令和市立病院', '【DDD】', 'しさく公園', '令和市デジタル庁澪標研究棟']

  urls = ['https://line.me/ti/g2/27Ul0_tr-YyDMHIgzCS7Ow?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/7DHG49ErBIh5npZ_gZd5jw?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/XvISahCX8Yt0b6TPTC1DPA?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/1fG-xDlclF4CXt-8k3n_jQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://discord.gg/A6NbcNnFY6', 'https://line.me/ti/g2/x3tNKIam9FfbcR7LgR980Q?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/tl4x1jhp7wuJovem38W8yw?utm_source=invitation&utm_medium=link_copy&utm_campaign=default',  'https://line.me/ti/g2/ug0rKcEWvPtiOVj2u-P3hw?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/Jl9udQeJtpSZaNs5OGsONg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/aPdxTIf03gvb9_g-gqMpXQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/BXMu9SDB6ow8DIACeLsnzQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/W4k67QKcAi36NfciiTsDpg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default', 'https://line.me/ti/g2/6ZT9AW-wGagQ8cfiMkm3DQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default']

  items = [ QuickReplyButton(
        action=URIAction(
            label=f"{place}", uri=f"{url}"
            )
        ) for place, url in zip(places, urls)]
  return items

def saboten():
    words = ["起きてたよ。\nなんか言った？", "hello\nhello"]
    sleepy_word = random.choice(words)
    return sleepy_word

def all_sns():
    carousel_template_message = TemplateSendMessage(
        alt_text="どこの様子を見に行こうか",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/img_note.jpg',
                    title='note「令和市だより」',
                    text='もう説明は意味をなさなくなってきたけれど、行動の背景を知りたくなるときもあるよね。',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://note.com/reiwacity/m/m5467a2ca46c6'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/img_twitter.jpg',
                    title='twitter',
                    text='twitter上でも令和市の気配を感じたくなったらフォローしといて。',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://twitter.com/ReiwaCityNews'
                        )
                    ]
                ),

                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/img_college.jpg',
                    title='令和市民大学',
                    text='ありのままに見えている世界を共有したくなったらやっぱりここだな。誰かと話すっていいよね。',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://peraichi.com/landing_pages/view/r-university'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/164805270_470119047735471_3970313014321092495_n.jpg',
                    title='ホームページ',
                    text='このHP、リモコンみたいだよね。記念日を入れたくなったらこちらへ。',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://previewer.adalo.com/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0/'
                        )
                    ]
                )               
            ]
        )
    )
    return carousel_template_message

def username_search(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    yourname = profile.display_name
    return yourname

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)