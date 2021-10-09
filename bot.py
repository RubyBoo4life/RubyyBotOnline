import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

    @client.command()
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @client.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

client.run('ODk2MzU2OTkzNTQ2MjE5NTIw.YWF7gA.dl2eX4Rkn2NO_acSP0tmi_thwL4')
