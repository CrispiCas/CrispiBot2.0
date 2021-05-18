import discord


async def idea_command(message, prefix):
        messagesplit = message.content.replace(f"{prefix}idee:", "").replace(f'{prefix}idee', '')
        if len(messagesplit) > 0:
            l = open('logs/idea.txt', 'a')
            l.writelines(f'{message.author} hatte die Idee: {messagesplit}\n')
            l.close()
            #await message.channel.purge(limit=1)
            try:
                await message.delete()
            except:
                print()

            try:
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                embed.add_field(name="Deine Idee:",
                                value=f"{messagesplit}")
                await message.author.send(embed=embed)
            except:
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                embed.add_field(name="***__Error__***",
                                value=f"deine idee ist zu lang wurde aber notiert ;)")
                await message.author.send(embed=embed)

        else:
            embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
            embed.add_field(name='***__Error__***', value='Bitte eine Idee angeben')
            await message.channel.send(embed=embed)

