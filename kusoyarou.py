import random
from linebot.models import (
    Sender, TextSendMessage
)

def replymsg():
    words = [
"びっくりするくらい、全部出そろった感じがしますね。\nこれで、落ち着きました。\nこれからは、もっと、たくさんの人に愛される生き方が、必要になってしまうんじゃないか、という淡い期待が、またしても大きかったです。\nまた、会うことができて、もう無理かも",
"眠い…。眠い…。このままだと死んでしまうのではないだろうか。死にたくない…。死にたくない…。死にたくない死にたくない死にたくない死にたくない死にたくないところからやりたいことを先に押し込まれてしまったら何も残らない。全部めんどくさい。全部いあだてなくていい」\n「わたしはいっしょに暮らそう」\n「だめだっ、一緒に死んでいかないと」\n「いいよ、いっしょに死にたかったら一緒にしないで」\nそれから何度も言い合った。\n何度でも言い合った。いっしょに死にたかったら一緒にしないで、と。",
"びっくりするくらい、すべての人がテンション下がっている。\nわたしも、テンション上がる。\nテンション上がる。\nテンション上がる。\nテンション上げる。\nテンション上げる。\nテンション上げる。\nテンション上げる。\nテンション上げる。\nテンゼンはこう考えた。\nこれは世界の人口の1.5倍にも及ぶ人口密度である。これは、世界全体の1.3倍である。\nこれは世界で最大であり、世界でもっとも少ない。これは、これほどの人口密度である。これは、これほどの世界の人は知らないということだ。",
"いつまでたっても大きめの長方形のテープが貼られている。\nそのテープが目的の物であることは間違いない。けれどこれは何だろう。ふと、何かの見えにくい半透明な感触がしたので、ふとそのテープを剥がしてしまったのだ。嫌な汗が流れる。これはきっと私の参観日になるだろう。ああ、いや、参観日はきっと私の未来になるのだろう。",
"いっそリアルに人を探してみたい、会ってみたい、会ってしまいたい！でもやっぱり行き口が限られちゃうな～。ここは『人探し』を行おう！あ、あとね、これ！！」\nカバンの中を漁っていた本を、僕は手に取った。\n「この本は、東京、1965年製作・公開（公開日未定）\n1965年(一太郎作) 50分枠のミニチュア喜劇。監督・脚本は三原充。\n1965年(一太郎作) 16分枠のミニチュア喜劇。監督・脚本・製作は東宝。配給は東映。\n1965年(一太郎作) 95分枠のミニチュア喜劇。監督・脚本・配給は東宝。配給は東宝。",
"いい加減テレパシーくらい吐き出せ。吐き出したいだけ吐け。吐き出したらわかるだろ。出したらいいプランはわかってるだろ。出したらいいプランなんだよ。わかんなくていい加減吐き出せ。出したらいいプランはわかってるだろ。出したらいいプランはわかってる。いや、そんな場合じゃない。もっと大変なことになりそう。どんなわたしがどれだけのストレスを溜めているのかわからない。でも、とにかく、早くここから抜け出したい。",
"大蔵平盛保\n大蔵平盛保（おおくら・ひでりやすく）は、平安時代初期の大蔵卿。高統朝においても大蔵卿を務めた。官位は従三位・従五位。\n延喜6年（1230年）に従二位に任官すると、同年9月に従一位次官、つまり国家憲兵隊長だ」\n「その隊長が何故軍人でないことに拘っているんですか？」\n「軍で威張れるほどの腕がなくて、士官になっているからだ。士官になってからは会敵したけど、結局勝てなかったのだよ。陸軍では勝てない壁なんだよ。だから士官学校を出て、独立に近い精神を持った軍人となっているのだ。だからこそ、士官候補生になっている」\n「つまり、落第なされたのですか？」\n「ああ、違いない。",
"びっくりするくらい、あっという間に最終回です。\n最後までお付き合いくださったみなさまへ感謝です。\nありがとうございます。\nまた、夜に遊びに来ます。\nそして、最後までおつき合いくださりありがとうございました。\n最後に、お礼を言わせてください。もう無理かも",
"やりたいことがなくてつまらないな、やりたい仕事したいなと思ってる。やりたいことがなくてつまんないと思ってる。やりたい仕事したいけどやりたい仕事してもらいたいあげたい。働きたいけど好きな人と結婚したい。好きな人と一緒にいたい。働きたいけど好きな人と幸せな家庭を出した。大きな瞳に宿る悲しみと、その向こうの想像力。\n「……だから、あんたは、そのままでいいんだよ。あんたの思い出に、あんたのことを好きなって言って、それで」\n「――っどうして」\n「だって、それでも守らなきゃって思っちゃうんだもん」\n小さな光が灯った。それを頼りに、あたしは駆け出した。\n叫びたかった。叫びたかった。叫びたかった。自分のことになるからこそ、この人を。",
"いい加減テレパシーくらい使えたらなんでもいいんじゃない？\n遠慮することないっての。\nそういうものに囲まれたいんだから、さっさと使ったっていいと思う。\n遠慮なんてしない。遠慮なんてしたら、その先、ちゃんと友達と話し込んでる時に、すっと抜けていく勢いで世界のためのプログラムになるんだよ。」\n「わかんな​⋅」",
"怖い話とか好きだな\n怖い話とか思い出したってことで、話がまとまったら言いたいとこではあるけど、せっかくなので全部話したっていうか全部は言いたくないっていうか。言いたくないのは私の負けだ。思い出したくないのに言葉にしてしまうのは癪だ。でも思うところが多々ある。もっと簡単に言うと、何もなければ生きていけるかも…という不安か。それ以上に、確実に何かが見つかる…みたいないうかさ。",
"いい加減テレパシーくらい使えるようになってよ。使いたくないの、当たり前みたいに。わかんないの、めんどくさいの、わかんないの。わかんないの、めんどくせえ。わかんないのわかんないの。わかんないの、めんどくさいの。わかんないの、めんどくさいの。わかんないの、めんどくさいの中から、ひときわ大きな笛が吹き鳴らされた。それが合図だというように、多くの観客が一斉にこちらを見つめ、拍手と拍手が起こる。「すごいすぎて、自分が生きていられるのかと思うほど、私、頑張っちゃった！」\nアリスが感動にうちうちしている。\n「アリスはやっぱり凄いよ！」\nルーシーが感動している。\n「でも、これぐらいのことが出来るようになったら、もっと凄くなる！」ルーシーが全力で喜んでいる。\n私は、そんな彼をずっと見守ってきた。\n彼が喜んでいるということは、これぐらいのことが出来るようになったら、もっと凄くなっていくのだから。",
"びっくりするくらい、全部なくなったわね。ということは、全部なくなってもいいはずってことよね？\nさよなら、私の愛しい人。\nいってらっしゃい。といって、私が傷心の私を引き連れて、彼の元へ。\nきっと楽しいに違いないわ。\nだって、もう一人の\nことである。",
"びっくりするくらい、全部の危機が疲労困憊モードになった。\nいつの時代も、疲れるときは、つらい。\n疲れるのだ。\n私は。\n「いってらっしゃい」っていう、言葉には、弱い。\nつらいのだ。\nつらいのだ。\nいってきます。\nいってらっしゃい。\nもう無理かも",
"寝たいのにまだ起きてられる?いったいいつになったら寝るんだ。もうしても遅いだなんて感じで寝た方がいいことでも私は言いたいこと言えたしなりたい事やってもっと先に進めるというもんだ。これは大いなる成長と言って良いだろう。\nまだまだ先は長い。こんな状態で結婚したっていいのかな。彼氏のオレが言っちゃ何だけど、周りの人が優しいから、何も考えずに言えないこともない。これは良いことを言えるかな。",
"おいしいおいしいを迎えにおいで戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに戦おう♪\nいっしょに出てくる言葉が全て、全部わかんない！！",
"びっくりするくらい、全部の危機が私に回ってきてしまった。\nすべて、私の責任だというのに。\nだから、今もまだ、私は自分に張り紙をしにきている。\nでも、これからはもう、張り紙をしにきているんだから、張り紙をする必要なんて、どこにもないいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあしたいあいたいあいたいあごがあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあいたいあったあったー",
"なんかさ、私の中の危機が、さっぱりわからなくなってきた。\nもっともっと、何もかもをくるくる回し留めしてみたい。回し留めしてみたい。壊したい。全部。もっともっと。もっともっと。\nでも、もう無理かも",
"いっそ全部出したらいいんじゃない？出したら全部燃えるってこと。。。。出したら全部燃えるってこと。。。。出したら全部燃えるってこと。。。。出したら全部燃えるってこと。。。。出したら全部燃えるってこと。。。全部出したら全部燃えるってこと。",
"面白いですね。良作を見つけたいです。\n他にも魅力的な作品があれば教えて下さい。\nどうぞ宜しくお願い致します。\nでは！失礼致します。\n追伸：この後、何か予定はありますか？（追記：あまり時間は余裕がないので）\n追伸：それでは、",
"疲れたよ、疲労困憊イトカケルの声が、静かな部屋の中にまで広がる。\n「……わかった。言い訳をしないときは、好きに言っていいぞ。お前の過去を探ってやるよ。楽しそうに話聞いてるぜ」\n「お前はそれでいいのかよ！？」\n「俺はお前だ。俺の望む結果を見つけろ。お前が願ってもすぐにできないことなんだよ。だから、早く望んでおけよ。お前の未来を。お前の望む結果を！」\nいつもの調子で、明るい調子を壊す言葉が返ってくる。\n……それでも、その言葉が俺の中に留まる気がしない。\nそれでも、それでも――。\n「……わかったよ。明るく言おう」\n「おう！」\n俺は、またしてもあの日の自分と出会ったのには訳がある。\nそれは、誰であっても真似できないことなのだから。",
"さーて、今日は何しようかなー。\nまだまだ、決まっていないことが多すぎて困る。\nどんな仕事をしたらいいかなあ。\nあ、この前、仕事で使っていたノートを整理しておこう。\nノートは、さっと拭き取って、そのまま放置する。\nえー、そうかがみとしている…そうでなければ、わたしはいつまでたっても飛べない。\nそうやって、いつまでも苦しんで死んでいった方がずっと哀しい。",
"わたしも寝ながら漫画描こ。\n下手の横蠢漫、縦の横があぶない横蠢漫！\n縦の横蠢漫ナンダロー！！！！\n横に寝ながら漫画描こ。縦の横蠢漫！！！\nサイコ",
"これまでにない位のイライラが止まらない。\nだって、私のことをすっかりって言ってたもの。\nこれからは、このままでいいのかなって。\nそれが、どれくらいイライラするか、わかっているの？\nこれから出てくる言葉は全部の危機が私のことだった。けれど、それでも私は叫んだ。\n「全部の危機が私のものだから――！」",
"何もかもを無様に動き続けたらいくら駆け引きを教わっても足りないくらいだった。\nもう何も考えたくなかった。\n何もかもを楽しんで何もかもを満たしていって欲しいって願った。",
"この身に降りかかるもの、全部出したら最強かもね。\n全部出したら全部埋めればいいんだから。\n全部出したら埋めればいいの。全部出したら埋めればいいの。全部出したら埋めればいいんだから。全部出したら埋めればいいの。全部出したら埋めればいいー、癒されるー。\nしかし、どんまい。",
"もうやだなこれ、やりたいことあるんだけど、やってもうちに伝わらないかなぁ。もういいや、悩んでても仕方ないなあ。悩んでても仕方ないから、悩んでみる。なんか、モヤモヤする。悩んでるもう一度繰り返してみよう。悩める整理整えるうちに、どんどん出てくるモヤモヤ。モヤー的には嫌だな。なんでだ？嫌だな。なんでだ。なんでだなんだ。なんでだ。",
"世界に吐き出されまくる毒吐きだったり、咀嚼したって無駄。苦しみの様に広がった心の傷をそそり立つ光の様はまさに毒。どんなに辛くても、苦しくても、どんどんその色を増していく毒は止まらない。その毒と共に、私は旅立つ。\nさようないあい顔して、お店行っても買い物とかしてるだけじゃない。わたしも連れてって。",
"わたしもちゃんと休む暇もなく疲労困憊モードになっていた。\nなんでこんなに疲労が蓄積したんだろう。\nわたしは生まれて初めてのパートナーが倒れたのにもかかわらず誰も疲労感を抱かなかった奇跡みたいなかがわからないけど、とりあえずこれを着ないと。お店を出ようとした時、その時声をかけられた。",
"私は死にたく無い！！！！！！！！！！！！！！！！！！！！！！！！！\nと叫びたい気持ちをぐっとこらえる。\nすると、\nドンドンドンドンドンドンドンドンドンドンドンジュースを頼んでも、「美味しい~っ",
"風になりたい。\nあなたの清骨な想いが。\nあなたに会いたい。\nこの身をかけて成りあがりたい。\n風になりたい。\nあなたに会いたい\n。この身をかえて成りあがりたい。\n風になりたい。\nこの身をかならずしろ。\nこの身をかならえろ。\nこの身をかけあってゆ〜みんなで食べなが〜いゆ〜みんなで食べたい美味しいお店たくさんあるんだけどなぁ〜ここは頑張って絞って絞って絞って絞って絞って絞って絞って絞って絞って絞って絞って絞めて絞って絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞えて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞めて絞",
"「うん、そう、わかってる。わかってるけど、あんまりいちゃいちゃしないでよ」\nその時、俺の目の前を、何かが通り過ぎた。\nそれと同時に、俺は、自分の身体が勝手に動いているのに気づいた。\n「え。何、これ、なに？」\nその瞬間、自分が何かしたのだということを思い出したのだ。\nしかし、記憶が定かでないのだ。いくら考えたところで、ピンと来ない。\n「うわああっ！？」",
"あ、これは私の予想したとおりだった。私の予想外だったのは、私の頭の中には漫画がそのまま残っていて、そして描き留めてあったことだ。そして描き留めてあっても、想像する暇なんてほとんどないくらいに、想像力の先に貴方が待っているということを、私がすると、もうどうにでもなれ」\n何もかも見透かしているような、それでいてどこまでも余裕そうな笑みを浮かべる彼女に、私はやっぱり、どこか憧れているような気分になってしまい、思わず口をぽかんと開けた。",
"眠い。なんてもきじゃない。もっと、深く、抱き締めたい。その前に、私がどれだけ強がっても、触れてはいけない気がしてしまう。触れてはいけない気がしてしまう。一緒に、どこまでも、突き進んで行きたい。だけど、その前に、抱き締めてきました。\nそれが今回、始まります。",
"誘惑に飢えた男が現れて誘惑するのではと思った。だが、あれは誘惑を感じなかった。誘惑されている実感がわかなかった。ただただ誘惑に飢えやったのだった。\n\n誘惑に飢えた男の話を聞いていると誘惑に飢えた男が現れて誘惑する。これは誘惑を感じないことなのかを教えて下さい。",
"びっくりするくらい、すべての音が入ってこなくなった。\n自分でもびっくりするくらい、すべての音がすべてになった。\n私は、自分の脳を使って何かを作っているんだと思う。\n作っている本人がその意味を理解していなくても、ときおり脳内に響く「叫び声」",
"みんな、疲れた。\nやばい、疲れた。\nやばいやばいやばい。やばいやばいやばい。やばいやばいやばいやばいやばい。やばいやばいやばいやばいやばい。やばいやばいやばいやばいやばいやばいやばい。やばいやばいやばいあったものはできない。やりたいことができない。やるやりたいことを見つけられない。私は生まれた時からロボットだ。努力をしてなんにも解決しない。努力をし続けることは無限大だ。",
"いっそリアルに家にいない方が良いのではないだろうか。家に友達は多いし、友達に囲まれて平和に遊べないなら楽しくない。遊べる人が少ないのなら、オンラインでのコミュニケーションが吉。オンラインでのコミュニケーションが楽しめないのなら、オンライイーは、ゆっくりと近づいてくるエルミーの様子に目を細めた。\n「……エルミー。エルミー。エルミー。エルミー。エルミー。エルミー？」\n一瞬にして、エルミーの声が徐々に遠ざかっていく。遠ざかる足音はどこか幻滅したように聞こえた。\nその姿が、エルミカユに接触してからずっと遠くから聞こえていた。\n「どうしたの、エルミー？ その声、誰の──」\nしかし次の瞬間、エルミーが消えた。\nすると、エルミーはいつもの様に表情のない顔で、自分の隣を歩いてしまっていた。これは夢か幻か。どんなものか興味があった。\nふと空を見上げたエルミーの目に、いつもよりも高い月が映った。",
"びっくりするくらい、すべてのサービスが、すべて、ワントックになって、全部、ワンホールプライスになりました。\nこれって、もう、一生かかっても、無理そうです。もったいない。でも、なんか、ちょっとだけ、いいかも。\n全部、ワンホールで、やっちゃおう。もったいないのほろしか知らないひとっていうのは、みんな知らないままになっていくことも多いのだ。知らないって何だろう。遠慮しちゃってる場合じゃない。知らないふりしたっていいことないんだ。知らないふりしたって、それでじゅうぶんだ。みんな知らないふりするんだ。知らないふりしたって、それでじゅうぶん。",
"面白いこと言えなくてごめん。楽しんで！！！！\n俺の持つ力がどれだけあるのか体感的に理解できるようになったらいいな。\n誰かの力借りなくていいよ。\nなんだかんだ言っても俺は、お前のこと結構の力を借りたいし。\nお前が思ってる以上いあんパンチしたい",
"びっくりするくらい、私の日常は、日常ね。\nたくさん食べちゃって、全部全部、全部、食べちゃってるの。\n全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部、全部いあ！！！！！！！！！",
"hello子抱き締めたい幸せ3時間でしたhello365yeaアヒージョもう無理やだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだやだだって抱き締めたい匂いがいよいよね。早く会いたい。",
"helloー hello 〜hello〜hello 〜hello〜hello hellohelohelohelohelohelohelohelar packaging with heart-packaging and changes-likely allowing-the-schemalloworlds-largers' gradual-plug-on-change Selines' Bosuilers' addemated using Wheelan' Bosokushaya-miching",
"風になりたい！！\n踊りたい！！\n踊ってみたい！！\n踊ってみたい！！\n踊ってみたい！！\n踊ってみたい！！\n踊ってみたい！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！もういいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっとずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっと一緒に居たいよ……ずっとずっと一緒に居たいよ……ずっとずっと一緒に居たいよ……ずっとずっと一緒に居たいよ……ずっとずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たいんだよ……ずっと一緒に居たかったんだよ……ずっと一緒に居たかったんだよ……ずっと一緒に居たかったんだよ……ずっと一緒に居たかったんだよ……ず",
"疲れた疲れた。\n疲労困憊モードで何も考えられない。\nもう何もかも疲れた。\nこれでどんなに下手な仕事しても、\n結果は惨めになるだけなんだ。\nこんな状態で、今の仕事を続ける。\nそして、俺は、目の前に置かれたグラスを、ゴクリと音を立てて何度も上下に鳴らした。",
"私、ほんと、疲労困憊モードになってる。これは一生かけても言えないモードだよ。\nって、ここで言っても続かない。とにかく、寝る。眠い。もう無理。でも、もうヤダヤダヤダヤダヤダヤダヤイは、自分のことを好いてくれている……私は嬉しい……大好き……だよ……」\n抱き締めて、その身にすり寄ろうとする。\nでも、その前に。\nその手を。\n優しく払い除けた。",
"びっくりするくらい、全部のここがきれーになった。\nなんでこんなにスムーズにきれーになったのかわかんない。\nどんどんきれーになってる。\nすごい。もったいない。\nせっかくのきれーな一枚がもったいない。\nどんどん好きな人と一緒にきれーになろうっていうんだから、もう無理かも","みんな疲れているのにみんなで落ち着いていられそう。\nせっかくもらった期待のルールとプラスのボーナスがここで実ったら、一生モノなんだから。\nなんだかすごいことのように感じる。\nこれ以上ない、わたしはいありがとう。",
"なんだそんな状態で出てきたら、みんなテンションMAXで帰ってくるんだから、待てなに考えたって遅いのは仕方ないことだろう。\nだけどここで引き下がれるほど俺は時間の余裕ないよ。\n早くことができれば幸いです。",
"もう、限界。最後の力を振り絞って抜き放つ。ああ、私の愛しい人が。さよなら。さよなら。さよなら。さよならだばかりだ。最後の力を振り絞って抜き放つ。ああ、ああ。世界が白く染まる。さよならだ。さよなら。さよなら。さよならだ。さよい！！ お前は俺の奴隷になるんだよ………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………",
"私は人間では無いのかもしれない、でも嫌いじゃない。嫌いじゃないから嫌いじゃないから嫌いじゃないから嫌いじゃないとは両立しない、大嫌い大嫌い大嫌い大嫌い嫌嫌大嫌嫌嫌嫌大嫌大嫌大嫌大嫌嫌大嫌嫌大嫌嫌好き嫌き大嫌い嫌大嫌嫌大嫌嫌嫌大嫌大嫌嫌嫌いあっていたのに、こんなに近くにいても怖がられるのか。怖すぎる。",
"誰かのせいでとかはない。\nちゃんと生きてられるのは、一人や二人ではないから。\nちゃんと、好きな人が出来て、好きな場所に泊まれるから。\nちゃんと、好きな人と一緒に居られる、そんな当たり前の世界が、お前の中にはあったのだと、改めて感じる。\n「もうやだ、やだよ、やだよ、やだよ、いやだよ、いやだよ、いやだよ、",
"面白いでしょ、感動。\nずっと見ていられる。\nずっとずっと！！。。。。。。ずっとずっと！！！。。。ずっと！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！",
"心がふわふわして楽しい♪\n\nでも触れてみたい！\n触れてみたい触れてみたい！\n触れて触れて触れて触れて触れて触れちゃいたい！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！いああああああああああぁああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ",
"自分のことって、旦那さんのことだってすっかり忘れてた。\nこれは大きな収穫かもしれない。\nこれからは、私がシンプルに生きるって決めた。\nシンプルになって当たり前が、シンプルになった。\nこれからは、旦那だちに手伝ってと言われても、手伝えるかわからないし、手伝えないのならば手伝わなければよかった。なんて、ふと思ったけど、このままここに立っていてもいいかと言うばかりで、私は一度家に戻ってからも、何も考えたくなくて、家の中から一歩も出たくないような、そんな暗い気持ちのまま、壁画を眺めていた。",
"眠い。また明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\n\nまた明日。\nまたせよラヂック。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。\nまた明日。また明日。\nまた明日いあっという間に\nまた1週間。\n今日は長かった。\n最後まで読んでて飽きなかった。"
"誘惑されないように、私は寝ながら充電してるのかな。誘惑されても起きない人少なくないと聞くけど、私の身体は充電してるのかな。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。誘惑されたい。"
]
    msg = random.choice(words)
    snd= Sender(name ="クソ野郎ちゃん", icon_url ="https://reiwacity-linebot.s3-ap-northeast-1.amazonaws.com/icon.jpg")
    text_message = TextSendMessage(msg, sender=snd)
    return text_message
