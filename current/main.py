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

        # react weird to pings to the bot
        mention = f'<@!{client.user.id}>'
        if mention in message.content or client.user.mention in str(message.content.split()):
            await message.channel.send(message.author.mention+" solve some problems or do some work smh, don\'t ping me!")
            await message.channel.send('<:tourist_mad:803325979082752040>')
            return

        # Disjoint Set Union makes pingu angry 😑
        list = message.content.split()
        for i in range(len(list)):
            if(list[i].lower() == 'dsu'):
                await message.add_reaction("<:angeryboye:816339048524283934>");
                await message.channel.send("F DSU. Don't even take its name <:angeryboye:816339048524283934>")
                return

        # Union Find Disjoin Set makes pingu happy 😃
        for i in range(len(list)):
            if(list[i].lower() == 'ufds'):
                await message.add_reaction("<:ghosthug:819541321735733259>");
                return

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
            #await message.channel.send("<:orz:803321101831766036>")
            await message.add_reaction("<:orz:803321101831766036>")

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
client.run('<bot-token>')
