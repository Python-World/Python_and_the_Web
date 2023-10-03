import os
import random
from itertools import cycle

import discord
from discord.ext import commands, tasks

TOKEN = "token"
client = commands.Bot(command_prefix="/")
status = cycle(["Eight arms", "Meow meow"])
players = {}

cursewords = {
    "cursewords": [
        "fuck",
        "fuck off",
        "shit",
        "pissoff",
        "dickhead",
        "asshole",
        "son of a bitch",
        "bitch",
        "shut the fuck up",
    ]
}


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.dnd, activity=discord.Game("Meow meow")
    )
    print("Bot is online")


@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")


@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")


@client.command()
async def hey_cat(ctx):
    await ctx.send("Meow I'm gonna smother you with my tentacles")


@client.command()
async def mc(ctx):
    await ctx.send("Life is always hard and on survival until it's not")


@client.command(aliases=["8arm", "check"])
async def _8arm(ctx, *, question):
    responses = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
    ]
    await ctx.send(f"Question:{question}\nAnswer: {random.choice(responses)}")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unfound tentacles")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


async def clear_error(ctx, error):
    await ctx.send(
        "Please specify the amount of messages to clear with tentacles"
    )


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def octoplay(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl(url)
    players[server.id] = player
    player.start()


@client.command()
async def marco(ctx):
    await ctx.send("polo")


@client.command()
async def logout(ctx):
    await ctx.send("Going Offline")
    await client.logout()


@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency *1000)}ms ")


@client.event
async def on_message(message):
    if message.content in cursewords:
        await message.channel.purge(limit=1)
        await message.author.create_dm()
        await message.author.dm_channel.send(
            f"{message.author.name} that's a strike buddy"
        )


client.run(TOKEN)
