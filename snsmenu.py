from linebot.models import (
    TemplateSendMessage, CarouselColumn, URIAction, CarouselTemplate, ImageCarouselTemplate,
    PostbackAction, ImageCarouselColumn
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
                    thumbnail_image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/marche.jpg',
                    title='令和市バーチャルマルシェ',
                    text='令和市のオンラインショップがオープンしたってよ。どんなグッズを作ってみようか',
                    actions=[
                        URIAction(
                            label='鑑賞しに行く',
                            uri='https://reiwacity.stores.jp/'
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

def callkusoyarou():
    image_carousel_template_message =TemplateSendMessage(
        alt_text='さっきそのあたりを散歩していたよ',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/9D5BAC09-322C-43A7-8FD0-3A50B30E9791.jpeg',
                    action=PostbackAction(
                        label='話しかける',
                        display_text='おーいクソ野郎ちゃん',
                        data='kusoyarou'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/029D5C09-00F2-48A5-BF6E-BE18E67628A7.jpeg',
                    action=URIAction(
                        label='吐き出しちゃえよ',
                        uri='https://zealous-chandrasekhar-8fae19.netlify.app/'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/B734762A-6EFC-479E-A94F-4851A1546677.jpeg',
                    action=URIAction(
                        label='noteを見に行く',
                        uri='https://note.com/_404_e_r_r_o_r_/m/m40a2ad85e1aa'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/BF42A81F-CE29-40A9-864D-1D428D269CC8.jpeg',
                    action=URIAction(
                        label='twitterを見に行く',
                        uri='https://twitter.com/_404_e_r_r_o_r_'
                    )
                ),                
            ]
        )
    )
    return image_carousel_template_message   