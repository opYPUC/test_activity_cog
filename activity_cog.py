import discord
from discord.ext import commands


class ActivityCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing, name="Roblox + " "Minecraft + DND"
            )
        )

    @commands.command()
    async def change_status(self, ctx: commands.Context, status: str):
        await self.bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status)
        )
        await ctx.send(f"Статус изменен на: `{status}`")
