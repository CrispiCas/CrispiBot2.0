import discord

async def GitHub_command(message, prefix):
    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
    embed.add_field(name='Mein Github Profil:',
                    value='https://github.com/CrispiCas/CrispiBot2.0')
    embed.set_footer(text=f'{prefix}github')

    await message.channel.send(embed=embed)

