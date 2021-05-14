import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # stay safe from rick rolls 😜
        await client.change_presence(activity=discord.Streaming(name='geniosity stuff', url='https://www.youtube.com/watch?v=bIwVIx5pp88'))
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the contest bot to pong you"))

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        # say command:
        # send a message containing whatever text is provided as text
        if(message.content.startswith(';p')):

            # send code if someone wants it ✨
            if(message.content.lower() == ";p code"):
                await message.channel.send("Here's the code that makes me live: <https://github.com/GouravKhunger/pingu/blob/main/current/main.py>")
                return

            elif("say" in message.content.lower()):
                #split the content only if it has say command
                msg = message.content.split('say', 1)

                #pingu should not disturb everyone with ghost pings 😅
                if('@everyone' in msg[1] or '@here' in msg[1]):
                    await message.channel.send("Refrain from mass pinging <:angeryboye:816339048524283934>")
                    return

                if('<@' in msg[1] and '>' in msg[1]):
                    await message.channel.send("Refrain from pinging anyone <:angeryboye:816339048524283934>")
                    return

                #if the current message does not have any pings, delete the original message
                # and send it as a message from the bot
                await message.delete()
                await message.channel.send(msg[1])
                return

            # command to delete messages sent by pingu
            elif(message.content.lower() == ';p delete'):
                if(message.reference != None):
                    msg_d = await message.channel.fetch_message(message.reference.message_id)
                    if(msg_d.author.name == 'pingu'):
                        await msg_d.delete()
                        await message.delete()
                    else:
                        await message.channel.send("Can't delete messages which I did not send.")
                else:
                    await message.channel.send("Please reference one of my messages to be deleted...")

        # react weird to pings to the bot
        mention = f'<@!{client.user.id}>'
        if mention in message.content or client.user.mention in str(message.content.split()):
            await message.channel.send(message.author.mention+" solve some problems or do some work smh, don\'t ping me!")
            await message.channel.send('<:tourist_mad:803325979082752040>')

        # Disjoint Set Union makes pingu angry 😑
        list = message.content.split()
        for i in range(len(list)):
            if(list[i].lower() == 'dsu'):
                await message.add_reaction("<:angeryboye:816339048524283934>");
                await message.channel.send("F DSU. Don't even take its name <:angeryboye:816339048524283934>")

        # Union Find Disjoin Set makes pingu happy 😃
        for i in range(len(list)):
            if(list[i].lower() == 'ufds'):
                await message.add_reaction("<:ghosthug:819541321735733259>");

        # Don't try to call pingu a dumbass 😔
        if 'pingu' in message.content.lower() and ('dumb' in message.content.lower() or 'noob' in message.content.lower() or 'bad' in message.content.lower() or 'no gud' in message.content.lower()):
                await message.channel.send("<:nou:803324068967088168>")

        # Pingu likes complements
        elif 'pingu' in message.content.lower() and ('good' in message.content.lower() or 'god' in message.content.lower() or 'best' in message.content.lower() or 'op' in message.content.lower()):
                await message.channel.send("Who doesn't know that <:smug:834411396120576060>")

        # Don't take pingu's name behind it's back
        elif 'pingu' == message.content.lower():
                await message.channel.send("Why the hell did you take my name <:thonkeyes:803324068664573953>")

        # some random case work
        elif ('anti' not in message.content.lower() and 'dsu' not in message.content.lower()) and ('orz' in message.content.lower() or 'otz' in message.content.lower() or 'ofz' == message.content.lower() or 'OTL' in message.content):
            await message.add_reaction("<:nou:816338682835501056>")

        # reactions to messages with certain words
        elif 'geniosity' in message.content.lower() or 'geniosities' in message.content.lower():
            await message.add_reaction("<:geniosity:806548099903914044>")
            await message.add_reaction("<:orz:803321101831766036>")

        elif str(message.channel.id) == "804973113246220309" and str(message.author) == "Practice#2886":
            await message.channel.send("<@&807807887375990876> ^_^")

        # elif ('dsu' in message.content.lower()) and (('bad' in message.content.lower()) or ('worst' in message.content.lower()) or ('no gud' in message.content.lower()))  and ('not' not in message.content.lower()):
        #     await message.add_reaction("<:ac:816337894074875984>");

        # elif ('dsu' in message.content.lower()) and (('good' in message.content.lower()) or ('best' in message.content.lower()) or ('gud' in message.content.lower()))  and ('not' in message.content.lower()):
        #     await message.add_reaction("<:ac:816337894074875984>");

client = MyClient()
client.run('bot-token')
