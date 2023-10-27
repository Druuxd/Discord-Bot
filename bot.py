import discord
import responses
import botapi

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True


async def send_message(message, user_message, username, is_private):
    try:
        response = responses.handle_response(user_message, username)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = botapi.id
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        id = message.author.id
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, id, is_private=True)
        elif user_message:
            await send_message(message, user_message, id, is_private=False)

    client.run(TOKEN)
