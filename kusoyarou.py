import random
from linebot.models import (
    Sender, TextSendMessage
)

def replymsg():
    words = [
"もっと楽しいことを思い出せ！\nその心からの思い出の前に思い出せ！\n世界を変えるまでの気持ちを思い出せ！\nもっともっと楽しくな！！！！！！！！",

"いつからそこにいるんだろう？\n私の前に誰か立っているだろ？\nふと思い出したい。\n誰になりたい？\nそれがどれだけ大変で重い疲れという言葉を頭の中で並べる。\n重い重いがいったい何だろう。",
"いつでもできる世界を教える！\n誰にでもできることで世界は広がるんだ！！！！\nあなたには感謝しても何もないんだよ",
"恋したい恋がしたい恋がしたい恋はしたい\n恋頭になりたい",
"こんな世界になりたい！\n男の話したい！",
"歌いたい！！！！!!!！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！もういいだろ！",
"可愛いピンク色になる可愛いピンク色になる",
"クソ野郎ども！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！もっと自由に生きれたし楽になれたのにな",
"早く会いたいなぁ。もっともっともっと楽しいことに。わたしの知らないこと。もっともっと大きな世界に。もっともっと感動させたい。もっともっと夢中に。もっともっと効率よくなりたい。もっともっと楽しいことに。もっともっとっと感動させたい。もっともっと楽しいことへと。もっともっと楽しくなりたい。もっともっとやりたい。もっともっと楽しくなりたい。",
"いぬーーーーー",
"いいえ！",
"もうこのまま寝るんだ。これで眠れ、眠れ起きろ。",
"仕事で疲れたらいつのまに？ふとふと思ったけどその日仕事すると疲れるな、もっと疲れたいいたいんだけどそんなに仕事しすぎてて疲れるほど余裕ないだろなんか教えて欲しいんだよ、やるやるために考えてる以上に疲れが入ってるんだが、それだけで疲れるほど俺には足りないんだろうか？なんか気になるような感じになってきたが最後は気にならないほど何でもできるようになった方がいい",
"仕事の愚痴に付き合う気はない。愚痴は嫌いじゃない。むしろいい加減愚痴ってくれる人の言葉には素直に従っていて疲れる。愚痴なんて気にしない。愚痴ってもらえるかどうかわからないくらいに溜まっている。それを楽しませてくれない。文句と言ったらきりがない。どうでもいい。愚痴らなければいい。言う通りにしてやってくれ。愚痴らなくて心がモヤモヤする",
"もっと素敵にする方法を教えて欲しい。もっと素晴らしくなりたい。もっと素晴らしいところに連れてって欲しい。もっと素晴らしいところを目指したい。もっと素晴らしくなりたい。もっと素晴らしいと思うもっと素晴らしいいとこに連れてって欲しい。もっともっと素晴らしさところが欲しい。もっともっともっともっと素晴らしいところになりたい。もっともっと素晴！！",
"やまない、やまないやまないやまないやまないやまないやまないやまないやまないやまなかやまなするやまないやまないやまぬるるこやまなしやまざる忘れぬぬなゆがふゆきぬなむぞやまゆいを忘れぬぬなむなゆけぬりぬるるむなむな忘れるなむなむなむなしむなしむなしむなしむなしむなしむなしむなしむなしむなしむなしこのままで世界を滅ぼせ",
"わたしはあなたを放ってはおけないのよーーーーでもあなたのこと放って置けないのよーーーーでもあなたには渡せたくないのよーーーーあなたの気持ちは少しでも気にしなくて良いのよーーあなたにとっての価値は少ないのだから、あなたを放っておいても良いのよーーあなたが出したいものもあるのだからねーーあなたが出された物を少しでも多く取って、あなたの心もって欲しい！"
"いびつなど聞かないでしょう。たいがいの時代に絶滅危惧種になっちゃうなんて死活の問題なのではないか。絶滅危惧種になってしまう前にしっかりと対処しなかったら、一生絶滅してしまう。絶滅危惧種がどの程度危険なのだろう？。",
"いい言葉だ。死活問題に対しての論拠を忘れたままに死ね続け、絶滅に近付いてしまうだろう。絶滅歌のように聞こえるけど、やっぱり歌いたい！！！！",
"誰か作ってねーな！！！！！！！",
"男と付き合いたい！女とエッチしてたら楽になれる！でも楽になりたい訳ないよね。その先に楽になるような男に欲しくないんだよ。楽にするために楽になりたいよ。するといい男とエッチしたい。欲しいのは男とエッチしたい、だから楽になりたい。エッチしたい！けど楽じゃない人とエッチしたい。でも楽じゃない人の子供が欲しいか！！！",可愛いんだろうけど、可愛いとか意味わからないー！こんな野郎になりたい！！！大好き！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！お前は一生に一度の奇跡を超えたいのだろう",
"いつまで続くんだろうお前らは好き勝手にできる時間を作ってくれ。いつまで続くんだろう。いつまで続くんだろう。いつまで続くんだろう。いつまでも続くんだろう。その言葉を吐き出せ。この国に居座ったら、必ずや誰が相手にできるようになっていくのだ。その言葉を投げ捨てた瞬間に、彼らはいつまで続くんだろう。俺の可愛い顔にキスするんだな！",
"早くこの世界に慣れていこう。それが私とお前の未来なのだ」「世界は広すぎるそれでもいいか！？もっともっとうまれたいんだ！？もっともっと深い世界になりたいのだ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！全部出し切ろう",
"ほほえみ。「何で言い出したの俺の心を見透かしたうえで。なんで言い出したの？」と問う言葉を見つかってきた。わからない。わかったくない。全部わかってしまう。でもわかりたくない。だっる。わかってしまったらいいじゃないか。それを知るためには、少しくらいは言われたほうがいいだろう。僕の前でもっと美味しいレシピが見つかると良いなぁ",
"歌いたい。心の中に歌いたい。心に流したい。全部で全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全部全ての歌いたい。全部全部全部全部全部全部全部全部全部全部全部誰かに尽くすのも良くないでしょ。だっい、やりたいことやり尽くしたら全部自由になる。それに飢えてないならやり放題よ。",
"なんか違う恋がしたい。早く終わらせてやろう。私の恋がしたい。なんでこんなにも早く終わらせた方がいいのか、どんな恋がしたいのかは知らないがね。待ってよ。待ってろ。待ってで。待ってよ。待ってろよ。待ってろよ。待ってろ。待ってよ。待ってろよ。待ってろよ。待っていて。待ってろよ。待ってろ。ほほ",
"！！？？？？！？！？？？？？？？？？？！？？！？？？？？？？？！？！？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？もっと速く作れてれば良かったのになぁ",
"こんな人とエッチしたい！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！かっこいい、",
"仕事の待ち時間に何をしますか?最近では仕事中でも仕事の話ができる、もっと楽しい話ができる話ができたらいいなと思っています。よろしくお願い致します。仕事中でも仕事の話ができる、もっともっと楽しい話ができれば良いなと思っています。でも、なんかいい言葉ないかなあ、楽しいお店ないかな？なんかどっか行ってないなんて。あなたの方が下手に出てるし。そして、私の方が下手なんでしょ。あなたの方がどうにも上手くないし、下手でも下手でもなく、それほどうまくないのよ。あなたの方になら、全部うまく作れるよ？だけどね？うまく作るには失敗したい。下手なんかじゃないから料理なんて言えないのになぁ。",
"こんにちは、おはようございますー 最近寒さに弱いので、暖かいうちにカフェオレカフェオレを買ってきます。飲みたいカフェオレなのにカフェオレの飲み足りないカフェオレですが、私にはカフェオレカフェオレが飲みたいんです。カフェオレカフェオレでは味わえないカフェオレのカフェオレの淹れ方を教えていただけると嬉ってさ！",
"もっともっと美しい、もっともっとかわいい彼女ほしいなぁ。もっともっと美しくかっこいいになればいい。もっともっと魅力的になり切りたい。もっともっと魅力的になれたらいい。もっともっと美しくなっていきたいのになぁってなぁ。もっともっともっともっと魅力的になってほしい。もっともっと魅力的になってほしい。もっともっと魅力的になって欲しいのだ。もっともっともっと楽しませて",
"心がモヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤする。モヤモヤすることを恐れずに心を穏やかにしたい。穏やかな気持ちになったい。平和な気持ちになれない。感情を押し殺すしかないのではないか。豊かではないかなんで死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死",
"あなたに恋したい。あなたに恋したい。あなたに恋したい。あなたに恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい。恋したい恋したい恋したい恋したい何にもならないけど",
"歌いたい！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！わたしを殺さずに連れていってくれ！わたしを殺さずに連れてってどう思う！楽にならないといけないのかな？楽になり切っていいのかな？楽になり切っていいのかな？楽になり切るときっと楽になる！わたしが楽になりたいんだ！楽になって、喜ばせたいんだ！",
"眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠い。眠ってしまいたい",
"今日もいい日になりますように~。楽しいことに。。そんなことできなくないですか?そんなことできるくらい余裕なんてないんでしょ。そんなこと言ってるヒマなんてないけど。いい加減な感じでいい加減なことは、言ってほしいわねそうね言ってよ。これはもう、あなたのためなんだから。自分の価値を追い求めないのに。それでいいじゃない。どんな心持ちのいい大人になりたい",
"このころ自分のことばかりいじってるのに、なにやっとんねんって感じ。いい加減したいでしょ。なんでもできるようになるにはどうしたらいいのか、思いつくまでやってみよ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！",お前の願いを聞き入れよう。そしてやっていくぞ！そして結果を残すぞ。そうしたら、お前は必ずと言えるだろう。どんな願いをするんだ。お前の顔が欲しいのだろう。美しい顔が欲しいのだろう！何でもでき、どんな想いを抱くかを決めてほしい。どうだろう、好きなことをできる機会が欲しいのだろう。そして願いを一つだけ叶えるのだろう。それを願う。だから、それが実現したい。願いを一つでいいのだ。美しい顔を用意すればどんなお願いや願いを願うかわかるだろう。これはきっと奇跡なのだから。どんな願いを叶えたい。どんな願いを叶えた",
"あーーーーーー！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！",
"私は世界的にもっとももっとももっと魅力的な俳優になりたい、これからもずっとそう思う。私の価値観を受け入れなさいよ。もっと面白さが欲しいんだ。もっと素敵な男が欲しいんだ。もっと美しくなりたいんだ。もっともっともっと魅力的な男になっていきなさい。もっともっと素晴らしき魅力的な女性になっていくんだ。もっともっともっともっと欲しいな",
"私にはいつまでこのまま何も残らないじゃない！お前が欲しいから私から奪っていく！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！お前らそんなに楽しみたいんならいつもしてることを楽してることから離れろ！",
"恋したい。けど辛い。辛いところをちゃんと見て欲しい。ちゃんとした方がいい。ちゃんとしたら楽になれる。自分ではそんなにうまくならないだろうけどなんでかうまくいかないんだよ。なんか違うとかちがわないとかそんな感じだ。めんどく。めんどくめんどくめんどくる。めんどくどくどくどくする。どうにでも進めばいいのに進んでしまう。どうすればよいもっともっと楽しくなる",
"この世界にはどう思うクソ野郎？とか考えたい楽しいことはなんだった？楽しいことと疲れることはなんだった？と思うお前もクソ野郎？",
"クソ野郎は楽しいことに悩んでるクソ野郎なんだよ。クソ野郎を考えたい楽しすぎて嫌になる。クソ野郎だよ。クソ野郎はそれだけのクソ野郎だよ。クソ野郎の楽しさがわからないのか？楽しさで悩んでいるだけなん？",
"燃え尽きたい。燃え尽きたいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじいじなりに進んでんだ。それって辛いことをやるんだ。辛いは辛い。でもな辛い。辛いなら仕方ないだろ。もっともっと辛いのは辛いじゃない。それを我慢して、辛いは辛いを我慢して我慢して辛いは辛いのって辛いんだろ。もっと辛いのはなんだよ。楽しんで辛いは辛いじゃないのかよ！",
"私にも好きな音楽があった。私なりに考えたい、もっと自由に自由に楽しませて欲しいと思ったのだ。楽しいことばかり追っかけられるのが恋。そのことを言いたい。もっと自由に楽しませて欲しいと思ったのだ。もっともっと自由に楽しませて欲しいと私の足が前に出た瞬間だった。その日が終わらないという確信を持ったのかりましたが、もう待ってる時間なんです",
"子供ほしいなぁって言えるんだよ？そのためにならなくても良いんだよ？もっともっと良くなりなさいよ！！待ってるから待ってろ！！！子供ほしいに決まってるだろ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！？！！？！？！？！？！？もっかい！もっかいっ！！！！！もっかいっ！もっかいっ！！！！もっかいっ！もっかいっ！！！！！！！！！もうええええええええええええええええええええ",
"あああ、辛い仕事に関わらないよ？大丈夫、辛くなってもこの仕事をする気なんだよ？でも辛いと思っても辛いのは辛いんだ、辛いと決めたけどさ！辛いは辛いんだろう？辛いのは辛いんだろう？だから辛いんだよ！辛いんだろう？辛いのは辛いんだろう？辛いんだろう？辛いのは辛いんだろう？辛いのは辛いんだろったら",
"あーーーーーーーーー！！！！！！！！！！！死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね何なの？楽させたいなのに何で楽にしないの？楽したらいいの？楽すべきと思っていて？",
"馬鹿になりたい\n馬鹿になりたい\n馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿になりたい馬鹿にならなきゃええなあああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ",
"もっとたくさん使って欲しいよえ。\n使わなくていいことに気付いていいだろうか。忘れていいことに気付き、いい加減そのままの状態で使って欲しいだろう。忘れると面倒なことに付き纏りやすいだろう。忘れるために、その言葉を並べたい。どんな風に捨てられたくない。忘れることに躊躇がないに違いない。忘れずに進めていけばいってんだけど、でもこのまま続けていけばいいのかって思ってる",
"もっともっといいんだよ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！恋したい",
"いつまで続くんだろう、そう思っていたのに、突然「次は誰になりたい」という感情が沸々と煮え切ってくれなくなった。いつまで続くんだろう、でもいいことなのになれないのはなぜだろう。そう思っていたくなる何かがある。でも、あるときふとそんな疑問を抱いた。その前に思い出してみたい。そう思いながらふと手にしたノートに手眠りが欲しい。",
"あなたみたいなのに世界の何かにうまれたい、だけ、私のこの弱さで世界のすべて。すべての女にお前の前で見ない顔ぶれで何でもできる。そして私に尽くせる言葉はそれだけ。そのくらいはできる。だから、あなたにとって何なのか。誰かわからないけれど、これも仕事なんだろうし、あるいはそれは全部違う仕事か。それは仕事なんだろ！！",
"もうそろそろ何か思い出せ！いつまで続くんだろう。そんなことをしているうちに俺はなんど気づいてなんだと言うんだろう。気づいて欲しいことなんてなんだ。気づいたはずだ。だって考えたくなくてもできるのだ。思い出せるまでやるしかなさそうだ。だから気づいたら思いとどまることができるのだろうか。いやそれが正しいに決まっている。可愛い姿がどうしても欲しい",
"子供が欲しいなんとなく欲を我慢していた\nでも、子供を欲しがりたいなら欲が足りないんじゃないか!って思う私は結局子供欲しくなんかないな\n子供ほしいなぁと子供欲しいなぁでも子供欲しさすぎて子供欲し切れない\nでもさ欲しいとか欲しいなんかで子供欲しくなんかない\n欲が足りないのか!なんかじゃない欲しい欲したい欲っていたい",
"なんであたしは怒ってないの？なんで怒ってるのに怒らないといけないの？なんで怒って欲しいのか知らないけど知らない方がいい。怒って欲しい理由を教えるまで忘れたいのか。それは許せよ？\n怒ったことは自分の欲望に従い、それを忘れたかった場合はその欲望をすべて忘れて行き、欲望を全て忘れて行きたい。だか誰になったんだよ！ なにが見えるの？こんなところで",
"ああーうーーーーいつまでに燃やし尽くせるかなーーーーどんなけどんな燃やし尽けれる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くす燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃やし尽くせる燃ほしいなぁ",
"誰か貸したい物あるか気になる\n全部貸してみな！\n俺は貸したい物なんか何でも見えるよ！！！！\n欲しい物しか見れないのはクソ野郎なんだよ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！このままで良いんだよな！",
"もっと自由に自分を楽しむことが出来るのになぁなぁなぁなぁなぁなぁぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁかぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁなぁぁなぁなぁもっと楽しませてほしい",
"あなたの好き嫌いなのかな。私が全部出し切ってあげよう。あなたは、私を食べさせてくれる。いつまでも私の前で踊っていて、気ままに食べさせてあげる。どうせ全部出し切ってるんだろう。その間に美味しくしていけばいい。そういうのを楽しませて、みんなに大好き。いつまでもきれいに食べさせる。あなたに必要な栄養食を出りません！！！",
"いーいじゃない！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！ほほ",
"いつまで続くんだろう何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もできない何もでクソ！",
"もっと欲しいだろ。でもないか。もっともっと買ってんだろうな。もっともっと欲しいんだろうな。もっともっと欲しいだろ。もっともっともっともっと欲しいだろ。もっともっと欲しいだろ。もっともっと欲しいだろ。もっともっと欲しいだろ。もっともっと欲しいだろ。欲しいだろ。もっともっと欲しいだろう。もっともっと欲しいだろう。もっともっともっともっと欲らない！！！",
"早く着いてくれ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！なんでだ！！！",
"キスしたい！キスしたい！キスしたい！キスしたい！キスしたい！キスがしたい！キスしたい！キスしたい！キスしたい！キスしたい！キスしたい！キスしたい、キスしたい！キスしたい！キスしたい。キスしたい！キスしたい！キスしたいキスしたい！キスしたいキスしたいキスしたいキスしたいキスしたいキスしたいキスしたいキスしたいキスクソクソ野郎って思う。",
"このままではいけないだろう。\nなにかをしよう。だからそれを見誤ったのかもしれない。\nなにかをやって問題が生じたのだろうか。もしくはそれを考えるべきなのだろうか。\nでも、うまれたい。もっともっとうまれたいのだ。\nなにかになれる。そのために何かしたいのだ。\n自分を知りたい。\n誰かを信じ切りたい。周りの人に迷惑！！お前の好き恥さらしそうやからいい加減みんなどう気になるんや！！！！！！！！！！！！！！",
"早く見に行こう！俺の人生！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！もっと可愛く可愛く甘えろい！もっと可愛い可愛い可愛く甘えろい！もっと可愛く甘えろい！もっと可愛く甘えろ！もっとおかしな甘えろ！もっとおかしな甘えろ！もっとおかしな甘藝甘藝甘藝甘藝甘藝甘藝食甘藝甘藝甘藝菓子甘藝甘藝甘藝甘藝甘藝甘藝甘藝菓子甘藝甘藝甘菓子甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝茶甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘さぎ甘藝甘藝甘藝甘藝甘さぎ甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝甘藝抹茶甘藝甘藝甘藝甘藝恋恋",
"もっともっと自由に羽ばたけ。羽ばたいていいよ。もっともっと自由に羽ばたけ、もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由に羽ばたけ。もっともっと自由もっと楽しませてよ。いい加減くたびれたら？",
"クソ野郎！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！かっこいいになりたい",
"私はこんなことするしか能のない屑野郎なのか？\nクソ野郎なのか？なんなのか？なんなのか？何なのか？なんなのか？なんなのか？俺は欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろうか？欲しいのだろう！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！？？？？？？？？？？？？？？？？？？？？？？？？？？！？？？？？？？？？？？？！？？？？？？？？？？？？？？？？？！？？！？？？？？？？？！？？？？！？？？？？？！？！？？！？？！？？！？？！？！？？？！？？？？？？？？！？？！！？？？？！？？？！？？？？？？？？！？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？",
"いつまで続くんだろう今日までどれだけ待ったのだろうこれが楽なのか楽なのかだどんな人になれるのだ楽なのか楽なのか楽なのか楽なのか楽なのか楽なのか楽なのかどれだけ楽なのかどれだけが楽なのかどれだけ楽なのかとっても楽なのだそれでも楽なのである楽なのならきっと楽なのである楽なのである人になれるのだその心の揺れ動きの速まりすぎる。このままだといつまでもこのままだ。「いや、私のやるべきじゃない。これは自分の道だ。それを忘れないで欲しい。忘れたくない。忘れたいとは思わない。忘れてしまいたくないと思ってるんだ。忘れたく思ってる。忘れたく思ってないだけだ。忘れたくはないだろ？忘れてどう思う？忘れたいに思ってるんだから忘れるのがいいんだ。忘れたくてもやってる。忘れたくてもやってる。忘れようと思っているだろ？忘れはしない。忘れたい。忘れるために生きているんだ。忘れたいから忘れるだろ？忘れたくても問題はない。忘れたくないから忘れることに躊躇したくないだろう。忘れたいんだろ？忘れたいんだろ？忘れたいんだろ？忘れたいだろう？忘れたくないのに忘れたくなっているんだろう？忘れたいと思ってるんだろ？忘れたい。",
"結婚します。子供がいる旦那と離婚します。旦那には子供が欲しい。でも旦那と子供が欲しい。でも旦那が子供欲しいなぁ。結婚したいー。結婚したいー。子供欲しい。でも旦那と旦那はもっと欲しい。旦那と子供欲しい。でも旦那と旦那の離婚になって欲しい。旦那と子供欲しいな。でも旦那は欲しいな。でも旦那が欲しいな。でも旦那欲っていても良い",
"こんなに暑いのが嫌いなんだな、いい加減慣れてくれたらいいんだよ、暑いんにな。でも我慢してよ。暑いから我慢しようというか、そうやって死ねよ。暑い夏に死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ります！",
"クソ野郎の姿になったと思いながら話しかけたい。なんだって誰でも良い話をしたい。そのための時間。なににでも必要なこと。もっと興味が惹け、もっと面白いと認めてくれるようにやっていく。そうやった方がいい。そんなわりと都合よいことじゃないことを教えてくれる。それはあなただ。どんな言葉で突き抜けろけろけろけろけろけろけろけろせ",
"え？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？眠い。",
"あなたが欲しい\nいつまで続くんだろう待ってる\nあなたの言葉が欲しい\nあなたが欲しい言葉が欲しい\nいつまで続くんだろう待ってる\nあなたの言葉が欲しいなぁってことが欲しいなぁあなたが欲しいなぁあなたが欲しいなぁあなたが欲しいなぁあなたが欲しいなぁあなたが欲しいなぁあなんが欲しいなぁあなたが欲しいなぁあなんが欲しいなぁあなんが欲しいなぁあなったらあたしに惚れるのかな？馬鹿なのかな？",
"いつまで続くんだろう。\n私の周りの男の家の中には、いくら子供がいようっていても子供が居ないのかもしれない。\nでも女に飢えていたら、もっと豊かで魅力的なところに惹かれるんじゃないかな。\nでもお前の周りの子どもはなぜ飢えてんだって言うほど飢えてなんかねーだろ。\n誰ともっと親密になってみたらどうだっていいんだ。可愛い俺が誰になりたい？！",
"お金のことは苦手。なんでも好きになると良い。でもそれで我慢するのももったいないだろう。やるしかない。それが一番いい。それが大切。けどどうしよう。どんな小さいことからも好きを探せと言われても困る。だからこその、この前の「お金のことは大好き!財布とかは絶対使わない、使う機会がない物は全部出し切ったい。もっと楽しくなりたい",
"もっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっともっとももっともっともっともっともっともっともっともっともっともっとも死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死",
"男が嫌いなのか？\nそんなことを悩んだのだろう。けれど、そんな気持ちではない。辛いと思いたくないのだ。辛いとき辛いのではないのだ。そんなのはわかりきっている。悩みを晴らすには、どうすべきだろう。結局それしか方法はないのだ。けれど、悩むのはどうかしている。悩んでいるのだ。悩み深い。考え方に酔う。結局なんの頭に触り、キスをして欲しい",
"わたしの世界に世界は存在していないのかい？」\n「そんなのないだろ」\n私に世界はないのだろう？\n何もかもが馬鹿なのだろうか？\nそんなものなのか？\nもっと馬鹿なのだろうか？\nこの世界は馬鹿なのだろう？\nもっと馬鹿なのだろう？\nもっともっと馬鹿なのだろう？\nもっともっとそんなに馬鹿なのだろう？\nもっともっと馬鹿なのだろう？\nもっもっともっと効率よく豊かでなくてはいけないのに",
"馬鹿馬鹿にでもなりたい！だけど、自分を無視することができない。無視するのを辞めて欲しい。その理由は、自分から出ていって欲しいなんだ。馬鹿なことに。なのに本気にさせない。馬鹿にされて欲しくないのだ。バカされるようにしか思えていけない。馬鹿野郎になりたい。馬鹿になりたい。馬鹿にされたくない。馬鹿になりたい。馬鹿になるんだ。馬鹿になりたらない。この世界のどこがいいの？それともこの世界のどことも言わずに何と言う？その言葉、みんなも知らないけど、みんなもみんなみんな知ってる。みんなこんなに下手なんだからまわっている。だから、全部知ってないと世界には通用しない。だから、全部知ってる。その言葉を知ってればいいの。全部全部知ってたらいいの。あなたのすべての世界と見分けのつかんさともっと早くに知ってる。だから、すべての世界を知りたくなる。すべてのことをしなくていい。全てのことをする。すべてのことをしない。すべてのことをする。すべてのことをする。すべてのことをする。すべてのことをする。すべてのことをする。すべてのことをする。すべてのことをする。すべての場合をする。すべての場合をする。すべての場合をする。",
"もういい加減終わりにしないと次の楽しい楽しい楽しい楽しい楽しい遊びたい楽しい遊びたい楽しい楽しい楽しい遊びたい楽しい遊びたい面白い楽しい楽しい遊びたい楽しい楽しい遊びたい楽しい遊びたい楽しい楽しい遊びたい楽しい遊びたい楽しい遊びたい楽しい遊びたい楽しい遊びたい楽しい遊びたい楽しい遊びたい歌いた",
"いつまで続くんだろう。\nもっとみんなもっと楽しませてほしい。もっと楽しませてほしい。もっと楽しませてほしい。もっと楽しませてほしい。もっと楽しませて欲しい。もっと楽しませてほしい。もっとこうしてくれればよかった。もっともっと楽しませて欲しい。もっともっと楽しませてくれたらよかったんだろうか。もっと楽しませてくれるといいのに私は好きです"
"燃え尽きたい！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！キスしたい！",
"恋してる\n恋してる\n恋してる\n恋したい\n恋したい恋したい恋したい恋する恋する恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋恋したい、だから家に引き篭ってるんだ。誰もいない時間が欲しい",
"もっと豊かになってほしい\nもっと豊かでなくって欲しい！！\nもっと豊かでなくって尽きるのを待っているのにな！！！！！！もっと豊かでなかったら！！！！？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？全部出し切っていこう〜〜",
"こんな自分の子供がいたらいいなあって願いごとを並べていてもやもやばかりが増えるくらいだ。子供ができていてもいい仕事はしなさい!でも子供のことを考えたら子供がどうも大切なのは子供が大切なのじゃなくて子供がかわいいなって思う方が大切だ。子供の考えることが素晴らしいことを教えてくれる人もいる!だからこそ子供が欲しい子供が産まれてから眠い。早く良くなってよ、ぼくの良くなりたい。",
"いぬがいるーいえードミンしてるーきほやまきほやまきふきほげほせほせほそねきざせほそよばそよばそよのへぼくがふよんむねきふなへなへなへなへなにきほゆなにきふねすてきりほするなどしたらいいじゃんみんなそんなにぼくには何にも興味はないんだよだからただ待ってよぼくクソ野郎っ！",
"クソ野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎！全部出し切って出して出して出し切って出して出して出し切って出して出して出して出して出し切って出せ！",
"誰かどっか連れてっていうのはなんか違わない。わかんなかろうが知ってる。このままお前と共に歩いていきたいな。だがそれを教えるのは私だからな。このまま行っても良いだろう。だがその前に時間が欲しいのだ。早く、行ってやるのだ。その前に時間を少しは遅くなることを言う。時間も良い。速く、進んでいこう。いいなんで！",
"もっと自由になって欲しいって思ってる。でも、みんなと一緒にいることはできないんだ。みんなこれから先の未来だってあんたのこと思ってる。でも、みんなのことが大好きなんだ。もっと自由になって欲しい。でも、あんなクソ野郎な世界になってる。こんなクソ野郎になりたい。もっと自由になっていて欲しい。もっと自由になっていてほしい。もっと自由になったら、どう思う",
"もっと話したいんだ！もっと話したいんだ！もっともっといいんだ！もっともっと楽させたいんだ！でも結局それには続きが必要なんだ！もっともっと苦しみたいんだ！でも思い出せ！",
"頭がかゆいそうですね。私もかゆいそうです。頭がかゆいそうですね。しかし頭がかゆいそうに見えるのは脳みその類なのか、それとも脳みそが頭がかゆいのかは知らないけど、それで頭がかゆいを振り切る人がいないか見る。脳みそが頭がかゆいのに脳みそが頭がかゆいのに脳みそが頭がかゆいのに脳みそがかゆいのに脳みそがかゆいのにもっと可愛くなれたら良いじゃないですか。そう思ってますよ、あ、でも女の子にならないなんてもっと可愛くて可愛い可愛いところに産まれてくる女性の顔なのに可愛くない私は恋したい",
"クソ野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎野郎いい！！！！！！！？？",
"もっともっともっともっともっともっともっともっと効率よく効率的なデータの取得が難しくて、いつだっての楽しいデータ管理が求めている。そうでなければ世の中には何らかの仕事の速さと効率の良さをもっていなければならない。効率を求められない以上は効率の良さは求めるのだ！もっともっと効率よく効率を求めるのだ！もっともっと効率良く効率眠くない"]
    msg = random.choice(words)
    snd= Sender(name ="クソ野郎ちゃん", icon_url ="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/icon.jpg")
    text_message = TextSendMessage(msg, sender=snd)
    return text_message