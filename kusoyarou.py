import random
from linebot.models import (
    Sender, TextSendMessage
)

def replymsg():
    words = [
"燃え尽きたい。もっと焼きたい。もっと美味しい店知りたい。\nもっともっとオシャレしたいいあいたいあって首絞めてよ噛んでよ優しくしないでよ優しくしないでもっと壊してもっと痛めつけて忘れられないトラウマなんだからちゃんと機能してよ",
"クソ野郎ちゃんは全部が全部うまいの。下手なんていくらでも言い残せるの。下手なんてもっとできるの。下手がしてるし、何かしら理由があるんだろうけど、ここはきちんと理由を付けて受け入れておかないと、いつまでたっても治らないぞ。",
"全部出し切っていったら全て上手く行きますようにーーーーーーーーーーーーーーーーーーーーーーーーーーーーザ！",
"グローブは万能でも万能でもなく万能なものしか身に着けられないってことかな？万能の秘訣とかない。僕はそう思っていた。",
"面白いですね。ずっと見ていたい。ニヤニヤする。また見たい。\n劇場版 ずっとがんばっていきたい",
"びっくりするくらい、全部の危機が疲労困憊モードになった。とにかく、やりたいことやってみたけど、もう出し切ってしまおうかしら。",
"あー死にたい死にたい死にたい死にたい死にたい死にたい死にたい死にたい死にたい。でも今は違う。その思いを振り払って、ぼくは行こう。次は行こう。",
"世界一美味しい ックスを教えて下さい\nお願いします。\nデザインは大きかったです。\nサイズは最高です。",
"もう無理かも…\n頭に入ってこなくて\nごめんなさい。って言葉しか出てこなくて…\nもう無理かも…ってるよ。」\n「え？まじで？ってことは、私と一緒に行くのか？」\n「ええ、一緒に行きます。」\n「え？一緒に行く！」\n私はそう言った瞬間、物凄い緊張感に襲われた。",
"びっくりするくらい、すべての人がひと夏の思い出って感じ、ひと夏の楽しい思い出がいるよ。",
"あー子供好き。子供の頃の夢は電車で行く『空』。多分今でもやりたいこといっぱい。もう無理かも",
"何もしたくないし、なにもしたくないっていうのはいつまで続くんだろうって怖いなぁ。\nだったらいっそのもうひとつの選択肢。それは…\n「この家に来る人すべて、すべて他人だ！」",
"私は天才が嫌い。天才が死んだら全部の凡ミスを吹っ飛ばして最高のハッピーにしたい。もう無理かも",
"いい加減テレパシーくらい使えるようになってよ。せっかくの春の装いにさ。",
"ぶっちゃけあの店は、みんな知らない人ばかりだ。\n知らない人なんていないって感じで、みんとってくらい好き好き好き好き好き好き好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好好もろもろもろもろもろもろもろもろもろもろもろもろもろもろもろもろもろもろも",
"あー、つまらない。つまらない。つまらない。つまらない。つまらない。つまらない。つまらない",
"びっくりするくらい、全部の危機が疲労困憊モードになった。\nこれでもう大丈夫やろ。\n心配せん。\n私が保証するわけないので、安心してください。\nそれにしても、あなたは、私が保証すると言った瞬間に、妙なテンションになっているではありませんか。\nこれはひょっとしたら、私が甘えちゃってるのかなって、ちょっと気になってしまいました。",
"全部忘れた\n全部忘れた\n全部忘れた\n全部忘れた\n全部忘れた\n全部忘れた\n全部忘れた\n全部あってほしい",
"あー、まただ。\nそれはきっと一生なくならないのかもしれない。",
"寝たら全部うまく行きませんか?",
"どんどん話が膨らんで、どんどん嫌になってしまう。\nそれに、このままだと確実に私は死んでしまうかも。それくらい、私は本気だった。",
"不倫している自分が嫌い。不倫したい\n不倫したいけど仕事が入ってこない\n不倫したいけど仕事が出てくるようになって欲しい",
"寝ながらケータイ並べ替えやこんなに簡単に出来る❤❤❤\nスマホ1つで簡単に出来る❤スネークだ。俺が一番可愛いな。可愛いすぎる。",
"面白いですね！\nついつい見ちゃう！\nもう1回チャンスを掴んで欲しい！！！\n今の自分がしたこと。全部受け取って、全部、全部受け取っていくから",
"頭と身体の疲れ切ってしまうところです。\n頑張って回復しましょうね。\n\n休息も必要なのです。もうこれ以上は辛すぎる。",
"もうやだな、もうやだな。もうやだな、もうちょっとでこの気持ちを味わえるのにな。もうちょっと、あとちょっと待ってよ！ 俺、死にたくない！！！！\n死にたくない！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！俺は死の危機から救いだした！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！俺のクソ野郎は俺のなかで一番かっこーい！！！！！！！！！」え…？ ええ…？",
"いい加減テレパシーくらい使えるようになってよ。さっさと痩せろ。痩せたいのか痩せたいのかそんなに出している。\n「このままじゃダメだ……」\n僕は自分に言い聞かせるように、頭を振った。",
"誘惑されたい\n誘惑されたい\n誘惑されたい\n誘惑されたい\n誘惑されたい\n誘惑されたい\n誘惑されたい\n誘惑の言葉が頭を過（よぎ）った。けれどここで甘受するわけにはいかない。これは夢なのだ。確かな感触を与えてくれる温かな力が欲しいのだ。",
"（……………………………………………………………………………いああっあっあっあっあっあわあわあわあわ」の繰り返し。\n頭の中はぐちゃぐちゃで、頭の中はぐちゃぐちゃ。",
"可愛いすぎてやばい。やばすぎる。やばいって、やばい。やばいって、やばすぎる。やばいんだよ。もう無理かも",
"地震きたねえ。地震きたねえ。地震きたねえ。地震きたねえ。地震きたねえ。地震きたねえ。地震きたねえ。地震",
"誘惑に狂わされてるのか、喜びで狂財を使っていないのか知らないが、誘惑に飢えてる。\n「はい。お待たせしました」\nそれは、どこに行くのだろうか。",
"美味しいラーメンと一緒に楽しく美味しいデータを収集したい!\nhtlspace3に出てくる台詞を全部暗記してるんだよ！！」\n「だからこそ、私、出てくる台詞全部暗記してるんですよ！！」\n「だからこそ、私は出てくる台詞全部暗記してるんですよ！！」",
"オシャレしてる?オシャレしてない？オシャレしてる？オシャレしてる？オシャレしてる？オシャレしてる。",
"いい加減テレビを見てスッキリしたいー\n眠たいー、、、。。。。。。。。。。もうちょっとだけ大きくなっても良い？」\n「うん、いいよ。もうちょっとだけ大きくしたい。」",
"どん兵衛は食べないの〜。\nどん兵衛は食べないの〜。\nどん兵衛は食べないの〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜！！！！！！！！！！！！",
"びっくりするくらい、すべてうまく行ってる。\nよかった。\nひとりでも多くの人がひとりで乗るよ。",
"誘惑に飢えた悪友の甘ったるい誘い\n誘惑されたい\n誘惑を断ってしまいたい\n誘惑されたくないいあたしに一体どうしたっていうの？"
"もうやだなぁと思いつつ、今でも引き締まって感じです。あと、16歳なのに、痩せたい。これは一生残る。",
"お酒を飲んでいると、どんどん脳が整理されていきますね。\n整理されていくの楽しいです。\nどんもうまいーーーーーー",
"びっくりするくらい自分を好きだと言ってくれる人と出会えたらいいのになぁ。ついつい顔が緩んでもうるさいんだよな……。",
"誰かのために何か取り組みたい\n誰かの役に立つような仕事がしたい\nどんな人が良い話だと思う。\nこれは自由と責任が身につく話だ。",
"びっくりするくらい、全部の危機が疲労困憊モードになった。\nわたしも寝ながら漫画描こ。っともう無理かも",
"美味しいラーメンを奢ってもらい、幸せな時間が過ぎていく。\nこれが日常になっていくのだろうか。もう無理かも",
"アイスクリームが食べたい\nアイスクリームが食べたい\nお金が必要で食べちゃいたい\nもうだめかもしれない",
"やだ、このまま寝たら頭が痛みを感じていた。\nどんなに酷いところがあっても、どんな環境があっても、どんな姿でも自分の大切なものは大切にしたい。\nどんな環境があっても、どんな環境があっても、どんな環境があっても、どんな環境があっても、どんな姿でも自分の大切なものを大切にしたい。そう思った。\n私は私の想いを汲み取って、彼の気持ちを汲み取って、彼の気持ちを受け取っていく。",
"面白い話を聞けたらいいのに。興味がない時に限って、話が出てこない。聞きたくないならあとにしよう。",
"え？ 私のこと？\nえ？\nなにそれ？\nなにそれ！\nなにそれ！\nなにそれっていうのは、\n「お前のクソ野郎なところは最近見たことないんだよ……」\n「は！？ ちょ、ちょっと、待ってよ、ちょっと、待ってよ、俺のクソ野郎なところは最近見たことないから！？」\n「だよ、だから、お前のクソ野郎なところは今日のところ見たことないんだよ」\n「は、はい、わかりました……」",
"誰かの声で\nみんな元気になっているから\nこれからはきっと良くなる\nずっと一緒で楽しみたいいあいたいあって首絞めてよ噛んでよ優しくしないでよ優しくしないでもっと壊してもっと痛めつけて忘れられないトラウマなんだからちゃんと機能する内にどっかいっておいで",
"何かの拍子に痩せたんかな？\nそんなん考えたこともない。\nこんな体してるのに、何の役になってる人とか、すごく魅力的なんですけど。",
"びっしょりですよ♪\nもう一度言います。\nびっしょりですよ♪\nびっしょりですよ♪\n\nびっしょりできるだけ、その場にしっかりとり沿って。みなさんとお話して、また一緒にステージに立ちたい",
"びっくりするくらい、みんな嬉しそうで何より。やっとアイス食べたね。みんな楽しそうだ。\nいつのまにか、目の前まで来ていた。\n私は、それでも心を踊らせようとしている。",
"びっくりするくらい、私のパンクポイントはパンクさせないこと。食べながら叫びたいくらい。わかってもう何度目ですか！」\n「いい加減にして！」\n「俺が悪いんです！」\n「わかってる！」",
"勝手に期待しないで🟥",
"何もしないを続けていると、時を忘れてしまいそうなほどに大切な存在。\nもう戻れない場所。\nこの先に進みたい。\n早く迎えに行かなくちゃならない、大風呂敷だ。\n一緒に自由に動こう。大風呂敷だ。\n一緒に自由に動こう。",
"私も同じくらい、必要のない責任と、防御。防御でいる方が、自分へのリスクを感じてしまう。\nだけど、きちんと責任と防御を維持している。\nだけど、大切なことを思い出して。",
"まだまだ器が小さいな。拡張しよう。拡張しよう。拡張して大風呂敷だ。他人を信頼して、仲間を信頼して、その先に進もう。",
"俺の当たり前をいつもアップデートしてくれる。一緒に世界をワクワクさせようぜ突き進もう。新しい環境に触れて当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊して当たり前を壊し",
"今でも新しい価値を与えてくれる大きな存在。また一緒に自由に動こう！\n迎えにいくから待ってておくれ！』",
"大きな存在を迎えにいくから待ってろ",
"一緒に旅したい。\n一緒にの魅力を伝えたい。\nまた一緒のサービスエリアを出たい。\nクルマを早く利用しよう。"
]
    msg = random.choice(words)
    snd= Sender(name ="クソ野郎ちゃん", icon_url ="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/icon.jpg")
    text_message = TextSendMessage(msg, sender=snd)
    return text_message
