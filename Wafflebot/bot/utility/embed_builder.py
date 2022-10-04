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

    def good(self, message):
        embed = discord.Embed(
            description=message,
            color=discord.Color.green()
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
            kb = d[1]
            reason = d[2]
            member = d[3]
            embed = discord.Embed(
                title=f"Member banned: {member.mention}",
                description=f"Reason: {reason}",
                color=discord.Color.red()
            )
            if kb == "k":
                embed.title = f"Member kicked: {member.mention}"
            elif kb == "ub":
                embed.title = f"Member unbanned: {member.mention}. Welcome back!"
                embed.color = discord.Color.gold()
            return embed
        elif d[0] == 2:
            member = d[1]
            embed = discord.Embed(
                title="Slur report",
                description=f"{member.mention} said a slur.",
                color=discord.Color.orange()
            )
            return embed

