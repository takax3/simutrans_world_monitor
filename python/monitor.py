# -*- coding: utf-8 -*- 
# pip install discord.py watchdog

import discord
import os
import config
import help
import knAHNS
from watchdog.observers import Observer
from libs.FileChangeHandler import FileChangeHandler
from libs.vars import *

FILE_CMD = config.DIRECTORY + '/file_io/cmd.txt'

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    channel = client.get_channel(config.CHANNEL_ID)
    await channel.send(embed=discord.Embed(title=config.TEXT_HELLO_TITLE, description=config.TEXT_HELLO_DESC, color=0x00ff00))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    channel = client.get_channel(config.CHANNEL_ID)
    # 指定チャンネルでの指定フォーマットの人間のメッセージのみ反応
    content: str = message.content.replace('？', '?').replace('，', ',').replace('、', ',').replace('ヘルプ', 'help').replace('knAHNS', 'これなにAHNS')
    AHNS_dictionary = content.find('?これなにAHNS')
    if message.author.bot or message.channel != channel or content[0]!='?' or len(content)<2:
        return
    elif content in help.helps :
        await channel.send(embed=help.helps[content])
        return
    elif content.lower().startswith('?reset') :
        if message.author.id != config.ADMIN:
            await channel.send(embed=discord.Embed(title=config.TEXT_RESET_TITLE_NOT_ADMIN, description=config.TEXT_RESET_DESC_NOT_ADMIN, color=0xff0000))
        else:
            with open(FILE_CMD, mode='w', encoding='utf-8') as f:
                f.write('empty')
            await channel.send(embed=discord.Embed(title=config.TEXT_RESET_TITLE, description=config.TEXT_RESET_DESC, color=0x00ff00))
        return
    elif AHNS_dictionary == 0 :
        knAHNS_1, knAHNS_2 = content.split(',', 1)
        if knAHNS_2 in knAHNS.knAHNSs:
            await channel.send(embed=knAHNS.knAHNSs[knAHNS_2])
            return
        else:
            embed=discord.Embed(title="指定された名前の記事はありません。", description="このコマンドの正しい使用方法は、`?これなにAHNS,<記事名/list>,[カテゴリー]`です。\nコマンド文にスペースが入っていたりすると正しく動作しません。", color=0xff0000)
            await channel.send(embed=embed)
            return
    with open(FILE_CMD, encoding='utf-8') as f:
        s = f.read()
        if s and not s.startswith('empty'):
            await channel.send(embed=discord.Embed(title=config.TEXT_BUSY_TITLE, description=config.TEXT_BUSY_DESC, color=0xff0000))
            return
    with open(FILE_CMD, mode='w', encoding='utf-8') as f:
        f.write(content[1:])
        set_waiting_message(await channel.send(embed=discord.Embed(title=config.TEXT_WAIT_TITLE, description=config.TEXT_WAIT_DESC, color=0x00ff00)))
        set_prev_out_hash(None)
        
def generate_io_files():
    os.makedirs(config.DIRECTORY+'/file_io', exist_ok=True)
    if not os.path.isfile(FILE_CMD):
        with open(FILE_CMD, mode='w', encoding='utf-8') as f:
            f.write('empty')

def start():
    generate_io_files()
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, config.DIRECTORY+'/file_io')
    observer.start()
    client.run(config.TOKEN)

# Botの起動とDiscordサーバーへの接続
start()