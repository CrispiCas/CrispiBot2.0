import discord
from commands import adcmd, blacklist, docs, functions, hash, help, idea, status, stop, verify
    
    
    
async def commands(message, client, prefix, owner):


    await blacklist.check_blacklist(message, owner, client)

    send = message.channel.send
    command = message.content.lower().startswith

    functions.logs(message)




    if message.author == client.user:
        return

    else:
        if message.content.lower().startswith(prefix):
            await adcmd.commands(message, prefix)

        if command(f'>adcmd'):
            await adcmd.ad_cmd(message, owner)

        #helpcommand
        elif command(f'{prefix}help'):
            await help.help_command(message, prefix)

        #hi command
        elif command(f'{prefix}hi'):
            await functions.test(message)

        #idea command
        elif command(f'{prefix}idee'):
            await idea.idea_command(message, prefix)

        #dice
        elif command(f'{prefix}dice'):
            await functions.the_dice(message, prefix)

        #hash encoder
        elif command(f'{prefix}hash: ') or message.content.startswith(f'{prefix}hash '):
            await hash.hasconverter(message, prefix)

        #stop command
        elif command(f'{prefix}stop'):
            await stop.stop_command(message)

        #github command
        elif command(f'{prefix}github'):
            await functions.GitHub_command(message, prefix)

        #status
        elif command(f'{prefix}status'):
            await status.set_state(message, client, send)

        #die docs
        elif command(f'{prefix}docs '):
            await docs.docs(message)

        #send command
        elif command(f'{prefix}send'):
            await functions.message_send(message, client, send)

        #verify
        elif command(f'{prefix}verify'):
            await verify.verify(message)
        
        #add blacklist command
        elif command(f'{prefix}adbl'):
            await blacklist.adbl(message, prefix, owner)

        #reset bl number
        elif command(f'{prefix}resetblnr '):
            await blacklist.reset_blacklistnr(message, prefix, owner)

        #getblnr
        elif command(f'{prefix}getblnr'):
            await blacklist.blavklistnr_abfrage(message, prefix, owner)