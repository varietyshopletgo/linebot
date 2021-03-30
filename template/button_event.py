from linebot.models import (
    PostbackEvent, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, PostbackTemplateAction
)

class Additional_question:
    def question_a(self):
        button_template = TemplateSendMessage(
            alt_text="追加質問",
            template=ButtonsTemplate(
                title="質問１",
                text="あなたがピンチに陥ったとき",
                actions=[
                    PostbackTemplateAction(
                        label="頭脳であなたを助けてくれる",
                        data="question_b"
                    ),
                    PostbackTemplateAction(
                        label="体を張ってあなたを助けてくれる",
                        data="question_c"
                    )
                ]
            )
        )
        return button_template

    def question_b(self):
        button_template = TemplateSendMessage(
            alt_text="追加質問",
            template=ButtonsTemplate(
                title="質問２",
                text="あなたが大変なことをやらかしたとき",
                actions=[
                    PostbackTemplateAction(
                        label="優しくフォローしてほしい",
                        data="answer_d"
                    ),
                    PostbackTemplateAction(
                        label="体を張ってあなたを助けてくれる",
                        data="answer_e"
                    )
                ]
            )
        )
        return button_template

    def question_c(self):
        button_template = TemplateSendMessage(
            alt_text="追加質問",
            template=ButtonsTemplate(
                title="質問２",
                text="どちらのほうがタイプ？",
                actions=[
                    PostbackTemplateAction(
                        label="無愛想",
                        data="answer_f"
                    ),
                    PostbackTemplateAction(
                        label="フレンドリー",
                        data="answer_g"
                    )
                ]
            )
        )
        return button_template
    def answer_d(self):
        msg = "診断結果はｄです"
        return TemplateSendMessage(text=msg)
    def answer_e(self):
        msg = "診断結果はEです"
        return TemplateSendMessage(text=msg)
    def answer_f(self):
        msg = "診断結果はFです"
        return TemplateSendMessage(text=msg)

    def answer_g(self):
        msg = "診断結果はGです"
        return TemplateSendMessage(text=msg)