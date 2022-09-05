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

        # This section of code does bad word detection
        async def check_for_badwords():
            content = message.content.split(" ")
            badwords = self.values.get_badwords()
            if any([True for word in content if word.lower() in ["retard", "retarded", "nigger"]]):
                pass # TODO: Write code to send a message to a moderation channel that reports a user using slurs
            elif any([True for word in content if word.lower() in badwords]):
                return True

        b = await check_for_badwords()
        if b:
            await message.reply("Some people may not be comfortable with the use of profanity, so please be careful with your words. Thank you!")

        # This section of code handles reports of bad behavior
        if (message.content == "report") and (type(message.channel) == discord.DMChannel):
            await message.channel.send("What would you like to report? Once you send your message, the administrators will automatically be notified. Please be as informative as possible with your answer.")
            # TODO: Write code that sends the user's report to a moderation channel
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
