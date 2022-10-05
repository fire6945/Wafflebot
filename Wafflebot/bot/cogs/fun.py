import discord
from discord.ext import commands

from ..utility import embed_builder, values  # just in case
from .backend import reddit


class Fun(commands.Cog):

    def __init__(self, client):
        self.client: commands.Bot = client
        self.reddit = reddit.Reddit()

    @commands.command(aliases=["rmeme"])
    def redditmeme(self, ctx):
        data = self.reddit.random_meme()
        embed = discord.Embed(
            title="Reddit memes",
            url=data["meme_url"],
            description=data["title"],
            color=discord.Color.purple()
        )
        embed.set_image(url=data["image_url"])
        embed.set_footer(
            text=
            f"👍: {data['upvotes']} 👎: {data['downvotes']} 💬: {data['comment_count']}"
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
