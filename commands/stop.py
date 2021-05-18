import sys
import toml

config = toml.load('./config/config.toml')
owner = config['owner']
konsole = config['konsole']

async def stop_command(message):
    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    if userID == owner:
        await message.channel.send("I'm disconenected")
        sys.exit()


    
    else:
        await message.channel.send('Du hast keine rechte hehe')