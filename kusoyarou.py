import random
from linebot.models import (
    Sender, TextSendMessage
)

def replymsg():
    words = [

"もう無理かもって諦めてた。もっともっと努力したっていいじゃん。もっと効率よくなりたいっています。その一方で仕事をしながら自分を好きな人と会話しているというのは幸せなことだ、ということを最近学びはじめています。どう接していいかわからないし、どう接していいのかわからない。でも接していかないと、私は一生、一生、生きていくことしかできなくなるのだろうか。",
"寝ながら読む本は最高！！！！！！！！！！！！！！！！！！！！何でだよ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！』どうしても勇者らしいかいな。。。でもさ、その世界を、滅する奴居る。",
"いい加減な男と3日で8割の甘え方を追い求めてしまったので、私はしがない農家であったからこそ自分がもっともっと自由に生きられると信じていた。だからその自負は本物だった。しかしそれから何日が経過しただろうか。ようやく家の中が片付いた頃、ふとした拍子に俺は何もない空間に放り投げられていることに気づいた。何もない、わけのわからない状態でどうやって何もない空間に放り投げられているのかと問われると、あまり思い出したくもない。そもそも俺はその状態で何もないところから飛び出して、何もない空間を逆さに吊り橋の下にでも落ちてしまったのだろうか。そんな馬鹿なところまでは確かにありはした。けれどここでは何もないところから抜け出すことを覚束なくしてしまったのだ。ただひたすらに、もがき続けていた。それが馬鹿馬鹿しいとは思わない。けれどこうしてこのおかしな状態のまま居続けていられるのも意外と難しいのだろう。そんな状態にありつつあったのだから、これは大きな間違いだった。これでもう少し自由に生きるにはどうしたらいいかわからない。けれどここに行く以外に選択がないのならば、もはやどうすることもできないだろう。こ",
"「彼氏欲しい」と言っても、「まだそんなに先ではない」と、彼はきっぱり",
"あーつまんね。もうヤケだ。ヤケだ。ヤケだ。ヤケだ。ヤケレかわからないから、なんか悔しいな。「さて、もういいだろ？ 僕はお前の手伝いをすると決めてるんだ。手伝ってくれたことだって、お前の大切なものだからな。だから手伝ってくれないか？」",
"もうやだよ。もうやだよ。もうやだよ。もうやだよ。もうやだよ。もうやだよ。",
"燃え尽きるまで楽しむぞ！アイスに限らず、あのアイスが食べたい。",
"びっくりするくらい、すごいすごいんですよ。わたし、生まれたこともないのになにかさらして信じられなかったけど、確かにここまでの戦いがするんだなって実感した。これくらいの勢いでいこう。",
"タバコ吸いすぎた？最近よくわからん。とりあえず何とかなるだろ。とりあえず何とかいあるかもしれない。でも、それでも好きなんだから、好きを曲げないで、ただ愛していきたい。",
"心を動かさないで。お金と時間と笑顔を振り回して。お金よりも楽しめるアーティストの世界観で、自由に楽曲を作っていきたいです。",
"もう無理かもしれないな、もう無理だと思ったら、どんどん力を抜いていきたいな。",
"ここは？ここは、どこだ？私は、この宇宙に引っ張られているのだいあれ」彼女が歌い出した。僕の心の傷を少しでも癒したい。",
"クソな奴がめついてきたらいい加減にしろよ。いつまで経っても癒せずにいるのが目はしっかりとした口調で私の顔を覗き込んでる。やっぱりお前の好きな人の匂いがする。",
"ピザおいしいグラノーラほしいたべたい食べたい食べたい食べたい食べたい食べます",
"なにもしないのまま好きになってしまいたいです。生き別れ別れになってほしくないですよ。",
"誰にも止められないし、誰もかも知らないで叫んでしまう自分が嫌だ。",
"やりたい仕事か、やりたいようにやっていこうと思う人と出会わない限り、やりたいいあいたい",
"何か嫌われるようなことしたかな。結構、友達と遊んだのに。何もない方が嫌うけど、やっぱりここで吐き出したい。",
"「さようなら」が、最後になってしまったのでしょうか。最後に君の笑顔が見たかいあれ。",
"死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ね死ねーって、言いたかったのになぁ。",
"誰かこの人と連絡取ってるーーーーお前だけじゃなくて、この人の大切べまだ温かいよ」「ああ、そうそう。もうそろそろ行かないと。またね」「うん、またね」そうして別れて俺は、どこまで行けたらいいんだろうと考える。この世界に、行けなくなってからは考えないようにする。",
"もういい加減寝たいな 目がハイライトを追いかけたいいっそ全部の夢が出てくる。また出てくる・・っていうか、出てくれないと始まらないんだが。出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれだ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくれ、出てくる、出てくれ",
"面白くないなぁ 誰も教えてくれないし、関わりたくないな。ずっとモヤモヤしてきました。そして、その先の未来を想像したとき、想像以上にワクワクするんです。ワクワクを感じるきっかけを与えてくれるのが、このセッション。私のセッションの特徴は、想像とイメージが一緒くたになるセッションです。想像すること、イメージすること、想像することが大好き。セッションを受けて実感したことは、想像力が成長したってこと。想像することは、想像したことになにかしらの形をもたらし、想像力を高める。想像する力が成長したとき、想像する力が増す。想像することが大好き。想像する力が増したとき、想像する力が増すので、環境が変わる。環境が変わるたびに環境は変わる。想像する力が増した場合、環境は変わる。",
"お菓子食べたい❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤⚽",
"もういいよ、さようならだってささよならが一番楽しいじゃんもう嫌だ、さよそめしくそーな話かーなー",
"何もしないでぼーっとしてる人に興味なんて無いんだよなぁ・・・たまに何かが起こっているのではないかとか、そういうものだったらいいなーって思ったり。",
"あー、またか。イライラする。イライラする。イライライライライライライライライライララ系に振り回されている。お金は持っている？仕事はこなす！愛してる！愛してる！",
"もう無理かも。もう無理かも。もう無理かもって何回も思った。でもやっぱりやっぱりやっぱりやっぱりすごい！ やっぱりすごい！ すごいすごい！』そう、これが俺の最初のステージなんだ。ステージを始めてからどれくらいの時間が経ったんだろう。気づいたころには日が暮れていた。もう寝ちゃおうと思ってそのまま目を閉じていたとき、不意にお前がやってきた。『ねえ、ちょっといいか？』その名前は聞き覚えがある。俺は反射的に手を伸ばした。でもその触れる直前で身体が動かなくなった。『なあ、どうしたらいい？』",
"不倫していると言っても受け入れてもらえるかわからないし、自分に正直に生きてますが自分に合ったデザインを知りたくていろいろ調べたり調べた末、この商品にしました",
"やりたいことがありすぎて、どんどんやりたい放題になってる…。せっかくの楽しみが台無がしないようにしないと…",
"やりたいことやるくらいしか頭に残ってないんだから、もうちょっとなんとかしたい。やります。これからの季節は本当に生きた心地しないです。自分を解放するという使命を忘れていて、解放されたことにより、自由になれたような気がしない…なんていうことできることは、まだ少ししかありません。これからも、僕と一緒に自由に生きていきませんか。",
"やりたいことに追われて、自由に動けない今。中途半端にやりたいことを追い。やりたいことControllerを動かすControllerを動かす",
"「家に友達が来る」っていうのはなんて言い訳だなんだか微妙だなあ。",
"家に篭ったままぼーっとするのもいいかもしれないな！！！！！外に出さないようにしてたのにーーーーーー",
"おいしいお野菜が食べたい前に食べたお肉が美味しいっていうのはよくわかっています。これは人類の遺伝子であり、遺伝子と言っても良いでしょう。そう考えているのは確かです。何故これを選択したのですか。これは人間の将来の為になさっている選択です。これは人類の役に立てるチャンスです。",
"子供が寝てから3時間くらいかな。でも平気。誰か助けて。早く。心が張り裂けそうだ。",
"「さようなら」くらいは言いたい「さよなら」くらい言いたい「さよならいあたしの時間は惜しい」「なんだそのステージは」「主役はだいたい決まるから、主役が決まった方がもっと観られるんだよ」「主役が決まってることは決まりだな」「主役が決まってるって、どんだけお金のかかることなんだ」主役が決まってることは決まっている。",
"お酒が禁止になっても、ビールを作りたい。でもビールは作れない。だから、ここで死んでしまおうかしら。ああ、どうせ死んでいるのだから、何も怖いものはないのに。",
"全部出し切って行こう。全部出し切って行こう。全部出し切って行こう。",
"ここで「ぼく」っていうのかな。「ぼく」っていう前に、「ぼく」っていう前に、俺が殺す。死んで花になって。これからは一緒に死ね。",
"全部めんどくせえ全部めんどくせえ全部めんどくせえ全部めんどくせえ全部めんどくせえるよ。なんだその言い草は。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカクる。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカつく。ムカ",
"死にたい。死にたい。死にたい。死にたい。死にたい。死にたい。",
"あーさーん、そろそろ行きまーす。旅立つ曲、もう忘れたの？もうかまわないの？」「なんだよ、いきなり。いつの時代もそうだが、いきなり喧嘩売って来て。俺は買いかぶりだなと思ってるんだよ。」「だったら、そのくらい分かってるでしょ。」",
"もうやだこんな気持ちにならないでーっとお願いばかりしている中、このヤロウライブDVD にチャレンジしました。 その名も【DISCOVERY ZOOM Z-OV-01 (40時間VIDEO)】",
"やりたいことを見つけて、やれやれって感じですね。やりたいことを見つけて、「なんだよ、それ」",
"エロいなー。エロいしかし、エロいしねー。エロいなー。エロいしかー。エロいしざりした。ふと、隣にいる男の姿がようやく近づいてくる。男はびくりと肩を震わせる。私は男を見た。男は不機嫌そうな顔をしていた。その目には確かに狂気が宿っている。「お前、何か知っているのか？ ここでは教えないから、帰ってくれ」男は私を見た。だが、すぐに表情を強張らせた。その瞳には何の迷いもない。「何が、教えないんだよ。何もないんだってわかっているじゃないか」「何もかも、知っているじゃないか」「何もかも、お前が分からないのか？」男は黙っている。「お前は何もかもをかけて、何もかも知っているじゃないか。その意味が、わからないのか」その視線に射ぬかれるように、私は男に近づいた。男は怯えたように私と目を見つめ合った。その眼は、まるで涙の粒が溜まるのを眺めているかのように深かった。「わからない、か。そうだね。わからないな。だけど、わからない理由なんてわたしには要らないんだ。わからなくていいから、わたしがずっと前に進もうよ。お前の邪魔なんて、なんにもしないよ」その言葉を最後に、私の瞳からは再び光が失せた",
"あーイチャイチャしたいあーイチャイチャしたいあーイチャイチャしたいもういいや、と考えていたら気づいてしまった。これじゃん、もうやだなんて感じる。これは、自分の中にずっといる、生まれた感情なのかもしれない。",
"死んだら終わり。また死にたくなるその前に死んでしまいたい。死にたいけどできない、ってことは俺が受け入れるしかないってことさ！」「お前は俺の敵か、それとも敵わない俺の敵かっ！」「あ、ああ……わかった、わかったから待ってくれっ！」そんなとき、このままずっと戦い続けたいがために俺は力を振り絞って、この世界の支配者になったのだ。その力で世界を支配し続ければ、世界はきっと平和になるだろう。だから、その力で世界を支配し続けたい。それこそが俺の願いだから……！",
"あーもうめんどくせえーーーーーめんどくせえーーーーーー腹を決めて決めて腹を出してきた。「ありがとう」",
"漫画読んでる。このジャンルに疎くてすいません。よろしくお願いします。もう帰ろうかな。帰ってきたときには、きっとお腹が空いているはずだよ。早く会いたい。",
"不倫のことは全部忘れて、愛する人と幸せになっていましょう。不倫したいけど、忘れいているかもしれない。でも、僕は彼と一緒にいられるだけで幸せだよ。",
"誰かの力で何とかならないのかな？力を貰えばそれで良いのかなって思う。それに、この時間に帰るのは惜しい。私はもっと早く家に帰って両親にばれないように隠したい。",
"冷蔵庫にあったものを全部出したら面白いかも?冷蔵庫無いときの楽しみ方が全かがわからないのですが、なんか、頭の中がぐちゃぐちゃになって、言葉が出ない。頭の中はぐちゃぐちゃで、言葉なんて出てこない。なんとも言えない状態で、ただただ、ぐちゃぐちゃになった言葉の数々が、頭の中に浮かんで行ってしまう。まるで脳を置き場にしたまま、ぽろぽろと、ぽろぽろぽろぽろぽろぽろぽろぽろ。ああ、なんて、なんて、なんて、なんて、なんて、なんて、なんて、なんて、なんて、なんて、なんて、なんて。",
"あー、つまらない。つまらない。つまらない。つまらない。つまらない。つまり、この人がただのエロいだけなんですよね？僕は見ないふりをしてきいたけど、見てほしいよ。",
"このくらい料理すれば良いんじゃない？コツとかポイントとか。料理下手じゃなくてもいあーだ。",
"ここまでしてくれるのなら良かった。これでまた早くに戻ってこれる。これからはもっと嫌な気持ちになる。早くこの気持ちを払拭したい。",
"燃え尽きたい。アイスバックスだ。誰か俺を縛ってくれえええええええーーー。なんか、情けないな。でも仕方ないな。だから、僕がこのコードを引き受けてやるよ！」",
"家で食べたい夜食朝ごはん夜食昼ごはん夜食これだけは食べれないかも",
"おいしいおいしいを作る人てほとんどいない。おいしいを作る人はおいしいといありがとう。また、会おうね。",
"おいしいおかゆ。つくれぽに。風にたゆたってくれる。食べ歩き出る感情の起伏が大きくなっていく。これは、つまり、感情の起伏が大きくなっていく、ということなのだろう。だからやりたくないなー。",
"びっくりするくらい、すべすべしたべたべたなんだけど、すごく好き。好きのろって出てくる言葉が全て。つまらない。もっと明るいキャリアを願えば良かった。",
"寝ながら漫画読もう寝ながら漫画か朝の時間に身も心も少女になろう",
"燃え残った本を整理し直したい！そう思った時は、燃え残った本いあい。",
"何もしたくないから何もしたくないんだから何もしたくないで引っ張らないで下さい。",
"もう疲れたよー。もう。寝よ。。。。。。。。。。。。。。。",
"なんだろう……わからない。何が何だかわからない。何も考えたくないままにしてしまうのはなぜなのか",
"どんな風に生きるのが一番幸せなんだろう。それはきっと誰も教えてくれないいあたしに負けるないあたしに勝つために！」「うんうん、わかっちゃった！わかっちゃったからこそ俺が叫びたいの！叫ぶしかないんだよ！！」「うんうん、わかっちゃった！叫べる人は俺にはいないの！！」「俺だって俺の想いを大切にしてればよかった！！」こうして俺と一緒に戦ってくれるあたしは、強大な力を持つ剣を前に膝をつき、悔しそうに俯いている。悔しいけれど、その想いは確かに俺の手に入っているんだ。だから、もっと力になってあげたい。そして、その想いを俺にぶつけて欲しい。",
"燃え尽きようかという前に、何もかも失ってしまえ。それが私の生きながらに散っていくのかもしれない』と。どうやっても出会わない人の幸せ、それはきっと僕の幸せなんだろう。だけど、そんなの関係ない。出会わないもどかしい、出会えたってあの人の幸せは掴めない。出会えないで当たり前。出会えたって所詮当たり前。出会えないまま、知らず知らずのうちに積み上げられていくの。つまらない、つまらない。出会わない、だから進もうと思えない。出会えないからこそ進もうと思えない。出会えないまま、その先に何が待つのか知らなくて、進もうとしないで、ただただ嫌われ続けるの。嫌われたまま、でも進もうとしないで、ただ見つめてくるの。まるで心を無にして心を無にしているようだ。あの人の幸せなのが、その先に待っているのかも知れない。",
"眠い。また明日。                  長山正平)  「この番組は感動した。 感動した。これまでに味わったことのない新しい 感動の体験ができた。」  「これからもテレビが大好き。だから大好きなんだ。 」  「そして、また同じステージに立つんだ。そのステージを、一緒にワクワクしながら 走ろう。」  これからはもっと感動の新しい新しいドラマが生まれる。その感動を感じる番組だ。感動のステージというのは、「感動の新しいドラマ」なのかもしれない。",
"お金がない時には何も考えない習慣が嫌いなんだと思う。つまらない。",
"自分に自信が持てない。周りと一緒に周りの人を幸せにしたらいいのになぁいあたしとお友だちになってください。",
"やりたいことたくさんやる。やりたいことたくさんする。やりたいことたくさんしない。やりたいいあいたくない…",
"何もない事なんて、どうでもいい。そんなのわかっている。わかっているけど、目を出したらいいんじゃない？",
"面白かった!面白かった!面白かったーーーーーーーーーーーーーーーーーーーーーーーーーーーが乗り移ったようになっていた。「ちょっと、私はまだ帰らないとダメなの？」「お前は最後までやり切ったが、また一緒に走らなければならないのだ。少しは回復した方が良いのではないのか？」「私はもっと走りたいよ、っていうか、もっと一緒に走ってたいよ。」「わかったわかった、頑張って走っていけばいい。」そういうと、アイアンクローが吹っ飛んでいった。「おい、アイアンクロー！これで勝ったってどういうことだよ！」「わかんない、わかんないよ。」なんだそいつ、と思ったが、とにかくこれ以上こいつのことだ。何か他に方法がないのだろうか。",
"面白いですように。つまらない事を笑い飛ばしている様に見えるんだろうか。もう無理かも",
"何にもしなくても、誰か俺を縛ってくれないか？その先は自分でだ。もうそろそろ良いのではないだろうか。それくらいのことでモヤモヤしていたというのに、ここまでやると逆に笑いたくなってくる。まだ早いかもしれない。だって、まだ出会い頭に使ってないから。もうちょっとうまく使っていたい。",
"なにもしたくないから、何もしたくないから、何もしたくないから、何もしたくないから、",
"タバコ吸いすぎて30分で死ぬのやめてほしい。漫画みたいに死にたい。死ばして、その代わりに残したいものってなんなんだっけ。それが、この世界か、この私のかけ離れたわたしなのかもしれない。",
"クソ野郎はクソ野郎で良い。クソ野郎で良い。クソ野郎で良い。クソ野郎で出てくるのなら、出てこない方が不思議でもなんでもないかもな。うん。",
"もうやだ、これ。何もかも嫌になって、何もかも忘れて、何もかも可愛いないあい方。愛してる。",
"眠いー眠いー寝たいーーーーーーー目を閉じてるーーーーーーーーーーーーーやっと、やっと繋がった。全部はうまく行かないことはわかっていた。でも確かに、繋がっていてモノになっていった。そのモノにはなりたい。その気持ちはいつも強い。",
"美味しいラーメンと出会いにくを入れたい♪♪♪♪♪美味しいラーメンと出会いありがとうね",
"世界平和、平和で美しい日本を共に平和で豊かな世界へ世界70か国全土で起こるであろう連続的なテロ事件をテーマにしたドキュメンタリー映画である。",
"家に帰ってから漫画描こーよー。漫画読もう。漫画読もう。漫画読もう嫌だ。どうにかしないと、俺の居場所が……「おい、なんだそのムカつく事は……」「なんですか？」男が俺に詰め寄っている。その手が動き俺の顎を掴みようとしている。その瞬間、俺は地面に強く押さえつけられた。「ガハッ……！？」「お願いします！！！」その瞬間、俺の身体が光に包まれた。その光は見えない力で男の身体を締め付けていく。「お前が………俺の………」「私こそが正義です！！！！私こそが正義なんですよ！！！！！！",
"おいしいおいしいを作りたい・読んだラブコメを愉しもう料理はがきの作り出した。   「この世界が面白い」という理由だけではなく、たくさんの人が興味を持ってもらえたらいいなと願ってしまう。 みんな、面白い話をありがとう。■神の作ったものは結局、自分の物にならない。  「この世界が面白い」と思える世界を作っていけるようになったこの時代になるとどんどんそんな作りの人が増えている。  だが、そんなことは関係ない。  「この世界が面白い」っていうことは人それぞれ違うんだ。みんなはそう、みんな大好き。",
"もうやだなーなんでだよ。どうやって家に友達いるんだよ。友達いないよ。なんでなんだいある。",
"燃え尽きたい。燃え尽きたい。燃え尽きたい。燃え尽きたい。",
"あーめん食べたかったあーめん美味しかったあーめん美味しかったあーいああああああああああああああああ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？",
"なにもしたくないから何もしたくないけど、何か言いたい、なにかしたいっていうと何かが怖い。だけどここで不安を顔に出さない訳は無い。だから僕は深呼吸を決める。「……じゃあ、このままでいいかな？ 僕の言ったこと、すごい大切だと思う」「うん、わかった。なんだそれ、つまらないな」「なんか、その、僕の大切な人を傷つけていたらしいっていうか、悔しかったんだ」僕の言いたいことをすぐにわかるだろう。わかってくれたら、どんどん近づいていってもいい。だって僕の大切な人は、もうこの人にない。",
"美味しいお酒に酔いしれて酔い方が狂っているのではないかと疑われている気がする。",
"自分でもわからない××が好き。×××が好き。ème away❤",
"燃え尽きたい！！！！！！！！！！！！！！！！！！！",
"全部出し切っていっていいんじゃない？全部出したっていい加減つまんないよ？みんな。。。このまま、ここで、ずっと、時間が、止まっていたい。",
"このままでいいのかな全部うまく行きますように⚽ダイエットの悩みを元気にダイヤは最後の命令を残した「そのまま朽ちるがいい。」",
"なんでこんなに平気なの？なんかされたの？とか言われたりしたらいいのに。なんでこんないあたしに幸せは訪れない。それでも、いつかここから出ていくモノは誰もお金なんて気にしない。だったらこの世界にずっといたい。"
    ]

    msg = random.choice(words)
    snd= Sender(name ="クソ野郎ちゃん", icon_url ="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/icon.jpg")
    text_message = TextSendMessage(msg, sender=snd)
    return text_message
