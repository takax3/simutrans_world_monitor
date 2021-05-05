# -*- coding: utf-8 -*- 
# ヘルプなど

import discord

helps = {}

helps['?ヘルプ'] = discord.Embed(title="コマンド一覧", description="本botで使用できるコマンドは次の通りです。\n※helpコマンド・これなにAHNSコマンド以外はSimutrans起動時以外使用できません。\n引数の区切りはコンマ(`,`)で行います。\n`<>`のカッコ内は、その引数が必須であることを示します。（カッコは外してください）\n`[]`のカッコ内は、その引数がオプションであることを示します。（カッコは外してください）", color=0x00ff00)
helps['?ヘルプ'].add_field(name="`?help`", value="本botのヘルプを返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?wait,<駅名>,[エントリ数]`", value="指定された停車場の待機客およびその行き先を返します。エントリ数のデフォルト値は5です。", inline=False)
helps['?ヘルプ'].add_field(name="`?player`", value="ゲームに参加している会社一覧と、その番号を返します。ここで返される番号は、プレイヤー番号を指定するコマンドで使用します。", inline=False)
helps['?ヘルプ'].add_field(name="`?akabo,[プレイヤー番号]`", value="指定した会社に所属する停車場で、いわゆる赤棒が立っている駅とその待機客を返します。プレイヤー番号の指定がない場合は、すべての会社の赤棒を返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?time`", value="現在の年と月を返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?finance`", value="各会社の資金を返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?route,<プレイヤー番号>,[路線属性]`", value="指定したプレイヤーの路線番号と路線名を一覧で返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?halt,<路線番号>,[停車場数]`", value="指定した路線のスケジュール上にある停車駅を順番に返します。3つ目のパラメーターを指定すると、路線上にある駅を利用者順でソートして返します。", inline=False)
helps['?ヘルプ'].add_field(name="`?これなにAHNS,<記事名/list>,[カテゴリ名]`", value="指定した名称の記事を返します。listオプションは、指定したカテゴリ内の記事一覧を返します。", inline=False)
helps['?help'] = discord.Embed(title="コマンド一覧", description="本botで使用できるコマンドは次の通りです。\n※helpコマンド・これなにAHNSコマンド以外はSimutrans起動時以外使用できません。\n引数の区切りはコンマ(`,`)で行います。\n`<>`のカッコ内は、その引数が必須であることを示します。（カッコは外してください）\n`[]`のカッコ内は、その引数がオプションであることを示します。（カッコは外してください）", color=0x00ff00)
helps['?help'].add_field(name="`?help`", value="本botのヘルプを返します。", inline=False)
helps['?help'].add_field(name="`?wait,<駅名>,[エントリ数]`", value="指定された停車場の待機客およびその行き先を返します。エントリ数のデフォルト値は5です。", inline=False)
helps['?help'].add_field(name="`?player`", value="ゲームに参加している会社一覧と、その番号を返します。ここで返される番号は、プレイヤー番号を指定するコマンドで使用します。", inline=False)
helps['?help'].add_field(name="`?akabo,[プレイヤー番号]`", value="指定した会社に所属する停車場で、いわゆる赤棒が立っている駅とその待機客を返します。プレイヤー番号の指定がない場合は、すべての会社の赤棒を返します。", inline=False)
helps['?help'].add_field(name="`?time`", value="現在の年と月を返します。", inline=False)
helps['?help'].add_field(name="`?finance`", value="各会社の資金を返します。", inline=False)
helps['?help'].add_field(name="`?route,<プレイヤー番号>,[路線属性]`", value="指定したプレイヤーの路線番号と路線名を一覧で返します。", inline=False)
helps['?help'].add_field(name="`?halt,<路線番号>,[停車場数]`", value="指定した路線のスケジュール上にある停車駅を順番に返します。3つ目のパラメーターを指定すると、路線上にある駅を利用者順でソートして返します。", inline=False)
helps['?help'].add_field(name="`?これなにAHNS,<記事名/list>,[カテゴリ名]`", value="指定した名称の記事を返します。listオプションは、指定したカテゴリ内の記事一覧を返します。", inline=False)

helps['?これなにAHNS'] = discord.Embed(title="記事名を指定してください。", value="​", description="このコマンドの正しい使用方法は、`?これなにAHNS,<記事名/list>,[カテゴリー]`です。", color=0xff0000)
# この先隠しコマンドあり！閲覧注意！







































































helps['?ahakuoku'] = discord.Embed(title="ahakuoku", description="ahakuokuさんは、128jpの公開鯖の鯖主としてAHNSの創設に尽力し、AHNSに自由の雰囲気を築くために多大な功績を残した人です。どうかこのメッセージを消さないでください。", color=0x00ff00)

helps['?かわぎえ'] = discord.Embed(title="かわぎえ", description="ぎえーｗｗｗｗｗ", color=0x00ff00)

helps['?お前を消す方法'] = discord.Embed(title="お前を消す方法", description="邪魔だったよね、ごめんね。もう少し役に立てるように頑張るよ。", color=0x00ff00)

helps['?鯖主の最寄り駅'] = discord.Embed(title="お前を消す方法", description="<:kamioooka_A:800358960325853254><:stop:800361810506022972>\n<:kamioooka_B:800359063513858058><:stop:800361810506022972>", color=0x00ff00)

helps['?OTNP'] = discord.Embed(title="OTNP", description="でっけえ男性器 飛んでるよ 飛んでるよ", color=0x00ff00)

helps['?デドロイト市警だ！'] = discord.Embed(title="デドロイト市警だ！", description="君？嘘をつくのは、一体良くない。", color=0x00ff00)

helps['?ヘイト行為'] = discord.Embed(title="ヘイト行為", description="仏塔鉄道は1等旅客専業となりました。全謬爆劣2等旅客はバスでもﾂｶｯﾃﾛ", color=0x00ff00)

helps['?イオン'] = discord.Embed(title="イオン", description="ヘイト企業イオンは謝罪しろ！", color=0x00ff00)

helps['?高鷲'] = discord.Embed(title="高鷲", description="ここで一句\n\nちんちんは\n​　いくら揉んでも\n​　　かまいません", color=0x00ff00)