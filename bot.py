import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'),description="TheEmperor™'s Discord bot.\n\nHelp Commands",owner_id=250674147980607488)
bot._last_result = None

startup_extensions = [

    'cogs.fun',
    'cogs.mod',
    'cogs.math'                        	
	
]


def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers boi!"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="_help"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="V 0.1.1"))
        await asyncio.sleep(10)

	
@bot.event
async def on_guild_join(guild):
    logChannel = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xffffff))
    em.title = "L3NNY has arrived in a new server!"
    em.description = f"Server: {guild}"
    await logChannel.send(embed=em)
    
	
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
	
	
@bot.event
async def on_guild_remove(guild):
    logChannel = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "L3NNY has left a server."
    em.description = f"Server: {guild}"
    await logChannel.send(embed=em)


@bot.command()
async def support(ctx):
    """Join the support server!"""
    color = discord.Color(value=0xffffff)
    em = discord.Embed(color=color, title='Help out in the development!')
    em.description = f"Link: https://discord.gg/zzzJAKM"
    await ctx.send(embed=em)

@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0xffffff)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)


@bot.command()
async def invite(ctx):
    """lets me join ur club"""
    await ctx.send ("Lemme join dat club: https://discordapp.com/api/oauth2/authorize?client_id=414456650519412747&permissions=8&scope=bot")

    
@bot.command()
async def say(ctx, *, message:str):
    """Speak as me!"""
    await ctx.message.delete()
    await ctx.send(message)    


@bot.command()
async def upvote(ctx):
    """Upvote me!"""
    await ctx.send ("Upvote me here! https://discordbots.org/bot/414456650519412747") 

@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, user: discord.Member = None):
    '''Mutes a user'''
    if user is None:
    	return await ctx.send("Please tag that annoying user to mute them!")
    try:
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"{user.mention} has been muted. FINALLY!")
    except discord.Forbidden:
        return await ctx.send(":x: I don't have **Manage Channel** permmition.")  

		
@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, user: discord.Member = None):
	'''Un-mutes a user'''
	if user is None:
		return await ctx.send("Please tag a uesr to unmute them!")
	try:
		await ctx.channel.set_permissions(user, send_messages=True)
		await ctx.send(f"{user.mention} is now unmuted. Hope they learned their lesson.")
	except discord.Forbidden:
		await ctx.send(":x: Couldn't unmute the user. I need the **Manage Channels** permission.")
  	

@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body):
    """Evaluates python code"""
    if ctx.author.id != 250674147980607488 and ctx.author.id != 277981712989028353:
        return await ctx.send("You cannot use this command becuase you are not a developer.")
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': bot._last_result,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text) - 1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:

                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')
	
	
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
