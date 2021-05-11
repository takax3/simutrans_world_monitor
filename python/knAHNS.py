# -*- coding: utf-8 -*- 
# ヘルプなど

import discord

knAHNSs = {}

# 記事一覧など
knAHNSs['list'] = discord.Embed(title="カテゴリーを指定してください。", description="現在存在するカテゴリーは次の通りです。", color=0xff0000)
knAHNSs['list'].add_field(name="ミーム", value="AHNSの各ミームを解説", inline=True)
knAHNSs['list'].add_field(name="ツール", value="AHNS関係のツールを解説", inline=True)
knAHNSs['list'].add_field(name="先鋭語", value="地理界隈発祥とされる各ネットスラングを解説", inline=True)
knAHNSs['list'].add_field(name="AHNS1", value="AHNS1について解説", inline=True)
knAHNSs['list'].add_field(name="AHNS2", value="AHNS2について解説", inline=True)
knAHNSs['list'].add_field(name="AHNS-F1", value="AHNS-F1について解説", inline=True)
knAHNSs['list,ミーム'] = discord.Embed(title="カテゴリー:ミーム", description="ミームカテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,ミーム'].add_field(name="横手車庫", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="おそロシア", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="あほなす", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="OTNP", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="○○はいくら○○してもかまいません", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="下着", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="見納め", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="Kitakyu_Simuする", value="​", inline=True)
knAHNSs['list,ミーム'].add_field(name="なんだ、君？一体、揉めるのか？", value="​", inline=True)
knAHNSs['list,ツール'] = discord.Embed(title="カテゴリー:ツール", description="ツールカテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,ツール'].add_field(name="AHNSbot", value="​", inline=True)
knAHNSs['list,ツール'].add_field(name="らくらくNS", value="​", inline=True)
knAHNSs['list,ツール'].add_field(name="これなにAHNS", value="​", inline=True)
knAHNSs['list,先鋭語'] = discord.Embed(title="カテゴリー:先鋭語", description="先鋭語カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,先鋭語'].add_field(name="先鋭語", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="劣っている", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="全謬", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="爆劣", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="封鎖", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="打鋲", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="収鋲", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="爆優", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="廃止", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="無謬", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="瘧害", value="​", inline=True)
knAHNSs['list,先鋭語'].add_field(name="優れている", value="​", inline=True)
knAHNSs['list,AHNS1'] = discord.Embed(title="カテゴリー:AHNS1", description="AHNS1カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,AHNS1'].add_field(name="横手車庫", value="​", inline=True)
knAHNSs['list,AHNS1'].add_field(name="足立区", value="​", inline=True)
knAHNSs['list,AHNS2'] = discord.Embed(title="カテゴリー:AHNS2", description="AHNS2カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,AHNS2'].add_field(name="おそロシア", value="​", inline=True)
knAHNSs['list,AHNS2'].add_field(name="法力", value="​", inline=True)
knAHNSs['list,AHNS-F1'] = discord.Embed(title="カテゴリー:AHNS-F1", description="AHNS-F1カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,AHNS-F1'].add_field(name="OTNP", value="​", inline=True)
knAHNSs['list,AHNS-F1'].add_field(name="先鋭急行", value="​", inline=True)
knAHNSs['list,AHNS-T1'] = discord.Embed(title="カテゴリー:AHNS-T1", description="AHNS-T1カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,AHNS-T1'].add_field(name="AHNS-T1", value="​", inline=True)
knAHNSs['list,参加者'] = discord.Embed(title="カテゴリー:参加者", description="参加者カテゴリーの現在存在する記事は次の通りです。", color=0x00ff00)
knAHNSs['list,参加者'].add_field(name="​", value="​", inline=True)
knAHNSs[''] = discord.Embed(title="記事名を指定してください。", value="​", description="このコマンドの正しい使用方法は、`?これなにAHNS,<記事名/list>,[カテゴリー]`です。", color=0xff0000)

#ミームカテ 合計9記事
#初期記事 合計3記事
knAHNSs['横手車庫'] = discord.Embed(title="横手車庫", description="**横手車庫（よこてしゃこ）**とは、AHNS1の都市「横手」付近に創急電鉄の手によって建設されたクソデカい車庫の事である。\n\n創急電鉄は、開業当初より時間調整機能を本車庫に集中させており、後年本数が多くなった結果、これまでにないような規模の車庫が出来上がった。その規模は供用部分だけでも2層106線、未供用部分を合わせると3層194線という非常に大規模なものになった。一部では「103系の全製造車両を収容できる規模の車庫」などとも言われている。", color=0x00ff00)
knAHNSs['おそロシア'] = discord.Embed(title="おそロシア", description="**おそロシア（おそろしあ）**とは、AHNS2のマップ南東の海上に存在した都市である。\n\n実際の設置形態としては、海上にポツンと役所のみが存在しており、その役所に300万人が住んでいるという計算であった。最寄り駅であるおそロシア駅は、1秒間に約200人の旅客が発生していた。", color=0x00ff00)
knAHNSs['あほなす'] = discord.Embed(title="あほなす", description="**あほなす（あほなす）**とは、AHNSの俗称である。ちなみに、正式な読み方は「あはんす」である。\n\nこの俗称の起源は、AHNS設立以前の2019年7月にNANSのDiscordサーバーで鯖主が「AHNS←ないです」と発言した際にかわごえが「あほなす」と返したことである。ここからAHNS設立までは正式名称が不明であったが、AHNS設立に伴い正式名称が「あはんす」であることが確定した。その後、2021年のエイプリルフールでサーバー名称が1日限りで「あほなす」に変更され公式化された。", color=0x00ff00)
# 21/05/04追加記事 合計1記事
knAHNSs['OTNP'] = discord.Embed(title="OTNP", description="【性的な記述あり！閲覧注意！】閲覧したい方は黒塗りされている部分をクリックもしくはタップしてください。\n||**OTNP（おーてぃーえぬぴー）**とは、男性器を模したネタアドオンである。\n\n休日自衛隊氏の制作で、JHNSに導入されたのち、AHNSではAHNS-F1の1回目のPak更新で導入された。しかし、AHNSでは賛否両論で、本アドオンに関する苦情が頻発した。その後、名指しこそされていないが「『公序良俗に反すると思われるアドオン』の使用にあたって各参加者の感情に配慮するよう」サーバー管理者の通知があった上、Pakset作成者からも「次回のPak更新から削除する」という旨の発言があった。||", color=0x00ff00)
# 21/05/11追加記事 合計5記事
knAHNSs['○○はいくら○○してもかまいません'] = discord.Embed(title="○○はいくら○○してもかまいません", description="**○○はいくら○○してもかまいません（○○はいくら○○してもかまいません）**とは、高鷲構文の一つである。\n\n元ネタは沖縄で性犯罪を起こした際の高鷲というtwitterユーザーの迷言「ちんちんはいくら揉んでもかまいません」である。当時高鷲から発せられた迷言はこれ以外にもいくつかあるが、五七五で語感が良いことなどからコピペ化され、現在でも改変されて頻繁に使用されている。", color=0x00ff00)
knAHNSs['ちんちんはいくら揉んでもかまいません'] = discord.Embed(title="○○はいくら○○してもかまいません", description="**○○はいくら○○してもかまいません（○○はいくら○○してもかまいません）**とは、高鷲構文の一つである。\n\n元ネタは沖縄で性犯罪を起こした際の高鷲というtwitterユーザーの迷言「ちんちんはいくら揉んでもかまいません」である。当時高鷲から発せられた迷言はこれ以外にもいくつかあるが、五七五で語感が良いことなどからコピペ化され、現在でも改変されて頻繁に使用されている。", color=0x00ff00)
knAHNSs['下着'] = discord.Embed(title="下着", description="**下着（したぎ）**とは、AHNSサーバー内のクソロールである。\n\n元ネタは当サーバーの参加者であるきたきゅー氏のニックネーム「るしあちゃんの下僕」をかわごえが「るしあちゃんの下着」に空目したことである。その後、ある日の夜クソロールを作る流れになりそのクソロールの名称が下着になったことでクソロールの名称として定着した。", color=0x00ff00)
knAHNSs['見納め'] = discord.Embed(title="見納め", description="**見納め（みおさめ）**とは、何かを廃止することを意味する単語である。\n\n元ネタとしては、あるtwitterユーザーがバスの注意ステッカーを無断で剥がして持ち帰った人が当該行為の事を「見納めにしました」と発言したことである。ここから転じて、AHNSで使用される「何かを廃止すること」を意味する単語に変化した。", color=0x00ff00)
knAHNSs['Kitakyu_Simuする'] = discord.Embed(title="Kitakyu_Simuする", description="**Kitakyu_Simuする（きたきゅーしむする）**とは、地形を平坦化することを意味する単語である。\n\n語源は参加者のきたきゅー氏が毎回大規模な地形改変を含む平坦化を行うところから来ており、そこから転じてこのように動詞として使われるようになった。余談ではあるが、同氏の地形平坦化は、AHNS1のものが過去最大規模であり、その平坦化はかわごえ氏と共同して行われ、きたきゅー氏の会社は過去最高額の赤字を記録した。", color=0x00ff00)
knAHNSs['なんだ、君？一体、揉めるのか？'] = discord.Embed(title="なんだ、君？一体、揉めるのか？", description="**なんだ、君？一体、揉めるのか？（なんだ、きみ？いったい、もめるのか？）**とは、twitterユーザーであるさとちゃん氏によって発せられた迷言である。\n\nこの迷言を発したさとちゃん氏はその特徴的な句読点や「一体」という単語の使用方法により、近年鉄道界隈で注目を集めており、この迷言はさとちゃん氏がさらに注目を集める一因となった。", color=0x00ff00)


#ツールカテ 合計3記事
#初期記事 合計2記事
knAHNSs['AHNSbot'] = discord.Embed(title="AHNSbot", description="**AHNSbot（あはんすぼっと）**とは、Discord上でAHNSゲーム内の様々な情報を提供するbotである。\n\nAHNSbotは、その動作にSimutrans world monitor( <https://github.com/teamhimeh/simutrans_world_monitor/blob/main/README.md> )をカスタマイズしたものを使用している。本記事では、主なカスタマイズ部分の仕様について記載する。本家Simutrans world monitorの仕様は上記のリンクを、コマンドの詳細については`?help` を参照されたい。\n\nAHNSbot独自の仕様として、コマンドの詳細を返す`?help` コマンドや英語でのコマンド入力の実装、文体の標準語化が行われている。さらに、らくらくNS( <https://github.com/ahakuoku/rakurakuNS/blob/main/readme.md> )と連携し、オートセーブの予告やサーバーダウンの通知なども行われている。また、おまけ機能として百科事典のようなテキストを返す`?これなにAHNS` コマンドや隠しコマンドが実装されている。", color=0x00ff00)
knAHNSs['らくらくNS'] = discord.Embed(title="らくらくNS", description="**らくらくNS（らくらくえぬえす）**とは、鯖主が開発・公開しているNSの管理を自動化するソフトである。\n\nらくらくNSそのものはAHNSと直接関係はないが、元々本ソフトはAHNS向けに開発されているなどAHNSとのかかわりが深いため、これなにAHNSでの解説を行う。詳細な仕様については公式のreadme( <https://github.com/ahakuoku/rakurakuNS/blob/main/readme.md> )を参照されたい。\n\nらくらくNSは、サーバーダウン時の自動復旧、任意の間隔でのオートセーブ、さらに付随して必要な動作を自動で行うソフトであり、コードはbatで書かれている。python移植の構想もあるものの、2021年4月現在、進捗はみられていない。らくらくNSのような自動化ソフトは他にも存在するが、特徴的な機能としてはSimutrans world monitor経由でのDiscord連携機能が存在する。", color=0x00ff00)
# 21/05/05追加記事 合計1記事
knAHNSs['これなにAHNS'] = discord.Embed(title="これなにAHNS", description="**これなにAHNS（これなにあはんす）**とは、AHNSbotのコマンドの一つである。\n\nこれなにAHNSは、Wikiのような情報を返すコマンドであり、2021年5月現在、この記事を含め29記事が存在する。その設立は「Wiki形式にすると管理が面倒になる事が目に見えている」というのが理由の一つであり、本コマンドはその代替を担うものとされている。また、最終的な目標は「AHNS関連の全ての情報を網羅する」ことではあるが、その目標を達成するにあたって、（特にセンシティブな話題に触れた）記事には中立性が求められるが、記事作成の優先度はなく、この目標を少しでも早く達成するため、 <#780726003739263046> での記事・カテゴリー作成申請を受け付けている。", color=0x00ff00)

#先鋭語カテ 合計13記事
#初期記事 合計6記事
knAHNSs['先鋭語'] = discord.Embed(title="先鋭語", description="**先鋭語（せんえいご）**とは、地理界隈発祥とされるインターネットスラングのことである。AHNSでよく使われる先鋭語として「爆劣」「全謬」「封鎖」などが存在している。現在のところ一般公開されている辞典は存在しない。", color=0x00ff00)
knAHNSs['京津鯖語録'] = discord.Embed(title="京津鯖語録", description="**京津鯖語録（けいしんさばごろく）**とは、かつて京津鯖Wikiに存在していたページである。\n\n先鋭語を多く収録していた事に加え、一般公開されている先鋭語辞典が存在しないため、決して先鋭語辞典ではないながらも唯一の先鋭語辞典として重宝された。繰り返しになるが、あくまで先鋭語辞典ではないため、先鋭語でないものも含まれている。これなにAHNSに収録されている先鋭語のほとんどはこの京津鯖語録からの引用である。", color=0x00ff00)
knAHNSs['劣っている'] = discord.Embed(title="劣っている", description="**劣っている（おとっている）**とは、物事がよろしくない様子を意味する先鋭語である。対義語は優れている。", color=0x00ff00)
knAHNSs['全謬'] = discord.Embed(title="全謬", description="**全謬（ぜんびゅう）**とは、全てが間違っていることを意味する先鋭語である。対義語は無謬。", color=0x00ff00)
knAHNSs['爆劣'] = discord.Embed(title="爆劣", description="**爆劣（ばくれつ）**とは、激しく劣っているさまを意味する先鋭語である。対義語は爆優。", color=0x00ff00)
knAHNSs['封鎖'] = discord.Embed(title="封鎖", description="**封鎖（ふうさ）**とは、誰かをブロックすることを意味する先鋭語である。", color=0x00ff00)
# 21/04/27追加分 合計6記事
knAHNSs['打鋲'] = discord.Embed(title="打鋲", description="**打鋲（だびょう）**とは、地図上に鋲を指してピン止めすることを意味する先鋭語である。", color=0x00ff00)
knAHNSs['収鋲'] = discord.Embed(title="収鋲", description="**収鋲（しゅうびょう）**とは、地図上の行きたい場所に刺した鋲を回収しに、現地へ訪れることを意味する先鋭語である。AHNSでは、<#689888697222693021>に投稿されたアドオンをダウンロードしてPak化済みという意味でも用いられる。", color=0x00ff00)
knAHNSs['爆優'] = discord.Embed(title="爆優", description="**爆優（ばくゆう）**とは、激しく優れているさまを意味する先鋭語である。対義語は爆劣。", color=0x00ff00)
knAHNSs['廃止'] = discord.Embed(title="廃止", description="**廃止（はいし）**とは、何かを消すこと無くすことを意味する先鋭語である。", color=0x00ff00)
knAHNSs['無謬'] = discord.Embed(title="無謬", description="**無謬（むびゅう）**とは、理論・判断などに、誤りが無いことを意味する日本語の単語である。語感が先鋭語と似ているためかよく先鋭語と間違えられるが、実際は真面目な国語辞典にも掲載されているごく普通の日本語である。", color=0x00ff00)
knAHNSs['瘧害'] = discord.Embed(title="瘧害", description="**瘧害（おこりがい）**とは、新型コロナウイルスの事を指す先鋭語である。", color=0x00ff00)
# 21/04/29追加分 合計1記事
knAHNSs['優れている'] = discord.Embed(title="優れている", description="**優れている（すぐれている）**とは、物事が素晴らしく、優れていることを意味する先鋭語である。", color=0x00ff00)

#AHNS1カテ 合計1記事
#21/05/11追加分 合計1記事
knAHNSs['足立区'] = discord.Embed(title="足立区", description="**足立区（あだちく）**とは、AHNS1のマップ西部に存在する都市である。\n\n実際の設置形態としては、周囲の高度を高くし、中央に湖をしていた。さらに湖には「世界の足立区　メキシコシティ」「三日月湖と星の部分に神社があるから世界平和なトルクメニスタン」「赤ピクミンは火に強い　青ピクミンは溺れない　足立区民はチャリ盗む」といったマーカーが立てられていた。一方、それ以外は比較的まともで、「足立区内線」という鉄道路線や、多数のバス路線が存在していた。", color=0x00ff00)

#AHNS-T1カテ 合計1記事
#21/05/11追加分 合計1記事
knAHNSs['AHNS-T1'] = discord.Embed(title="AHNS-T1", description="**AHNS-T1（あはんす-てぃーわん）**とは、OTRPのデバッグを目的として開催されたサーバーである。\n\n2020年10月10日～2020年12月10日までの開催で、参加者は過去最少の4名。\n本戦などとの同時開催を見越し、専用チャンネルまで作られたが、いざ開かれると上述の通り参加者が少なく、さらに4名中1名は末期からの途中参加、2名はほとんど放置するという前代未聞の事態に発展した。さらにOTRPの開発終了が追い打ちをかけたため、今後AHNS-T2が開催されることはないと思われる。現在は一部の専用チャンネルがbotのテスト目的に転用されるも、現在はそのような用途での使用もなくなっている。", color=0x00ff00)

#AHNS2カテ 合計1記事
#21/05/11追加分 合計1記事
knAHNSs['法力'] = discord.Embed(title="法力", description="**法力（ほうりき）** とは、AHNS2のマップ東部に存在する高速道路の直角カーブである。\n\n実際の設置形態としては、高速道路の上下線間に法力空港という空港が存在し、徳島方面線が直角カーブにより空港を迂回している状態となっている。\n語源としては、本設置物の近くに建てられた「高速道路を直角に曲げる法力」というマーカーであり、法力空港は開港当初は別の名称であった。", color=0x00ff00)

#AHNS-F1カテ 合計1記事
# 21/05/04追加分 合計1記事
knAHNSs['先鋭急行'] = discord.Embed(title="先鋭急行", description="**先鋭急行（せんえいきゅうこう）**とは、AHNS-F1の鉄道会社である。\n\n先鋭急行が輸送対象とした旅客は、初期のごく一部の例外を除き一等旅客のみで、また二等旅客を軽蔑するような発言を多数行ったため、多数の参加者からヘイト企業扱いされることとなった。", color=0x00ff00)