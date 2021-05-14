# required stuff
import discord
import requests
import json

BASE_URL = "https://zenquotes.io/api/random"


class MyClient(discord.Client):
    async def on_ready(self):
        # print('Logged on as', self.user)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="opportunities to pong you"))

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        # store variables for better access
        msg = message.content.lower()
        channel = message.channel

        # prefix check
        if msg.startswith(';p'):

            # send code if someone wants it ✨
            if msg == ";p code":
                await channel.send("Here's the code that makes me live: "
                                   "<https://github.com/GouravKhunger/pingu/blob/main/current/main.py>")
                return

            # get a random quote from zen quote's api
            if msg == ";p quote":
                response = requests.get(BASE_URL)
                json = response.json()
                quote = json[0]['q']
                q_author = json[0]['a']
                await channel.send(
                    quote
                    + "\n" +
                    "- " + q_author
                )

        # contest notifications from practice bot
        elif str(channel.id) == "804973113246220309" and str(message.author) == "Practice#2886":
            await channel.send("<@&807807887375990876> ^_^")


client = MyClient()
client.run('<bot-token>')
