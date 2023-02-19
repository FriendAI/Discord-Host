import discord
from keep_alive import keep_alive
from discord.ext import keep_alive
import os
import openai

bot = commands.bot(
    command_prefix='?',
    case_insensitive=False,
    destriction=None,
    intents=discord.intents.all(),
    help_command=None
)

@bot.command()
async def test(ctx,*,arg):
    query = ctx.message.content
    response = openai.Completion.create(
        api_key = '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',
        model="text-davinci-003",
        prompt=query,
        tempature=0.5
        max_tokens=60
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    await ctx.channel.send(content=response['choices'][0]['text'].replace(str(query), ""))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.activity(type=discord.activityType.listening, name=f"hi"))
    print(f"logged in as {bot.user.name}")

keep_alive()

bot.run(os.environ['BOT KEY']) #enter your discord bot token here!

from flask import Flask
from threading import Thread
 
app = Flask('')
 
@app.route('/')
def home():
    return "Hello. I am alive!"
 
def run():
  app.run(host='0.0.0.0',port=8080)
 
def keep_alive():
    t = Thread(target=run)
    t.start()
