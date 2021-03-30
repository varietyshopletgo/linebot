from linebot.models import (
    PostbackEvent, TextSendMessage, TemplateSendMessage,
    CarouselTemplate, ImageCarouselTemplate, PostbackTemplateAction,
    CarouselColumn, ImageCarouselColumn
)


def all_sns(self):
    carousel_template_message = TemplateSendMessage(
        alt_text="どこの様子を見に行こうか",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/164805270_470119047735471_3970313014321092495_n.jpg',
                    title='ホームページ',
                    text='記念日を入れたくなったらここかな。',
                    actions=[
                        URIAction(
                            label='Go',
                            uri='https://previewer.adalo.com/7e89d6b4-efb5-435c-8ea3-3822f4a7c5c0/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/165932370_775317893098235_6080044181924237203_n.jpg',
                    title='twitter',
                    text='フォローしておくとたまにtwitterのタイムラインに現れるよ。',
                    actions=[
                        URIAction(
                            label='Go',
                            uri='https://twitter.com/ReiwaCityNews'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/166060251_156255479701750_7248689856255699436_n.jpg',
                    title='note「令和市だより」',
                    text='もう説明は不必要な時代だけれど、背景の思いを知りたくなるときもあるよね。',
                    actions=[
                        URIAction(
                            label='Go',
                            uri='https://note.com/reiwacity/m/m5467a2ca46c6'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/166060251_156255479701750_7248689856255699436_n.jpg',
                    title='令和市民大学',
                    text='ありのままに見えている世界を共有したくなったらここかな。',
                    actions=[
                        URIAction(
                            label='Go',
                            uri='https://peraichi.com/landing_pages/view/r-university'
                        )
                    ]
                ),                        
            ]
        )
    )
    return carousel_template_message