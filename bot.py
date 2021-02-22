import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hey buddy!')

@client.command()
async def ping(ctx):
    r = round(client.latency*1000)
    if r > 400:
        await ctx.send(f'With {r}ms now {ctx.author} can teleport into the next dimension!')
    elif r > 150:
        await ctx.send(f'{ctx.author} your ping is too high:{r}ms')
    elif r < 150:
        await ctx.send(f'{r}ms can put smile on your face!{ctx.author}')

@client.command()
async def hello(ctx):
    await ctx.send('Hi buddy!')

@client.command()
async def clear(ctx,d=2):
    await ctx.channel.purge(limit=d+1)



client.run('ODExNjU3NjMxMjU2OTM2NDcw.YC1ZEw.RHBYa9JkTXeiM-bgpAya-al6Ffc')
