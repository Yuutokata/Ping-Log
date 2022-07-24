import datetime
import discord
from discord.ext import commands
import discord.ui
from discord.ui import Button, View
from utils.config import Config

config = Config()


class Checker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if len(ctx.role_mentions) > 0:
            for role in ctx.role_mentions:
                embed = discord.Embed(
                    title="Ping!",
                    color=int(config.color, 16),
                    description=f">>> **Von: {ctx.author.mention}\n Channel: {ctx.channel.mention} \n Role: {role.mention}**")
                embed.set_thumbnail(url=ctx.author.avatar)
                embed.set_footer(text="NobleNotify", icon_url=config.icon)
                embed.timestamp = datetime.datetime.now()
                button = Button(label="Ping!", style=discord.ButtonStyle.url, url=f"{ctx.jump_url}")
                view = View(timeout=None)
                view.add_item(button)
                channel = self.client.get_channel(int(config.log))
                await channel.send(embed=embed, view=view)


async def setup(client):
    await client.add_cog(Checker(client))
