import os
import pya3rt
from linebot.models import (
    TextSendMessage, Sender
)
def talkapi(text):
    apikey = os.environ["TALK_API_KEY"]
    client = pya3rt.TalkClient(apikey)
    response = client.talk(text)
    msg = response['results'][0]['reply']
    snd= Sender(name="令和市公民館跡地のハムスター", icon_url="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/reiwa_hamstar.jpg")
    text_message = TextSendMessage(msg, sender=snd)
    return text_message