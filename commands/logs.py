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