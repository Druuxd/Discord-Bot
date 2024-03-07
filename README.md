# Lurk, the Discord Bot 🤖

Lurk is a Discord bot crafted in Python, designed to provide instant access to information about anime and manga using the MyAnimeList API.

## Introduction

I am a very big Manga and Anime enthusiast and I also use Dicord quite a lot. I knew about MyAnimeList so I thought to myself "Why not try and make a bot that can easily give me the details about any Anime or Manga that I'm interested in?", and that's the story behin how I came up with the idea of **Lurk**.

## Features

- **Effortless Information Retrieval**: Instantly fetch details about anime and manga directly from Discord.
- **Real-time Data**: Utilizes the MyAnimeList API to ensure accurate and up-to-date information.
- **Comprehensive Details**: Provides essential information such as title, rank, mean score, episode/chapter count, and status.
- **Efficient Parsing**: Employs BeautifulSoup for efficient parsing of HTML content, ensuring smooth operation.

## Getting Started

1. **Invite Lurk**: Add the bot to your Discord server.
2. **Simple Querying**: Type 'anime:' or 'manga:', followed by the title you're interested in.
3. **Instant Response**: Lurk will promptly provide detailed information about the requested anime or manga.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- Discord.py
- Requests library
- BeautifulSoup4

## Installation

1. **Clone the Repository**:
  `git clone https://github.com/Druuxd/Discord-Bot.git`

2. **Install Dependencies**:
  `pip install -r requirements.txt`

3. **Run the Bot**:
  `python main.py`


## Obtaining API Keys

To enable the bot's functionality, you'll need API keys from MyAnimeList and a Discord Bot's TOKEN. Follow these steps:

- **Create a Discord Application and obtain the BOT TOKEN**: [Create Discord BOT](https://discord.com/developers/applications)
- **Obtain MyAnimeList API Key**: [MyAnimeList API](https://myanimelist.net/apiconfig)
- **Update Credentials**: Replace 'TOKEN' in 'bot.py' and 'client_id' in 'responses.py' with your own API credentials.

(*Note: For security purposes, consider using separate credential files or environmental variables.*)

## Commands

**Use '?' before any command to receive a DM response from the bot.**

- `!commands`: Displays a list of available commands.
- `anime:[anime title]`: Search for details about a specific anime.
- `manga:[manga title]`: Search for details about a specific manga.

## Example Usage

![example](https://i.imgur.com/cGZs3ju.png)

## Credits

This project was developed by Darius Andrei.

## Disclaimer

Lurk is an educational project and is not affiliated with MyAnimeList or Discord.
