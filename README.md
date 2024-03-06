# Lurk, the Discord Bot 🤖

A Discord bot developed in Python to provide information about anime and manga using the MyAnimeList API.

## Introduction

I am a very big manga and anime enthusiast and I also use Dicord quite a while. I knew about MyAnimeList so I thought to myself "Why not try and make a bot that can easily give me the details about any Anime or Manga that I'm interested in?", and that's the story behin **Lurk**.

## Features

- Search for details about anime and manga directly from Discord.
- Utilizes the MyAnimeList API to provide accurate and up-to-date information.
- Provides information such as title, rank, mean score, number of episodes/chapters, and status.
- Scraping with BeautifulSoup, enabling efficient parsing of HTML content.

## How to Use

1. Invite the bot to your Discord server.
2. Type '?' followed by either 'anime:' or 'manga:' and the title of the anime or manga you want to search for.
3. The bot will respond with detailed information about the requested anime or manga.

## Requirements

- Python 3.x
- Discord.py
- Requests library
- BeautifulSoup4

## Installation

1. Clone this repository:
`git clone https://github.com/your-username/anime-manga-discord-bot.git`

2. Install the required dependencies:
`pip install -r requirements.txt`

3. Run the bot:
`python main.py`

## Obtain API keys:

- [MyAnimeList API](https://myanimelist.net/apiconfig)

- Replace **TOKEN** from **bot.py** and **client_id** from **responses.py** with your own bot token and your cliend id, from MyAnimeList.
  - I used two separate *.py* files to store them, you can use *.env, .txt, etc.* Or just replace them directly in the code.

## Commands
**If you use '?' before any command, the bot will respond with a DM**

- !commands: Shows a list of commands.

- anime:**[anime title]**: Search for details about a specific anime.

- manga:**[manga title]**: Search for details about a specific manga.

## Example Usage

![example](https://i.imgur.com/cGZs3ju.png)

## Credits

This project was developed by *Darius Andrei*.

## Disclaimer

This bot is developed for educational purposes and is not affiliated with MyAnimeList or Discord.
