import random
import discord


async def the_dice(message, prefix):
    userIdgesplitet = str(message.author).split("#", 1)[0]
    rand = random.randint(1,6)
    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")



    embed.add_field(name=f"{userIdgesplitet}",
                    value=f"du hast eine {rand} gewürfelt ")
    embed.set_footer(text=f'{prefix}dice')
    await message.channel.send(embed=embed)