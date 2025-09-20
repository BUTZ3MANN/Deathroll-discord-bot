from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Permissions, utils
from responses import start_deathroll, roll_deathroll, forfeit_deathroll, finish_deathroll

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
CLIENT_ID: Final[str] = os.getenv("DISCORD_CLIENT_ID")  # Add your bot's client ID in the .env file

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Handle messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    user_message: str = message.content
    user_id: int = message.author.id  # Store user ID instead of name

    # Generate an invite link dynamically
    if user_message.startswith("!invite"):
        permissions = Permissions(
            send_messages=True,
            read_message_history=True,
            view_channel=True,
            embed_links=True,  # Optional: If you use rich embeds
        )
        invite_url = utils.oauth_url(CLIENT_ID, permissions=permissions)
        await message.channel.send(f"Invite the bot using this link: {invite_url}")
        return

    # Start Deathroll: "!deathroll @opponent"
    if user_message.startswith("!deathroll"):
        if not message.mentions:
            await message.channel.send("Usage: `!deathroll @opponent`")
            return
        
        opponent_id = message.mentions[0].id
        response = start_deathroll(user_id, opponent_id)
        await message.channel.send(response)
        return

    # Roll command: "!roll <current_number>"
    if user_message.startswith("!roll"):
        parts = user_message.split()
        if len(parts) < 2:
            await message.channel.send("Usage: `!roll <current_number>`")
            return
        
        response = roll_deathroll(user_id, parts[1])
        await message.channel.send(response)
        return

    # Forfeit command: "!forfeit"
    if user_message.startswith("!forfeit"):
        response = forfeit_deathroll(user_id)
        await message.channel.send(response)
        return

    # Finish command: "!finish"
    if user_message.startswith("!finish"):
        response = finish_deathroll(user_id)
        await message.channel.send(response)
        return

# Bot startup
@client.event
async def on_ready() -> None:
    print(f"{client.user} is online")

# Run bot
def main() -> None:
    client.run(TOKEN)

if __name__ == "__main__":
    main()
