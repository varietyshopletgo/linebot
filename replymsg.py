import random

def replymsg():
    words = [
        "はいよ！\nどうした？", 
        "どうもどうも",
        "ほい、呼んだ？",
        "ごめん。ケンタウロスは貸しちゃったんだ",    
        "はいはいはーい\n今日はなんか無駄に元気",            
        "魔界都市計画の相談だっけ？",
        "あ、意識飛んでた。おはよう。",         
        "やばっ、ごめん。なんか言った？",             
        "ハロー\n深呼吸が必要そうな顔してるね\n\nはい、すってーー、吐いてーー",
        "いいですね。魔都に追加しましょうか",
        "まあ、みんなポンコツですからね。わたし筆頭にね（笑）" ,
        "ドッペルゲンガーについて何か知ってたら教えてほしいなー"
    ]
    msg = random.choice(words)
    return msg

def kusoyarou_saboten():
    words = [
        "今ちょっと反応ないかも/nシステムは動いているから昔の返答が返ってくると思う"
    ]  
    msg = random.choice(words)
    return msg  
