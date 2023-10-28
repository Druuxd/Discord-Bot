import discord
import responses
import botapi

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True


async def send_message(message, user_message, username, is_private):
    try:
        # Call handle_response() to get the exact answer the user wants
        response = responses.handle_response(user_message, username)
        # Check weather the message should be sent in a DM or in a channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = botapi.id
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')  # Log

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        id = message.author.id  # Find the id of the use, used so that the bot can @ the user
        username = str(message.author)  # the username of the sender
        user_message = str(message.content)  # the message of the user
        # The channel where the message was sent
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")  # Log

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            # If the user used "?" then send a DM
            await send_message(message, user_message, id, is_private=True)
        elif user_message:
            await send_message(message, user_message, id, is_private=False)

    client.run(TOKEN)  # Start it up.
