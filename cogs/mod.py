import discord
import sys
import os
import io
import asyncio
import json
import ezjson
from discord.ext import commands


class mod:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, num: int):
        """Deletes messages. _purge [number]""" 
        try: 
            if num is None:
                await ctx.send("_purge [number]")
            else:
                try:
                    float(num)
                except ValueError:
                    return await ctx.send("The number is invalid. Make sure its a number! _purge [number]")
                await ctx.channel.purge(limit=num+1)
                msg = await ctx.send("Done. ( ͡° ͜ʖ ͡°) ", delete_after=4)
        except discord.Forbidden:
            await ctx.send("I don't have **Manage Messages** permission.")
        except commands.errors.MissingPermissions:
            await ctx.send("Cant delete messages without perms.")

            
def setup(bot): 
    bot.add_cog(mod(bot))              
