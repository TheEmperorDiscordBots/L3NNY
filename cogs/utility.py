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
import urllib.parse
from pygoogling.googling import GoogleSearch
from .utils.paginator import Pages
from discord.ext import commands


class Utility:
    def __init__(self, bot):
       self.bot = bot


    @commands.command()
    async def ascii(self, ctx, *, text):
        """Send fancy ASCII text!"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}") as resp:
                message = await resp.text()
                if len(f"```{message}```") > 2000:
                    return await ctx.send('Your ASCII is too long!')
                await ctx.send(f"```{message}```")
                
                
def setup(bot): 
    bot.add_cog(Utility(bot))                            
