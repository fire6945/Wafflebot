import discord
from discord.ext import commands

from ..utility import embed_builder, values

class Events(commands.Cog):
    """
    TODO: Finish coding all the events that the bot currently needs to support

    This cog will handle the required events that the bot listens for:
    >> on_ready
    >> on_message
    >> on_member_join
    >> on_member_remove
    >> on_member_ban
    >> on_member_unban

    This cog will also log information regarding the above events to the appropriate channels.
    """

    def __init__(self, client):
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user} is alive")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.User):
        pass

def setup(client):
    client.add_cog(Events(client))
