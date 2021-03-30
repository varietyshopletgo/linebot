from flask import Flask, request, abort
import os
import adalo
import countdown
import information
import quick_reply

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,MessageAction, QuickReply
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "今日はなんの日？":
        result = adalo.callAPI()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result))
    elif event.message.text == "令和市が終わるまであと何日？":
        result = countdown.countdown()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=result))
    elif event.message.text == "施設一覧が見たい":
        result = information.information()
        line_bot_api.reply_message(event.reply_token,FlexSendMessage.new_from_json_dict(result))
    elif event.message.text == "サボテン話そう":
        result = quick_reply.response_message()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="どの言語が好きですか？", quick_reply=QuickReply(items=result)))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)