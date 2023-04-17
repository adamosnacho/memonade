import discord
import asyncio

# Replace "YOUR_BOT_TOKEN" with your bot token
client = discord.Client(intents=discord.Intents.default())

# Define a coroutine to send the message every 20 seconds
async def send_message():
    channel = client.get_channel("general") # Replace YOUR_CHANNEL_ID with the ID of the channel you want to send the message to
    while True:
        await channel.send("Hello, World!")
        await asyncio.sleep(20) # Wait for 20 seconds before sending the next message

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")
    # Start the send_message coroutine when the bot is ready
    client.loop.create_task(send_message())

# Run the bot with your bot token
client.run('qLRc92J2MORZm7HGG3d64wNyVKHUFUGo')
