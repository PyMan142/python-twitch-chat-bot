from twitchio.ext import commands
from twitchio.client import Client
from keys import *

# The main controller you'll be using for most things
bot = commands.Bot(
    token = irctoken,
    client_id = clientid,
    nick = '', # This is the username of the bot account
    prefix = '!', # What the bot looks for to start a command
    initial_channels=[''] # Your streaming channel name - You can add this in ANYONES channel --  BE CAREFUL
)

#If you need to access the client for getting things like a full list of users in the chat
client = Client(
    token = irctoken,
    client_secret = clientsecret
)

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("This is a test response")

if __name__ == '__main__':
    bot.run()