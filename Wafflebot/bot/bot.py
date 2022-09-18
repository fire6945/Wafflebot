import discord
from discord.ext import commands

from .cogs import events, utility
from .utility import values

class Wafflebot:
    """
    TODO: Test stuff

    This class handles Wafflebot's operations at the highest level.
    """
    def __init__(self, token):
        self.token = token
        self.client = commands.Bot(command_prefix=values.Values.get_prefix(), case_insensitive=True, intents=discord.Intents.all())
        self.cogs = [events, utility]

    def run(self):
        for cog in self.cogs:
            cog.setup(self.client)

        self.client.run(self.token)
