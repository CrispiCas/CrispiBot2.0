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