import discord
from commands import dice, docs, github, hash, help, hicommand, idea 
from commands import logs, sendcommand, status, stop, verify, blacklist
    
    
    
async def commands(message, client, prefix, owner):


    await blacklist.check_blacklist(message, owner)

    send = message.channel.send
    command = message.content.lower().startswith

    logs.logs(message)




    if message.author == client.user:
        return

    else:

        #helpcommand
        if command(f'{prefix}help'):
            await help.help_command(message, prefix)

        #hi command
        elif command(f'{prefix}hi'):
            await hicommand.test(message)

        #idea command
        elif command(f'{prefix}idee'):
            await idea.idea_command(message, prefix)

        #dice
        elif command(f'{prefix}dice'):
            await dice.the_dice(message, prefix)

        #hash encoder
        elif command(f'{prefix}hash: ') or message.content.startswith(f'{prefix}hash '):
            await hash.hasconverter(message, prefix)

        #stop command
        elif command(f'{prefix}stop'):
            await stop.stop_command(message)

        #github command
        elif command(f'{prefix}github'):
            await github.GitHub_command(message, prefix)

        #status
        elif command(f'{prefix}status'):
            await status.set_state(message, client, send)

        #die docs
        elif command(f'{prefix}docs '):
            await docs.docs(message)

        #send command
        elif command(f'{prefix}send'):
            await sendcommand.message_send(message, client, send)

        #verify
        elif command(f'{prefix}verify'):
            await verify.verify(message)

        elif command(f'{prefix}adbl'):
            await blacklist.adbl(message, prefix, owner)

        elif command(f'{prefix}blacklist'):
            await blacklist.sendblacklist(message)

        elif command(f'clear'):
            await blacklist.clear_command(message)