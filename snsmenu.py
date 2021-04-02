from linebot.models import (
    TemplateSendMessage, CarouselColumn, URIAction, CarouselTemplate
)

def sns():
    carousel_template_message = TemplateSendMessage(
        alt_text="どこの様子を見に行こうか",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/img_note.jpg',
                    title='note「令和市だより」',
                    text='もう説明は意味をなさなくなってきたけれど、行動の背景を知りたくなるときもあるよね',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://note.com/reiwacity/m/m5467a2ca46c6'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/img_twitter.jpg',
                    title='令和市twitter',
                    text='twitter上でも令和市の気配を感じたくなったらフォローしといて',
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
                    text='ありのままに見えている世界を共有したくなったらやっぱりここだな。誰かと話すっていいよね',
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
                    text='このHPってリモコンみたいだよね。記念日を入れたくなったらこちらへ',
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