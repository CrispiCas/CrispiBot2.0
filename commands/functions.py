import random
import discord


#dice
async def the_dice(message, prefix):
    userIdgesplitet = str(message.author).split("#", 1)[0]
    rand = random.randint(1,6)
    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")



    embed.add_field(name=f"{userIdgesplitet}",
                    value=f"du hast eine {rand} gewürfelt ")
    embed.set_footer(text=f'{prefix}dice')
    await message.channel.send(embed=embed)

#GitHub
async def GitHub_command(message, prefix):
    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")
    embed.add_field(name='Mein Github Profil:',
                    value='https://github.com/CrispiCas/CrispiBot2.0')
    embed.set_footer(text=f'{prefix}github')

    await message.channel.send(embed=embed)

#log function
def logs(message):
    
    datum = str(message.created_at).split('.')
    datum.pop()
    DatumZeit = str(datum).removeprefix("['").removesuffix("']")
    datumzeit = DatumZeit.split(' ')
    Zeit = datumzeit.pop()
    Datum = str(datumzeit).removeprefix("['").removesuffix("']")

    f = open('./logs/logs.txt', 'a')
    f.writelines(f'{message.author} in {message.channel} auf {message.guild} am {Datum} um {Zeit}: {message.content} \n')
    f.close()

#send command
async def message_send(message, client, send):
    message = str(message.content).split(' ')
    ID = str(message[1]).replace('<', '').replace('>', '').replace('#', '').replace("'", "")
    mes = str(message[2:]).replace("]", "").replace("'", "").replace(",", "").replace("[", "")
    if ID.__contains__('@'):
        try:
            ID = ID.replace('@', '').replace('!', '')
            user = await client.fetch_user(ID)
            await user.send(mes)
        except:
            await send('Error: Nachricht konnte nicht gesendet werden1')

    else:
        try:
            channel = client.get_channel(int(ID))
            await channel.send(mes)
        except:
            await send('Error: Nachricht konnte nicht gesendet werden2')