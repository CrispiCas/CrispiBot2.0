import discord

async def help_command(message, prefix):
    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

    embed.add_field(name=f'{prefix}help', value='Zeigt alle Befehle\n'
                                                f'**{prefix}dice\n**'
                                                'ein einfacher Würfel command\n'
                                                f'**{prefix}docs (message, delete, embed)\n**'
                                                'Hier kannst du dir verschiedene Discord.py docs anzeigen lassen\n'
                                                f'**{prefix}GitHub**\n'
                                                'Leitet dich zu meinem GitHUb reporitory weiter \n'
                                                f'**{prefix}Hash: (Dein Wort/satz)**\n'
                                                'Gibt den hashcode von einem Wort/satz aus')






    #embed.add_field(name=f'{prefix}hash (dein Wort/Satz)', value='Gibt den hashcode zu einem Wort aus\n')
    await message.channel.send('Meine commands:')
    await message.channel.send(embed=embed)