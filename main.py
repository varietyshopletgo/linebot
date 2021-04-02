from flask import Flask, request, abort
import os
import adalo
import countdown
import information
import quick_reply
import random
import timetree
import replymsg
import facilities
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
    if event.message.text == "おーい、サボテン":
        result = replymsg.replymsg()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result))

    elif event.message.text == "そろそろ出かけようかな":
        result = facilities.facilities()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="OK！どこに行く？",quick_reply=QuickReply(result)))
    
    elif event.message.text == "近々なにかある？":
        result1 = timetree.get_timetree()
        result2 = timetree.get_msg()
        line_bot_api.reply_message(event.reply_token,[result1, result2]) 
    
    elif event.message.text == "今日はなんの日だっけ？":
        result1 = adalo.callapi()
        result2 = adalo.getmsg()
        line_bot_api.reply_message(event.reply_token,[result1, result2])
    
    elif event.message.text == "そういえば令和市が終わるまであと何日？":
        yourname = username_search(event)
        result1 = countdown.countdown()
        line_bot_api.reply_message(event.reply_token,result1)
    
    elif event.message.text == "ホームページとかどこだっけ？":
        result = snsmenu.sns()
        line_bot_api.reply_message(event.reply_token, result)
        
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)