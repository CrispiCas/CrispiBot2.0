from os import replace
import sqlite3
from discord.message import Message
import time
import discord
import toml

config = toml.load('./config/config.toml')
path = config['path']


con = sqlite3.connect(path)

cur = con.cursor()

async def check_blacklist(message, owner, client):

    mes = str(message.content.lower()).replace('.', '').replace(' ', '').replace('-', '').replace('_', '')
    for line in open('./data/blacklist.txt'):
        if mes.__contains__(line.replace("\n", "")):
            await blacklistbd(message)
            await message.delete()


async def adbl(message, prefix, owner):
    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    if userID == owner:
        blacklistword = message.content.replace(f'{prefix}adbl ', '')
        if len(blacklistword) > 0:
            open('data/blacklist.txt', 'a').write(blacklistword + '\n')
            embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com/%22")
            embed.add_field(name='Neues Blacklist Word', value=f'Das neue Wort ist: {blacklistword}')
            await message.channel.send(embed=embed)
            time.sleep(3)
            await message.channel.purge(limit = 2)

        else:
            await message.channel.send('***__Error__***')
    else:
        await message.channel.send('Du hast keine rechte hehe')




async def clear_command(message, prefix):
    limit1 = message.content.replace(f'clear ', '')
    print(limit1)
    #await message.channel.purge(limit = limit1)


async def blacklistbd(message):
    cur.execute("CREATE TABLE IF NOT EXISTS blacklistwords (name text PRIMARY KEY, blacklistnr number)")

    username = message.author.id

    try:
        cur.execute(f"INSERT INTO blacklistwords VALUES ('{username}', 0)")
        con.commit()
    except:
        pass

    
    cur.execute(f'UPDATE blacklistwords SET blacklistnr = blacklistnr + 1 WHERE name = "{username}"')
    con.commit()

    checknr = cur.execute(f"SELECT blacklistnr FROM blacklistwords WHERE name = '{username}'")
    checknr = cur.fetchall()
    checknr = str(checknr).removeprefix('[(').removesuffix(',)]')
    checknr = int(checknr)

    if checknr == 10:
        await message.channel.send('Bitte keine Wörter mehr in die Richtung')

    if checknr == 15:
        await message.channel.send('Letzt Verwarnung...')

    if checknr == 16:
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name='Yeee ich hab was böses getan'))


async def reset_blacklistnr(message, prefix, owner):
    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    if userID == owner:
        username = message.content.replace(f'{prefix}resetblnr ', '') 
        checknr = cur.execute(f"SELECT blacklistnr FROM blacklistwords WHERE name = '{username}'")
        checknr = cur.fetchall()
        checknr = str(checknr).removeprefix('[(').removesuffix(',)]')
        await message.channel.send(f'Die Blacklistnr von {username} wurde resetet')
        try:
            checknr = int(checknr)
        except:
            embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
            embed.add_field(name = '***__Error__***', value='Falsche User Id oder der User ist nicht vorhanden')
            await message.channel.send(embed = embed)

        cur.execute(f'UPDATE user SET blacklistnr = blacklistnr - {checknr} WHERE name = "{username}"')
        con.commit()

    else:
        await message.channel.send('Du hast keine rechte hehe')


async def blavklistnr_abfrage(message, prefix, owner):
    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    if userID == owner:
        username = message.content.lower().replace(f'{prefix}getblnr ', '')
        checknr = cur.execute(f"SELECT blacklistnr FROM blacklistwords WHERE name = '{username}'")
        checknr = cur.fetchall()
        checknr = str(checknr).removeprefix('[(').removesuffix(',)]')
        userId = message.content.replace(f'{prefix}getblnr ', '')
        try:
            checknr = int(checknr)
            await message.channel.send(f'{userId} hat {checknr} Blacklisted wörter geschrieben')
        except:
            embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
            embed.add_field(name = '***__Error__***', value='Falsche UserID oder User nicht in der Datenbank hinterlegt')

            await message.channel.send(embed = embed)

    else:
        await message.channel.send('Du hast keine rechte hehe')
