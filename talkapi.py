import os
import pya3rt
from linebot.models import (
    TextSendMessage
)
def talkapi(text):
    apikey = os.environ["TALK_API_KEY"]
    client = pya3rt.TalkClient(apikey)
    response = client.talk(text)
    msg = response['results'][0]['reply']
    text_message = TextSendMessage(msg, sender=["name"="令和市公民館跡地のハムスター", "icon_url"="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/reiwa_hamstar.jpg"])
    return text_message