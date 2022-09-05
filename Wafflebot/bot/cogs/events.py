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
        self.embeds = embed_builder.EmbedBuilder()
        self.values = values.Values()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user} is alive")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        async def check_for_badwords():
            content = message.content.split(" ")
            badwords = self.values.get_badwords()
            if any([True for word in content if word.lower() in badwords]):
                return True
            else:
                return False

        b = await check_for_badwords()
        if b:
            await message.reply("Some people may not be comfortable with the use of profanity, so please be careful with your words. Thank you!")
        else:
            print("Error with function check_for_badwords")
        print(f"({message.guild.name}, {message.channel.name}) {message.author}: {message.content}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = self.embeds.member_join(member)
        channel = self.client.get_channel(self.values.get_channel("welcome_and_goodbye"))
        await channel.send(content=f"{member.mention}", embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        embed = self.embeds.member_remove(member)
        channel = self.client.get_channel(self.values.get_channel("welcome_and_goodbye"))
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Events(client))
