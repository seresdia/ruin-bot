#coding: utf-8

# 上記で取得したアプリのトークンを入力
BOT_TOKEN = "NDQwODM5MjU5OTUyNTEzMDI0.Dcn9Nw.x_6PgGF2UbZEFDPOcyAMkM_CDRc"

# パッケージのインポートとインスタンス作成
import discord
import re
import asyncio
import datetime
client = discord.Client()

# ログイン&準備が完了したら一度だけ実行される
@client.event
async def on_ready():
# ゲーム情報表示
    #await client.change_presence(activity=discord.Activity(name='serestialenigma|r!help',type=discord.ActivityType.listening),status=discord.Status.online,afk=False)
    await client.change_presence(activity=discord.Activity(name='music',type=discord.ActivityType.listening),status=discord.Status.online,afk=False)
    # コンソールにBOTとしてログインした名前とUSER-IDを出力
    print('Logged in as')
    print('BOT-NAME :', client.user.name)
    print('BOT-ID   :', client.user.id)
    print('現在稼働中！')

# メッセージを受信するごとに実行される
@client.event
async def on_message(message):

    # BOTとメッセージの送り主が同じ人なら処理しない
    if client.user == message.author:
            return
    if not message.author.bot:
        if message.content.startswith("おはよう"):
            await message.channel.send("( ・∇・)おはようるいん！")
        if message.content.startswith("おやすみ"):
            await message.channel.send("( ・∇・)おやすみるいん")
        if message.content.startswith("るいん君"):
            await message.channel.send("( ・∇・)なあに？")
        if message.content.startswith("ただいま"):
            await message.channel.send("( ・∇・)おかえりるいん")
        if message.content.startswith("帰宅"):
            await message.channel.send("( ・∇・)おかえりるいん")
        if message.content.startswith("にぎりずし"):
            await message.channel.send("( ・∇・)すしさんは現代の張飛とよばれてるいん")
        if message.content.startswith("射程の暴力"):
            await message.channel.send("( ・∇・)すしに対抗する唯一の手段るいん")
        if message.content.startswith("すし補正"):
            await message.channel.send("( ・∇・)すし補正の力は未知数るいん")
        if message.content.startswith("クソザコるいん"):
            await message.channel.send("(;・∇・)ひどいるいん！")
        if message.content.startswith("音楽"):
            await message.channel.send("( ・∇・)おすすめの音楽るいん https://youtu.be/A0tL9p4c9Gw https://youtu.be/LrNvBIqlkIM")
        if message.content.startswith("疲れた"):
            await message.channel.send("( ・∇・)おつかれるいん、よく休むといいるいん")
        if message.content.startswith("つかれた"):
            await message.channel.send("( ・∇・)おつかれるいん、よく休むといいるいん")
        if message.content.startswith("諦め"):
            await message.channel.send("( ・∇・)エクストリームナインホワイトフラッグスアイアムギブアップアタック！")
        if message.content.startswith("かわいい"):
            await message.channel.send("( ・∇・)照れるいん")
        if message.content.startswith("可愛い"):
            await message.channel.send("( ・∇・)照れるいん")
        if message.content.endswith("処刑") and message.content.startswith("ブラスター"):
            await message.channel.send("( ・∇・)ブラスターは甘えるいん")
        if message.content.startswith("おはすし"):
            await message.channel.send("( ・∇・)おはすしるいん！")
        if message.content.startswith("おやすし"):
            await message.channel.send("( ・∇・)おやすしるいん！")
        if message.content.startswith("火力"):
            await message.channel.send("( ・∇・)火力は正義！")
        if message.content.startswith("メギドフレイム"):
            await message.channel.send("( ・∇・)PCにダイレクトアタックるいん")
        if message.content.startswith("ラストプリズム"):
            await message.channel.send("( ・∇・)Fire a lifeform disintegration rainbow!")
        if re.match("<@!?%s>" % 440839259952513024,message.content):
            await message.channel.send('( ・∇・)' + message.author.name + 'さん、どうかしたるいん？')
# 現在時刻表示
        if message.content.startswith("今何時"):
            await message.channel.send('( ・∇・)今の時刻は' + datetime.datetime.now(tz=None).strftime('%H:%M') + 'るいん')
        if message.content.startswith("今なんじ"):
            await message.channel.send('( ・∇・)今の時刻は' + datetime.datetime.now(tz=None).strftime('%H:%M') + 'るいん')
        if message.content.startswith("いま何時"):
            await message.channel.send('( ・∇・)今の時刻は' + datetime.datetime.now(tz=None).strftime('%H:%M') + 'るいん')
        if message.content.startswith("いまなんじ"):
            await message.channel.send('( ・∇・)今の時刻は' + datetime.datetime.now(tz=None).strftime('%H:%M') + 'るいん')

    if message.content.startswith("KeyCE"):
        splited = message.content.split(maxsplit=1)
        if len(splited) >= 2:
            src = splited[1]
        #src = ''この左に変換させたい言葉を入れてください
            dst = src.translate({
                ord(u'あ'): u'la',
                ord(u'い'): u'lyai',
                ord(u'う'): u'li',
                ord(u'え'): u'lyiu',
                ord(u'お'): u'lu',
                ord(u'か'): u'lyue',
                ord(u'き'): u'le',
                ord(u'く'): u'lyeo',
                ord(u'け'): u'lo',
                ord(u'こ'): u'lyoa',
                ord(u'さ'): u'ca',
                ord(u'し'): u'cyai',
                ord(u'す'): u'ci',
                ord(u'せ'): u'cyiu',
                ord(u'そ'): u'cu',
                ord(u'た'): u'cyue',
                ord(u'ち'): u'ce',
                ord(u'つ'): u'cyeo',
                ord(u'て'): u'co',
                ord(u'と'): u'cyoa',
                ord(u'な'): u'ta',
                ord(u'に'): u'tyai',
                ord(u'ぬ'): u'ti',
                ord(u'ね'): u'tyiu',
                ord(u'の'): u'tu',
                ord(u'は'): u'tyue',
                ord(u'ひ'): u'te',
                ord(u'ふ'): u'tyeo',
                ord(u'へ'): u'to',
                ord(u'ほ'): u'tyoa',
                ord(u'ま'): u'fa',
                ord(u'み'): u'fyai',
                ord(u'む'): u'fi',
                ord(u'め'): u'fyiu',
                ord(u'も'): u'fu',
                ord(u'や'): u'ma',
                ord(u'ゆ'): u'mu',
                ord(u'よ'): u'mo',
                ord(u'ら'): u'fyue',
                ord(u'り'): u'fe',
                ord(u'る'): u'fyeo',
                ord(u'れ'): u'fo',
                ord(u'ろ'): u'fyoa',
                ord(u'わ'): u'yha',
                ord(u'を'): u'yhu',
                ord(u'ん'): u'yho',
                ord(u'が'): u'lyueq',
                ord(u'ぎ'): u'leq',
                ord(u'ぐ'): u'lyeoq',
                ord(u'げ'): u'loq',
                ord(u'ご'): u'lyoaq',
                ord(u'ざ'): u'caq',
                ord(u'じ'): u'cyaiq',
                ord(u'ず'): u'ciq',
                ord(u'ぜ'): u'cyiuq',
                ord(u'ぞ'): u'cuq',
                ord(u'だ'): u'cyueq',
                ord(u'ぢ'): u'ceq',
                ord(u'づ'): u'cyeoq',
                ord(u'で'): u'coq',
                ord(u'ど'): u'cyoaq',
                ord(u'ば'): u'tyueq',
                ord(u'び'): u'teq',
                ord(u'ぶ'): u'tyeoq',
                ord(u'べ'): u'toq',
                ord(u'ぼ'): u'tyoaq',
                ord(u'ぱ'): u'tyueqe',
                ord(u'ぴ'): u'teqe',
                ord(u'ぷ'): u'tyeoqe',
                ord(u'ぺ'): u'toqe',
                ord(u'ぽ'): u'tyoaqe',
                ord(u'ぁ'): u'laq',
                ord(u'ぃ'): u'lyaiq',
                ord(u'ぅ'): u'liq',
                ord(u'ぇ'): u'lyiuq',
                ord(u'ぉ'): u'luq',
                ord(u'ゃ'): u'maq',
                ord(u'ゅ'): u'muq',
                ord(u'ょ'): u'moq',
                ord(u'っ'): u'cyeoqe',
                })
            await message.channel.send('変換結果:' + dst)
        else:
            await message.channel.send("変換する文字が入っていないるいん")

    if message.content.startswith("RevCE"):
        splited = message.content.split(maxsplit=1)
        if len(splited) >= 2:
            src = splited[1]
        #src = ''この左に変換させたい言葉を入れてください
            newsrc = (src.replace("cyeoqe",'っ')
            .replace("tyoaqe",'ぽ')
            .replace("tyeoqe",'ぷ')
            .replace("tyueqe",'ぱ')
            .replace("lyiuq",'ぇ')
            .replace("lyaiq",'ぃ')
            .replace("tyoaq",'ぼ')
            .replace("tyeoq",'ぶ')
            .replace("cyoaq",'ど')
            .replace("tyueq",'ば')
            .replace("cyeoq",'づ')
            .replace("cyueq",'だ')
            .replace("cyiuq",'ぜ')
            .replace("cyaiq",'じ')
            .replace("lyoaq",'ご')
            .replace("lyeoq",'ぐ')
            .replace("lyueq",'が')
            .replace("toqe",'ぺ')
            .replace("fyoa",'ろ')
            .replace("teqe",'ぴ')
            .replace("fyeo",'る')
            .replace("fyue",'ら')
            .replace("fyiu",'め')
            .replace("fyai",'み')
            .replace("tyoa",'ほ')
            .replace("tyeo",'ふ')
            .replace("tyue",'は')
            .replace("tyiu",'ね')
            .replace("tyai",'に')
            .replace("cyoa",'と')
            .replace("cyeo",'つ')
            .replace("cyue",'た')
            .replace("cyiu",'せ')
            .replace("cyai",'し')
            .replace("lyoa",'こ')
            .replace("lyeo",'く')
            .replace("lyue",'か')
            .replace("lyiu",'え')
            .replace("lyai",'い')
            .replace("moq",'ょ')
            .replace("muq",'ゅ')
            .replace("maq",'ゃ')
            .replace("luq",'ぉ')
            .replace("liq",'ぅ')
            .replace("laq",'ぁ')
            .replace("toq",'べ')
            .replace("teq",'び')
            .replace("coq",'で')
            .replace("ceq",'ぢ')
            .replace("cuq",'ぞ')
            .replace("ciq",'ず')
            .replace("caq",'ざ')
            .replace("loq",'げ')
            .replace("leq",'ぎ')
            .replace("yho",'ん')
            .replace("yhu",'を')
            .replace("yha",'わ')
            .replace("la",'あ')
            .replace("li",'う')
            .replace("lu",'お')
            .replace("le",'き')
            .replace("lo",'け')
            .replace("ca",'さ')
            .replace("ci",'す')
            .replace("cu",'そ')
            .replace("ce",'ち')
            .replace("co",'て')
            .replace("ta",'な')
            .replace("ti",'ぬ')
            .replace("tu",'の')
            .replace("te",'ひ')
            .replace("to",'へ')
            .replace("fa",'ま')
            .replace("fi",'む')
            .replace("fu",'も')
            .replace("ma",'や')
            .replace("mu",'ゆ')
            .replace("mo",'よ')
            .replace("fe",'り')
            .replace("fo",'れ'))
            await message.channel.send('変換結果:' + newsrc)
        else:
            await message.channel.send("変換する文字が入っていないるいん")
    if message.content.startswith("r!help"):
        embed = discord.Embed(title="セレスティアルエニグマ変換機の説明るいん", description="太字になっているところがコマンドるいん", color=0xffaa00)
        embed.add_field(name="r!help", value="変換機の説明を表示するいん", inline=False)
        embed.add_field(name="KeyCE", value="日本語をセレスティアルエニグマに暗号化するいん", inline=False)
        embed.add_field(name="RevCE", value="セレスティアルエニグマを日本語に変換するいん", inline=False)
        await message.channel.send(embed=embed)


# APP(BOT)を実行
client.run(BOT_TOKEN)
