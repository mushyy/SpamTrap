## Spam Trap Bot

This repository contains a small Discord moderation bot (spam trap) that monitors configured channels and bans users that trigger the trap, then posts a notification message to a configured notification channel.

This README explains how to configure and run the bot using Docker Compose (recommended) and gives troubleshooting tips.

## Configuration

The bot expects a YAML configuration file (the repo includes `config.yaml.example`). The application is run like:

`docker compose up -d` or `poetry run python main.py config.yaml`


Required configuration keys (as used by `main.py`):

- `discord_token` (string): your bot token
- `channel_mappings` (list of integers): channel IDs to monitor (messages by non-admins will get banned)
- `admins` (list of integers): user IDs exempt from the trap
- `notification_channel` (integer): channel ID where the bot will post a notification after banning someone
- `message` (string): message text that will be sent when someone is banned

Example `config.yaml` (already in repo):

```yaml
discord_token: "YOUR_BOT_TOKEN_GOES_HERE"
channel_mappings:
  - 123456789011121314
admins:
  - 123456789011121314
  - 123456789011121314
notification_channel: 123456789011121314
message: "User banned by spam trap"
```

### How to configure

1. Create the Discord Channel you wish to use make sure anyone can send a message there
2. Copy the ID from the channel and put it under channel_mappings
3. Copy your admin / moderator IDS and put it under admins
5. Set the discord notification channel by copying the ID from the channel and placing it under notification_channel
6. Decide what the message will be for example in WHUN for EVE its "Wormhole collapsed on"
7. Create a Discord bot
8. Invite bot to the server and give permissions to view channel, read message, and ban. Example - https://discord.com/oauth2/authorize?client_id=xxx&scope=bot&permissions=68614

## Running with Docker Compose

On Windows, Linux or Mac with Docker and Docker Compose installed, run the following to start:

```bash
docker compose up -d
```
