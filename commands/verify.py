import discord
import toml

config = toml.load('./config/config.toml')
Rolle = config["rolle"]

async def verify(message):

    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=Rolle))
    await message.delete()