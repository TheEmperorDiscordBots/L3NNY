import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Info:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def serverstats(self, ctx):
        """Just server stats"""
        guild = ctx.guild
        roles = [x.name for x in guild.roles]
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p"))         
        em = discord.Embed(description= "The Statistics for this server", title='Server Stats', colour=0xffffff)
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name='__Server __', value=str(guild.name))
        em.add_field(name='__Owner__', value=str(guild.owner))
        em.add_field(name='__Owner ID__', value=guild.owner_id) 
        em.add_field(name='__Members__', value=str(guild.member_count))
        em.add_field(name='__Total Channels__', value=str(channels))
        em.add_field(name='__Region__', value='%s' % str(guild.region))
        em.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        em.set_footer(text='Created - %s' % time)        
        await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(Info(bot)) 
