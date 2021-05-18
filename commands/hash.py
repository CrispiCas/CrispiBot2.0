import hashlib
import discord

async def hasconverter(message, prefix):
    hash = message.content.replace(f'{prefix}hash ', "")
    h = hashlib.new('sha512')
    h.update(hash.encode())

    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
    embed.add_field(name=f'Der Hash zu {hash}:',
                    value=f'{h.hexdigest()}')
    embed.set_footer(text=f'{prefix}hash: ')
    await message.channel.send(embed=embed)