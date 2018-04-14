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
        await asyncio.sleep(2)
        await msg.edit(content="im a MEME")
        await asyncio.sleep(2)
        await msg.edit(content="IM A MEME BOYZZZZ LMAOOOO XDDD")
        await asyncio.sleep(4)
        await msg.edit(content=f"lmao xd")   
            
    
    @commands.command(aliases=['g'])
    async def google(self, ctx, *, query):
        """Searches google and gives you top result."""
        await ctx.trigger_typing()
        try:
            card, entries = await self.get_google_entries(query)
        except RuntimeError as e:
            await ctx.send(str(e))
        else:
            if card:
                value = '\n'.join(f'[{title}]({url.replace(")", "%29")})' for url,
                                  title in entries[:3])
                if value:
                    card.add_field(name='Search Results', value=value, inline=False)
                return await ctx.send(embed=card)

            if len(entries) == 0:
                return await ctx.send('No results found... sorry.')

            next_two = [x[0] for x in entries[1:3]]
            first_entry = entries[0][0]
            if first_entry[-1] == ')':
                first_entry = first_entry[:-1] + '%29'

            if next_two:
                formatted = '\n'.join(f'<{x}>' for x in next_two)
                msg = f'{first_entry}\n\n**See also:**\n{formatted}'
            else:
                msg = first_entry

            await ctx.send(msg)
    
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def msg(self, ctx, user: discord.Member, *, msg: str):
        """Message someone as me!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("The message has been sent! hehehe....")
        except commands.MissingPermissions:
            await ctx.send("rip. you dont have enough perms. xd")
        except:
            await ctx.send(":x: Format: _msg (user tag) (messgae)")
    
    
    @commands.command()
    async def expose(self, ctx, user: discord.Member = None):
        '''Expose someone!'''
        if user is None:
            return await ctx.send(":no_entry_sign: **You need to mention a user.**")
        try:
            roasts = ["likes https://pornhub.com/, I found it in their history", "is super gay.", "likes your mom.", "copies code from my creator.", "is Adolf Hitler's son.", "is 97% gay :gay_pride_flag:", "is triple gay."]
            await ctx.send(f"{user.mention} {random.choice(roasts)}")
        except commands.errors.BadArgument:
            return await ctx.send(f":no_entry_sign: **{user}**, is not a valid username or mention")
    
    
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

        
    @commands.command()
    async def ascii(self, ctx, *, text):
        """Usage: _ascii [text]"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}") as resp:
                message = await resp.text()
                if len('​`​`​`' + message + '​`​`​`') > 2000:
                    return await ctx.send('Your ASCII is too long!')
                await ctx.send('​`​`​`' + message + '​`​`​`')
        
        
    @commands.command(aliases=['yt', 'vid', 'video'])
    async def yt(self, ctx, *, search):
        """Search for videos on YouTube"""
        search = search.replace(' ', '+').lower()
        response = requests.get(f"https://www.youtube.com/results?search_query={search}").text
        result = BeautifulSoup(response, "lxml")
        dir_address = f"{result.find_all(attrs={'class': 'yt-uix-tile-link'})[0].get('href')}"
        output=f"**Top Result:**\nhttps://www.youtube.com{dir_address}"
        try:
            await ctx.send(output)
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        
           
def setup(bot):
    bot.add_cog(fun(bot))
