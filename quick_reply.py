from linebot.models import (
    MessageAction,QuickReplyButton
    )
def response_message():
    language_list = ["Ruby", "Python", "PHP", "Java", "C"]

    items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"{language}が好き")) for language in language_list]

    return items