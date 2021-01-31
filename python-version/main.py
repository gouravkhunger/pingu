import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="opportunities to pong you"))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if str(message.channel.id) == "<channel-id>" and str(message.author) == "<user-tag>":
            await message.channel.send("@everyone ^_^")

client = MyClient()
client.run('<token>')
