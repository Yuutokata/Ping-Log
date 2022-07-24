import asyncio
import os

import discord
from discord.ext import commands
from utils.logger import logger
from utils.config import Config


class NobleNotify(commands.Bot):
    def __init__(self):
        allowed_mentions = discord.AllowedMentions(everyone=False, users=True, roles=True)
        intents = discord.Intents.all()
        super().__init__(command_prefix=Config().prefix,
                         intents=intents,
                         allowed_mentions=allowed_mentions,
                         description=Config().description,
                         heartbeat_timeout=150.0,
                         chunk_guilds_at_startup=False,
                         case_insensitive=True)
        self.logger = logger
        self.config = Config()
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        await self.presence()
        if not self.synced:
            await self.tree.sync(guild=discord.Object(id=int(self.config.guild)))
            self.synced = True
        self.logger.debug("The Bot has started")

    async def presence(self):
        status = self.status()
        await self.change_presence(activity=discord.Game(name=self.config.activity, status=status))

    def status(self):
        if int(self.config.status) == 0:
            return discord.Status.online
        if int(self.config.status) == 1:
            return discord.Status.idle
        if int(self.config.status) == 2:
            return discord.Status.dnd
        if int(self.config.status) == 3:
            return discord.Status.invisible

    async def cogs(self):
        if not os.path.isdir("cogs"):
            return
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                except Exception as e:
                    logger.error(f"Cant Load {filename[:-3]} Reason: {e} ", extra={"emoji": ":stop_sign:"})

    def run(self):
        asyncio.run(self.cogs())
        self.logger.debug(f"Starting ...", extra={"emoji": ":bomb:"})
        try:
            super().run(self.config.token, reconnect=True)

        except Exception as e:
            self.logger.critical(f"The Bot can't start, Reason: {e}", extra={"emoji": ":warning:"})
