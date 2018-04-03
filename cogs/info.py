
import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Info:
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['info', 'botinfo'])
    async def info(self, ctx):
        """My infomation. hehehe..."""       
        color = discord.Color(value=0xffffff)
        em = discord.Embed(color=color, title='Info')
        em.description = "My sweet, sweet info!"
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/414456650519412747/ede4bd62db1db6719bbbda4aa78a9344.webp?size=1024")        
        em.add_field(name='Owner', value='TheEmperor™#2644')
        em.add_field(name='Developer(s)', value='dat eric kang boi#0847')
        em.add_field(name='Number of Servers', value=f'{len(self.bot.guilds)} servers') 
        em.add_field(name='Version', value='0.1.0')
        em.add_field(name='Start Date', value='2/13/2018')
        em.add_field(name='Region', value='North America')
        em.add_field(name='Code Platform', value='GitHub')
        em.add_field(name='Hosting Platform', value='Heroku')
        em.add_field(name='Coding Language', value='Python, discord.py')      
        await ctx.send(embed=em)



        
        

def setup(bot): 
    bot.add_cog(Info(bot)) 
