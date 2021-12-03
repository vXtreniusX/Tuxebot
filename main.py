# bot.py
from os import listdir, environ

import discord
import json

TOKEN = environ['token']
mon_files = listdir('/app/mods/tuxemon/db/monster')
tech_files = listdir('/app/mods/tuxemon/db/technique')
images = '/app/mods/tuxemon/gfx/sprites/battle/'
client = discord.Client()


@client.event
async def on_message(message):
    # for now we only check for monsters,
    # but in future we can add techniques, npcs, etc.
    if message.content.startswith("/monster"):
        m = message.content
        if '.json' in m:
            m = m.replace('.json', '')
        for i in range(len(mon_files)):
            f = str(mon_files[i])
            if '.json in f':
                f = f.replace('.json', '')
            if f in m:
                curfile = open(mon_files[i])
                data = json.load(curfile)
                slug = data['slug']
                category = data['category']
                move_set = data['moveset']
                weight = data['weight']
                catch_rate = data['catch_rate']
                types = data['types']
                text = str(slug + ', the ' + category + ' Tuxemon\n')\
                    + str("Types:" + str(types))\
                    + str("Weight: " + str(weight))\
                    + str("Catch Rate: " + str(catch_rate) + '%')\
                    + str('Learnable Moves: ')
                for j in range(len(move_set)):
                    text.join(str(move_set[j]))

                imagefront = discord.File(images + slug + '-front.png')
                imageback = discord.File(images + slug + '-back.png')

                await message.channel.send(content=text, files=[imagefront, imageback])


client.run(TOKEN)
