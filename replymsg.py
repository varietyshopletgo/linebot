import random

def replymsg():
    words = ["はいよ！\nどうした？", "どうもどうも\nそういえば最近図書館行ってないな",
        "どうもどうも\nそういえば最近図書館行ってないな",
        "ほい\nサボテンって感じで書くとかっこよくない？\n仙人掌。",
        "寝てない寝てない\n今日はこれが終わるまでは寝ないって決めた",
        "本読んでたら寝ちゃってた\n本って一行だけ見えるようにして読むと頭に入ってくるよね",
        "はい！\nサボテンだよ",
        "ハロー\n深呼吸が必要そうな顔してるね\n\nはい、すってーー、吐いてーー",
        "ほいー\n結局なんだかんだいってソクラテスが全部説明してたじゃんって思うの、僕だけ？",
        "あれ？\n今何時？",
        "はろー\n気がついたら四字熟語の意味を調べまくっちゃうときってあるよね",
        "いやあ、さっき気づいたよ\n物語が不足してるわぁ",
        "うん\nひらめきと光ってどっちが速いんだろう",
        "たまにさ\nクラブに行きたいとかって思うことない？",
        "剛胆無比ってかっこいいよね\n他の者よりも抜きでて肝がすわっていて、思い切った行動をとる様のことを言うらしいよ",
        "一竜一猪って言葉、たまに思い出すよ\n努力して学ぶ者と学ばない者との間には、極めて大きな差ができるという意味",
        "言葉が先にあってそこから感覚を思い出すことってあるよね\nだから熟語って好きだな",
        "ぴえん。\n言ってみたかっただけ", 
        "おおお\nそろそろ新しい遊びを見つけたいな",
        "最近学びたい気分ー\n令和市って科学館か博物館あったっけ？",
        "やりたいことやればいいんだよ\nあ、意識飛んでた。おはよう。",
        "はいはいはーい\n今日はなんか無駄に元気",
        "調子いいときって調子乗ったらいいよね\nさっきそう思った",
        "ほい、呼んだ？",
        "この間さ、巨大数について調べてたら時間が溶けたよ\n数学ってやばいよね",
        "ぬわー\n今、明日何するか考えてた",
        "よろっと休憩行ってくるわ",
        "やっほ〜呼んでくれてありがとう！！どうしたの？",
        "なんだい？",
        "多くの人はアイデアは持ってない\nでも、考えは持ってるんだよ。",
        "その人と一緒にいるときの自分がいちばん好きだ",
        "「なんだ？　針でも飲むか？」",
        "やばっ、ごめん。なんか言った？",
        "まあ、みんなポンコツですからね。わたし筆頭にね（笑）"         
    ]
    msg = random.choice(words)
    return msg