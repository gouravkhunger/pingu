# pingu
## Discord Ping Bot
This is a simple discord bot written in java, which is made to ping everyone when another bot/person messages in a particular channel

```java
if (event.getChannel().getId().equals("<channel ID for pinging>") && author.getId().equals("<person's/bot's ID>")) {
    event.getChannel().sendMessage(("@everyone")).queue();
}
```

Whenever the sender's ID equals the a particular id(which is to be entered in `<person's/bot's ID>`) and the channel in which that message is sent matched with `<channel ID for pinging>`, this bot will ping `@everyone`.

This project uses JDA(Java Discord API), which can be found here: https://github.com/DV8FromTheWorld/JDA.

This is a grade app, and the code was written in IntelliJ IDEA community edition :)

To get started with making you own basic discord bots with JAVA, you may look into this very well explained article https://medium.com/discord-bots/making-a-basic-discord-bot-with-java-834949008c2b.
