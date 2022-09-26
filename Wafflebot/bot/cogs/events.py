import discord
from discord.ext import commands

from ..utility import embed_builder, values

import asyncio

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

        # This section of code does bad word detection
        async def check_for_badwords():
            content = message.content.split(" ")
            badwords = self.values.get_badwords()
            if any([True for word in content if word.lower() in ["retard", "retarded", "nigger", "nigga"]]):
                embed = self.embeds.moderation([2, message.author])
                channel = self.client.get_channel(self.values.get_channel("moderation_log"))
                await channel.send(embed=embed)
            elif any([True for word in content if word.lower() in badwords]):
                return True

        b = await check_for_badwords()
        if b:
            r = discord.Embed(title="Some people may not be comfortable with the use of profanity, so please be careful with your word choice. Thank you!", color=discord.Color.orange())
            await message.reply(embed=r)
            channel: discord.TextChannel = message.channel
            last: discord.Message = await channel.get_partial_message(message.channel.last_message_id).fetch()
            one = last.delete(delay=3)
            two = message.delete(delay=3)
            await asyncio.gather(one, two)

        # This section of code handles reports of bad behavior
        if (message.content == "report") and (type(message.channel) == discord.DMChannel):
            await message.channel.send("What would you like to report? Once you send your message, the administrators will automatically be notified. Please be as informative as possible with your answer.")
            msg = await self.client.wait_for('message')
            embed = self.embeds.moderation([0, msg])
            channel = self.client.get_channel(self.values.get_channel("moderation_log"))
            await channel.send(embed=embed)
        try:
            print(f"({message.guild.name}, {message.channel.name}) {message.author}: {message.content}")
        except:
            print(f"(DM with Wafflebot) {message.author}: {message.content}")

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

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        pass

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        pass

def setup(client):
    client.add_cog(Events(client))
