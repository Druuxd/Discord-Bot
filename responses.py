import random
import champions


def handle_response(message, id) -> str:
    p_message = message.lower()
    random_champion = random.choice(champions.champion_list)

    print(f"Received message: {p_message}")

    if p_message == 'ce campion sa ma joc pe lol?':
        return f"<@{id}> Hmmmm, Malphite or Garen!"

    if p_message == '!ce campion sa ma joc pe lol?':
        return f"<@{id}> Hmmmm, try {random_champion}"

    if p_message == 'tuff':
        return f"<@{id}> , Tuff rau ngl!"

    if p_message == 'sad':
        return f"<@{id}> , You should KILL YOURSELF, NOW!"

    if p_message == 'hello':
        return f"<@{id}> , Hey there!"

    if p_message == 'roll':
        return f"<@{id}> , {str(random.randint(1, 6))} !"

    if p_message == '!help':
        return f"`<@{id}> , no.`"
