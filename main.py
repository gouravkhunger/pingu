# required stuff
import discord
import requests
import json
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://zenquotes.io/api/random"

# The following function selects a language in discord to display the quotes, in discord, different languages have
# different colours, like cpp would give green colour, java would give red, etc.
def get_formatted_string(str1, str2):

    # Here, the format is, colors[0] == the name of lang, colours[1] == prefix, colours[2] == suffix.
    colors = [
        ["diff", '-', ''],
        ["css", '{', '}'],
        ["fix", '', "--"],
        ["apache", "%{", '}'],
        ["diff", '+', ''],
        ["css", '"', '"'],
        ["bash", '"', '"'],
        ["json", '"', '"'],
        ["ini", '[', ']']
    ]

    rand = random.choice(colors)
    final_str = "```" + rand[0] + "\n" + rand[1] + str1 + "\n\n~" + str2 + rand[2] + "\n```"

    return final_str


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
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
                await channel.send(get_formatted_string(quote, q_author))

        # contest notifications from practice bot
        elif str(channel.id) == "804973113246220309" and str(message.author) == "Practice#2886":
            await channel.send("<@&807807887375990876> ^_^")

client = MyClient()
client.run(os.environ.get('BOT_TOKEN'))