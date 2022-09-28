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

    def moderation(self, d):
        if d[0] == 0:
            msg = d[1]
            embed = discord.Embed(
                title="Incident Report",
                description=msg.content,
                color=discord.Color.orange()
            )
            embed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
            return embed
        elif d[0] == 1:
            kb = d[1] # gets the value which says whether a member was kicked or banned
            reason = d[2]
            member = d[3]
        elif d[0] == 2:
            member = d[1]
            embed = discord.Embed(
                title="Slur report",
                description=f"{member.mention} said a slur.",
                color=discord.Color.orange()
            )
            return embed

