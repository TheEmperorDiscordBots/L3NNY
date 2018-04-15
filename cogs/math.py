import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Math:
    def __init__(self, bot):
       self.bot = bot
                
    
                                              
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
        '''Add numbers'''
        if num is None:
            await ctx.send("_add [number] [number]")
        else:
            await ctx.send(```num + num2```)
                
                
    @commands.command()
    async def subtract(self, ctx, num: int, num2: int):
        '''Subtract numbers'''
        if num is None:
            await ctx.send("_subtract [number] [number]")
        else:
            await ctx.send(```num - num2```)
                
                
    @commands.command()
    async def multiply(self, ctx, num: int, num2: int):
        '''Multiply numbers'''
        if num is None:
            await ctx.send("_multiply [number] [number]")
        else:
            await ctx.send(```num * num2```)
                
                
    @commands.command()
    async def divide(self, ctx, num: int, num2: int):
        '''Divide numbers'''
        if num is None:
            await ctx.send("_divide [number] [number]")
        else:
            await ctx.send(```num / num2```)
            
            
def setup(bot): 
    bot.add_cog(Math(bot))  
