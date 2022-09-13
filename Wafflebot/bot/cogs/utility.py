import discord
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['u', 'uinfo', 'user'])
    async def userinfo(self, member: discord.Member):
        pass