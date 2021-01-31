# pingu
## Discord Ping Bot
This is a simple discord bot written in java as well as python(both do the same thing, but one is made using gradle and other uses python), which is made to ping everyone when another bot/person messages in a particular channel

Java:

```java
if (event.getChannel().getId().equals("<channel-id-for-pinging>") && author.getId().equals("<person-or-bots-ID>")) {
    event.getChannel().sendMessage(("@everyone ^_^")).queue();
}
```

Python:

```python
if str(message.channel.id) == "<channel-id>" and str(message.author) == "<user-tag>":
    await message.channel.send("@everyone ^_^")
```

Whenever the sender's ID equals the a particular id(which is to be entered in `<person's/bot's ID>`) and the channel in which that message is sent matched with `<channel ID for pinging>`, this bot will ping `@everyone`.

This project uses JDA(Java Discord API) for the Java version and discord.py for the python version. Links are given below. 
JDA: https://github.com/DV8FromTheWorld/JDA.
discord.py: https://github.com/Rapptz/discord.py

The Java code a gradle app, and the code was written in IntelliJ IDEA community edition :)

To get started with making you own basic discord bots with JAVA, you may look into this very well explained article https://medium.com/discord-bots/making-a-basic-discord-bot-with-java-834949008c2b.
