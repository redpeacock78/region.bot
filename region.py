import discord
import os
import subprocess

client = discord.Client()

region_japan = 'Japan'
region_london = 'London'
region_hongkong = 'Hongkong'

change_before = 'Change to '
change_after = 'Changed to '

@client.event
async def on_ready():
    print('Botを起動しました。')

@client.event
async def on_message(message):
    #日本
    if message.content.startswith('#region japan'):
        await message.channel.send(change_before + region_japan)
        await message.guild.edit(region='japan')
        await message.channel.send(change_after + region_japan)
    #ロンドン
    elif message.content.startswith('#region london'):
        await message.channel.send(change_before + region_london)
        await message.guild.edit(region='london')
        await message.channel.send(change_after + region_london)
    #香港
    elif message.content.startswith('#region hongkong'):
        await message.channel.send(change_before + region_hongkong)
        await message.guild.edit(region='hongkong')
        await message.channel.send(change_after + region_hongkong)
    #生存確認
    elif message.content.startswith('#alive'):
        reply = 'I am alive!'
        await message.channel.send(reply)
    #バージョン表示
    elif message.content.startswith('#version'):
        version = '0.0.1'
        await message.channel.send("Region_Bot/" + version)
    #ヘルプを表示
    elif message.content.startswith('#help'):
        help = 'USAGE:\n'\
               'Commands:\n'\
               ' #region [japan,london,hongkong]\n'\
               '         Change the server region.\n'\
               ' #alive\n'\
               '         Make a bot survival check.\n'\
               ' #version\n'\
               '         The version of this bot.\n'\
               ' #help\n'\
               '         Display help.'
        await message.channel.send(help)

client.run(os.environ.get('ACCESS_TOKEN_KEY'))
