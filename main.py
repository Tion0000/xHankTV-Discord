import discord
from discord.ext import commands

# Definiere die Intents, die der Bot benötigt
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

# Erstelle den Bot mit einem Präfix
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Wenn der Bot bereit ist
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Echo (wiederholt die Nachricht des Nutzers)
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Event: Wenn ein neuer Benutzer dem Server beitritt
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    if channel:
        await channel.send(f'Willkommen auf dem Server, {member.mention}!')

# Command: Hilfe (zeigt eine Liste aller Befehle)
@bot.command()
async def help(ctx):
    help_text = """
    **Befehle:**
    `!ping` - Überprüft, ob der Bot funktioniert.
    `!echo [Nachricht]` - Wiederholt die Nachricht des Nutzers.
    `!help` - Zeigt diese Nachricht an.
    """
    await ctx.send(help_text)

# Starte den Bot
bot.run('MTI3MTcxMDczMzg1MTE2NDcxNA.GVnbtk.jwUBb_1fuqv15QQJV_zrDsvMD7EMMxL0LqFfHY')