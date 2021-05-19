import sqlite3
from discord.message import Message
import time
import discord


con = sqlite3.connect('/Users/username/Documents/Python/CrispiBot2.0/databases/blacklistdb.sqlite')

cur = con.cursor()

async def check_blacklist(message, owner):

    mes = str(message.content.lower()).replace('.', '').replace(' ', '')
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
    cur.execute("CREATE TABLE IF NOT EXISTS user (name text PRIMARY KEY, blacklistnr number)")

    username = message.author

    try:
        cur.execute(f"INSERT INTO user VALUES ('{username}', 0)")
        con.commit()
    except:
        pass

    
    cur.execute(f'UPDATE user SET blacklistnr = blacklistnr + 1 WHERE name = "{username}"')
    con.commit()

    checknr = cur.execute(f"SELECT blacklistnr FROM user WHERE name = '{username}'")
    checknr = cur.fetchall()
    checknr = str(checknr).removeprefix('[(').removesuffix(',)]')
    checknr = int(checknr)

    if checknr == 15:
        pass
