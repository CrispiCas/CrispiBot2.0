async def test(message):
    userIdgesplitet = str(message.author).split("#", 1)[0]
    await message.channel.send(f'hi {userIdgesplitet}')