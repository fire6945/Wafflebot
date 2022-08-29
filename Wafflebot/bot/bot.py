import discord
from discord.ext import commands

from .cogs import events

class Wafflebot:
    """
    TODO: Test stuff

    This class handles Wafflebot's operations at the highest level.
    """
    def __init__(self, token):
        self.token = token
        self.client = commands.Bot(command_prefix="ww.", case_insensitive=True, intents=discord.Intents.all())
        self.cogs = [events]

    def run(self):
        for cog in self.cogs:
            cog.setup(self.client)

        self.client.run(self.token)
