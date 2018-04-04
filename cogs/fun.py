import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import json
from discord.ext import commands


class fun:
    def __init__(self, bot):
        self.bot = bot
        
        
        
        
        
        
    @commands.command()
    async def meme(self, ctx, user: discord.Member):
        """a meme animation"""
        msg = await ctx.send(f"i")
        await asyncio.sleep(2)
        await msg.edit(content="im")
        await asyncio.sleep(2)
        await msg.edit(content="im a")
        await asyncio.sleep(2)
        await msg.edit(content="im a M")
        await asyncio.sleep(2)
        await msg.edit(content="im a ME")
        await asyncio.sleep(2)
        await msg.edit(content="im a MEM")
        await asyncio.sleep(3)
        await msg.edit(content="im a MEME")
        await asyncio.sleep(3)
        await msg.edit(content="IM A MEME BOYZZZZ LMAOOOO XDDD")
        await asyncio.sleep(4)
        await msg.edit(content=f"lmao xd")   
            
    
    
def setup(bot):
    bot.add_cog(fun(bot))
