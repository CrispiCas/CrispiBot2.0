import discord

async def set_state(message, client, send):
        mesl = message.content
        action = str(message.content).split(' ')[1]
        if action == 'game':
            newsta = str(mesl).split(' ')[2:]
            newsta = str(newsta).replace("['", '').replace("']", '').replace("'", '').replace(",", '')

            if len(newsta) < 128:
                await client.change_presence(activity=discord.Game(name=newsta))
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
                embed.add_field(name='**Neuer Status!**',
                                value=f'Der neue Status ist: Spielt __{newsta}__')
                await send(embed=embed)

            else:
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
                embed.add_field(name='***__Error__***', value='Der Status ist zu lang')
                await send(embed=embed)
