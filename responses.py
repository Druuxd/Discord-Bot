import random
import myapi
import requests
from bs4 import BeautifulSoup
import re
import champions


def handle_response(message, id) -> str:
    p_message = message.lower()  # lowercase so there is no confusion
    random_champion = random.choice(
        champions.champion_list)  # Pick one champion randomly

    print(f"Received message: {p_message}")  # Log

    if p_message.startswith("anime:"):
        # Only take the thing written after "anime:"
        anime_name = p_message.replace('anime:', '').strip()
        print(anime_name)  # Log to see if everything is working as it should

        # Set the URL for the MyAnimeList search page
        # Replace spaces with "+"
        url = f"https://myanimelist.net/anime.php?q={anime_name.replace(' ', '+')}"
        print(url)  # Log

        # Send a GET request to the URL
        response = requests.get(url)

        # Code that represents the connection is good
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all search results
            results = soup.find_all('a', class_='hoverinfo_trigger')

            # Function to check for an exact match
            # Had a problem where if you for example passed the "Death Note" name, it would give the details of "Death Note: Rewrite", so now we search for an exact match of the anime we want.
            def is_exact_match(result, anime_name):
                # lowercase so there is no confusion
                return anime_name.lower() == result.text.strip().lower()

            # Search for the exact match
            exact_match = next(
                (result for result in results if is_exact_match(result, anime_name)), None)

            if exact_match:
                # Extract the anime URL
                anime_url = exact_match['href']

                # Use regular expressions to extract the ID (numbers) from the URL
                # Found a forum post that explained how to find the details of an exact anime and each of them has an id, it is found in the url of the anime.
                anime_id_match = re.search(r'/anime/(\d+)', anime_url)
                anime_id = anime_id_match.group(
                    1) if anime_id_match else "Anime ID not found"

                client_id = myapi.id  # MAL API

                # Set up the API endpoint and parameters
                # Here we use the id we took from the original url
                url = f"https://api.myanimelist.net/v2/anime/{anime_id}"
                print(url)  # Log
                params = {
                    "fields": "main_picture,rank,mean,num_episodes,status,alternative_titles"
                }

                # Found all the tags on the api config page from MAL

                # Set the X-MAL-CLIENT-ID header (Found this in the same post as line:47)
                headers = {
                    "X-MAL-CLIENT-ID": client_id
                }

                # Make the API request
                response = requests.get(url, params=params, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    # Here I'm just changing the base returns to cleaner ones
                    if data["status"] == "finished_airing":
                        data["status"] = "Finished"
                    elif data["status"] == "currently_airing":
                        data["status"] = "Currently Airing"
                    else:
                        data["status"] = "Not yet aired"

                    # The main picture has a data[] of itself because it has 2 sizes of the image.
                    main_picture = data["main_picture"]
                    # Reply with a message containing all the details
                    return f'<@{id}>{main_picture["medium"]}\nTitle: {data["title"]}\n Rank: {data["rank"]}\t Mean Score: {data["mean"]}\n Episodes: {data["num_episodes"]}\n Status: {data["status"]}'
                else:
                    return f"<@{id}>Failed to retrieve data from MyAnimeList API. Status Code: {response.status_code}"
            else:
                return f"<@{id}>Anime not found."

        else:
            return f"<@{id}>Failed to connect to MyAnimeList."

    # Manga is the same as anime, just keywords changed
    if p_message.startswith("manga:"):
        manga_name = p_message.replace('manga:', '').strip()
        print(manga_name)

        url = f"https://myanimelist.net/manga.php?q={manga_name.replace(' ', '+')}"
        print(url)

        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find_all('a', class_='hoverinfo_trigger')

            def is_exact_match(result, manga_name):
                return manga_name.lower() == result.text.strip().lower()

            exact_match = next(
                (result for result in results if is_exact_match(result, manga_name)), None)

            if exact_match:

                manga_url = exact_match['href']

                manga_id_match = re.search(r'/manga/(\d+)', manga_url)
                manga_id = manga_id_match.group(
                    1) if manga_id_match else "Manga ID not found"

                client_id = myapi.id

                url = f"https://api.myanimelist.net/v2/manga/{manga_id}"
                print(url)
                params = {
                    "fields": "main_picture,rank,mean,num_volumes,num_chapters,status"
                }

                headers = {
                    "X-MAL-CLIENT-ID": client_id
                }

                response = requests.get(url, params=params, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    if data["status"] == "finished":
                        data["status"] = "Finished"
                    elif data["status"] == "currently_publishing":
                        data["status"] = "Currently Publishing"
                    else:
                        data["status"] = "Not yet published"

                    main_picture = data["main_picture"]
                    return f'<@{id}>\n{main_picture["medium"]}\nTitle: {data["title"]}\n Rank: {data["rank"]}\t Mean Score: {data["mean"]}\n Chapters: {data["num_chapters"]}\tVolumess: {data["num_volumes"]}\n Status: {data["status"]}'
                else:
                    return f"<@{id}>Failed to retrieve data from MyAnimeList API. Status Code: {response.status_code}"
            else:
                return f"<@{id}>Manga not found"

        else:
            return f"<@{id}>Failed to connect to MyAnimeList."

    if p_message == 'what champion should i play?':
        return f"<@{id}> Hmmmm, Malphite or Garen!"

    if p_message == '!what champion should i play?':
        return f"<@{id}> Hmmmm, try {random_champion}"

    if p_message == 'tuff':
        return f"<@{id}> , Tuff rau ngl!" #x

    if p_message == 'hello':
        return f"<@{id}> , Hey there!"

    if p_message == 'roll':
        return f"<@{id}> , {str(random.randint(1, 100))} !"

    if p_message == '!help':
        return f"<@{id}> `, no.`"
