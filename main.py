import sys
import discord
import yaml
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_config(filename):
    try:
        with open(filename, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Loading config error {e}")

def validate_config(config):
    required_keys = ["discord_token", "channel_mappings", "admins", "notification_channel", "message"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")

    if not isinstance(config["channel_mappings"], list):
        raise ValueError("channel_mappings must be a list")

    if not isinstance(config["notification_channel"], int):
        raise ValueError("notification_channel must be a integer")

    if not isinstance(config["admins"], list):
        raise ValueError("admins must be a list")
            

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} config.yml")
    sys.exit(1)

config = load_config(sys.argv[1])
validate_config(config)
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    try:
        logging.info("Bot is now ready")

        for channel_id in config["channel_mappings"]:
            channel = client.get_channel(channel_id)
            if channel:
                logging.info(f"Channel monitoring - {channel.id} called {channel.name}")

    except Exception as e:
        logger.critical(f"Unable to ready up - {e}")

@client.event
async def on_message(message):
    try:
        if message.channel.id in config["channel_mappings"] and message.author.id not in config["admins"]:
            author = message.author
            channel = client.get_channel(config["notification_channel"])
            await author.ban(delete_message_seconds=1800, reason="Spam trap")
            await channel.send(f"{config['message']} <@{author.id}>")


    except Exception as e:
        logger.critical(f"Error On Message: {e}")

client.run(config["discord_token"], reconnect=True)