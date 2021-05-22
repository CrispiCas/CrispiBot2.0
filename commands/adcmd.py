import sqlite3
import toml

config = toml.load('./config/config.toml')
path = config['path']

con = sqlite3.connect(path)
cur = con.cursor()


async def ad_cmd(message, owner):
    
    if message.author.id == int(owner):
        cmd = message.content
        cmd = cmd.replace('>adcmd ', '')
        cmd = cmd.split('-')
        chmd = cmd[0]
        output = cmd[1]

        try:
            cur.execute("CREATE TABLE IF NOT EXISTS cmds (name text PRIMARY KEY, ausgabe text)")
        except:
            pass

        cur.execute(f"INSERT INTO cmds VALUES ('{chmd}', '{output}')")
        con.commit()

        await message.channel.send(f'Neuer command \n __Trigger__: {chmd} \n __output__: {output}')
    else:
        await message.channel.send('Du hast keine Rechte hehe')




async def commands(message, prefix):
    cmd = message.content.lower().replace(prefix, '')

    try:
        command = cur.execute(f"SELECT ausgabe FROM cmds WHERE name = '{cmd}'")
        command = cur.fetchall()
        command = str(command).removeprefix('[(').removesuffix(',)]')
        command = command.replace("'", '')
        command = command.replace('[]', '')
        await message.channel.send(command)

    except:
        pass