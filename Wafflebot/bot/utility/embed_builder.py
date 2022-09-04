import discord

class EmbedBuilder:
    """
    TODO: Code all the methods that build the embeds

    This class will build various embeds for different scenarios
    >> New member join
    >> Member leave
    >> Member ban
    >> Member unban
    >> User info
    >> Bot info
    >> Waffleweb info
    """

    def __init__(self):
        pass

    def member_join(self, member):
        embed = discord.Embed(
            title="Member joined",
            description=f"Welcome! We're so glad to have you here!",
            color=discord.Color.green()
        )
        return embed

    def member_remove(self, member):
        embed = discord.Embed(
            title="Member left",
            description=f"{member.mention} has left the server.",
            color=discord.Color.red()
        )
        return embed
