import hashlib
import discord

async def hasconverter(message, prefix):
    hash = message.content.replace(f'{prefix}hash ', '')
    h = hashlib.new('sha512')
    h.update(hash.encode())
    if len(hash) > 0:
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
        embed.add_field(name=f'Der Hash zu {hash}:',
                        value=f'{h.hexdigest()}')
        embed.set_footer(text=f'{prefix}hash: ')
        await message.channel.send(embed=embed)

    else:
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
        embed.add_field(name=f'***__Error__**',
                        value=f'Du musst schon etwas angeben was ich verschlüsseln soll ')
        embed.set_footer(text=f'{prefix}hash: ')
        await message.channel.send(embed=embed)