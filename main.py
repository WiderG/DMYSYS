"""
DMYSYS Discord Bot License (Version 1.4.2)

Basically, DMYSYS belongs to me and the people who help make it, and you can't pass it off as your own.

"""

# DMYSYS IS DESIGNED TO RUN ON PYTHON 3.8
# requires discord.py 2.3.2 and discord-py-slash-command 3.0.0 (SPECIFICALLY!!)

try:
    with open("config.txt", "r") as f:
        lines = f.readlines()
        DMYSYSKEY = lines[1].strip()
        DEBUGMODE = lines[5].strip()
        LOGDISABLED = lines[8].strip()
except:
    open("config.txt", "x")
    print("CONFIG file created. Put your key on the 1st line, a bool for if you want debugmode or not on line 5, "
          "and the same on line 8 to toggle logging")
    exit(1)
    
try:
    import socket
    import time
    import discord
    from discord_slash import SlashCommand
    from discord.utils import get
    import logging
    from datetime import datetime
except:
    print("There was an error importing packages.")
    exit(1)

HOSTNAME = socket.gethostname()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_time_forlogfile = now.strftime("%H_%M_%S")
print("BOOT TIME:", current_time)

OWNERID = "1118926122650959936"
VERSION = "1.4.2 Codename Makinami"
INTENT = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
DMYSYS = discord.Client(intents=INTENT)
MAINGUILD = '1211383990720921683'
SLASH = SlashCommand(DMYSYS, sync_commands=True)

print("Passed main variable registration!")

if LOGDISABLED:
    print("DMYSYS Logging is disabled. Here be dragons.")
else:
    logging.basicConfig(filename=f"DMYSYSLOG_{current_time_forlogfile}.log", level=logging.INFO)

print("Passed log controls!")

# Startup Message ---------------------------------------------------------------

print("Loaded! Now running on_ready()...")


@DMYSYS.event
async def on_ready():
    try:
        status_channel_id = 1220063391725387897
        status_channel = DMYSYS.get_channel(status_channel_id)
        if status_channel and not DEBUGMODE:
            print("Setting activity...")
            activity = discord.Game(name="Running.", type=3)
            await DMYSYS.change_presence(status=discord.Status.idle, activity=activity)
            print("Success! Sending successful boot embed...")
            embed = discord.Embed(title=" Startup Success! ", url="", description="Hello World! DMYSYS is online. ",
                                  color=0xFF5733)
            embed.set_footer(text=f"Version: {VERSION}")
            ping = ((round(DMYSYS.latency, 1)))
            finalping = f"Ping is {ping}ms"
            embed.add_field(name="Ping", value=finalping)
            embed.add_field(name="Host", value=HOSTNAME)
            embed.add_field(name="Time", value=current_time)
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/1218966857243955230/1220901123737653259/image.png?ex=66109fc7&is=65fe2ac7&hm=68b294c9935347cadf5e70a96e7fdaf70d42ed0aadfdfcfcd72bc2431770f350&")
            await status_channel.send(embed=embed)
            print("DMYSYS Initialized. Running on version", VERSION, "as", DMYSYS.user)

        else:
            print("DMYSYS is in Debug / Development mode. No startup message was printed.")
            logging.info("DEBUG IS TRUE.")
            activity = discord.Game(name="DEBUG MODE", type=1)
            await DMYSYS.change_presence(status=discord.Status.idle, activity=activity)
    except:
        print("Critical error in on_ready function.")
        exit(1)

# Commands ----------------------------------------------------------------------

@SLASH.slash(name='Shutdown',
             description="Shuts down DMYSYS. (GENDO+)")
async def shutdown(ctx):
    role = get(ctx.author.roles, name="Gendo Ikari")
    if role:
        status_channel_id = 1220063391725387897
        status_channel = DMYSYS.get_channel(status_channel_id)
        embed = discord.Embed(title=" Shutting Down. ", url="", description="Goodbye World. DMYSYS is shutting down.. ",
                              color=0xFF5733)
        embed.set_footer(text=f"Version: {VERSION}")
        embed.add_field(name="Host", value=HOSTNAME)
        embed.add_field(name="Time", value=current_time)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/1218966857243955230/1220901123737653259/image.png?ex=66109fc7&is=65fe2ac7&hm=68b294c9935347cadf5e70a96e7fdaf70d42ed0aadfdfcfcd72bc2431770f350&")
        await status_channel.send(embed=embed)
        print("Shutdown triggered by", ctx.author.name)
        print('[WARNING!] SHUTDOWN ACTIVATED BY USER', ctx.author.name, '[WARNING!]')
        logging.info("Shutdown has been activated by:", ctx.author.name)
        time.sleep(1)
        activity = discord.Game(name="Offline.", type=0)
        await DMYSYS.change_presence(status=discord.Status.do_not_disturb, activity=activity)
        exit()
    else:
        embed = discord.Embed(title=" [DMYSYS WARNING] COMMAND DECLINED.", url="",
                              description="SHUTDOWN COMMAND DECLINED. THIS INTERACTION HAS BEEN LOGGED.",
                              color=0xFF5733)
        await ctx.send(embed=embed)
        print("[WARNING!] Shutdown attempt from", ctx.author.name, "[WARNING!]")
        logging.info("Shutdown has been attempted by:", ctx.author.name)


# Autoresponse Units

keywords_responses = {
    "prick": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "gyat": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "how about": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "saw": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "shoulda": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "gyaat": "https://tenor.com/view/sopranos-tony-soprano-funny-gif-5018786074331786569",
    "https://tenor.com/view/rizz-hoop-peter-griffin-green-fn-gif-16271132247808270949": "https://tenor.com/view/rizz-hoop-peter-griffin-green-fn-gif-16271132247808270949",
    "rejected": "https://tenor.com/view/neon-genesis-evangelion-refused-glass-reflection-man-gif-14300048 ",
    "refused": "https://tenor.com/view/neon-genesis-evangelion-refused-glass-reflection-man-gif-14300048 ",
    "what the flip": "https://tenor.com/view/okay-dude-what-the-flip-ok-dude-what-the-flip-i%27m-gonna-touch-you-imma-touch-you-gif-7792701331326780614",
}


@DMYSYS.event
async def on_message(message):
    if message.author == DMYSYS.user:
        return
    msg_content = message.content.lower()
    for keyword, response in keywords_responses.items():
        if keyword in msg_content:
            await message.reply(response)
            break


DMYSYS.run(DMYSYSKEY)
