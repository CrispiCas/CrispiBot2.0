import discord
import toml
from commandexe import Commands

config = toml.load('./config/config.toml')
token = config["token"]
prefix = config["prefix"]
owner = config["owner"]
konsole = config["konsole"]
bot = config["bot"]
status1 = config["status"]
print(prefix)


client = discord.Client()

@client.event
async def on_ready():
    print('huhu ich bin online')
    await client.change_presence(activity=discord.Game(name=status1))


@client.event
async def on_message(message):
    await Commands.commands(message, client, prefix, owner)

    print(message.author)

client.run(token)