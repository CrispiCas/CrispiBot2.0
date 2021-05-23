import discord
import toml

config = toml.load('./config/config.toml')
prefix = config['prefix']

async def docs(message):
    if message.content.lower() == f'{prefix}docs message':
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
        embed.add_field(name=f'Die docs zu Message',
                        value='[message-docs](https://discordpy.readthedocs.io/en/stable/api.html#message)')
        embed.set_footer(text=f"{prefix} message")

        await message.channel.send(embed= embed)

    elif message.content.lower() == f'{prefix}docs delete':
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
        embed.add_field(name=f'Die docs zu delete',
                        value='[deleted message reverences](https://discordpy.readthedocs.io/en/stable/api.html#deletedreferencedmessage), '
                              '[message delete event](https://discordpy.readthedocs.io/en/stable/api.html#rawmessagedeleteevent) ')

        await message.channel.send(embed=embed)

    elif message.content.lower() == f'{prefix}docs embed':
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
        embed.add_field(name=f'Die docs zu embeds',
                        value='[embed-docs](https://discordpy.readthedocs.io/en/stable/api.html#embed)')
        embed.set_footer(text=f'{prefix}docs embed')

        await message.channel.send(embed=embed)

    elif message.content.lower() == f'{prefix}docs' :
        pass

