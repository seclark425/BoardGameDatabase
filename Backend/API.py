import requests
from boardgame import boardgame
from xml.etree import ElementTree as ET


    
def find_game_all(game_name, exact):
    base_search_url = "https://boardgamegeek.com/xmlapi/search"    
    params = {"search": game_name}

    if exact:
        params["exact"] = 1

    try:
        response = requests.get(base_search_url, params = params)

        if response.status_code == 200:
            print("Request successful")
        else:
            print("error. Status code:{response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    
    root = ET.fromstring(response.text)

    game_list = []
    for game in root.findall(".//boardgame"):
        game_id = game.attrib["objectid"]
        game_title = game.find("name").text
        game_date = game.find("yearpublished").text

        print(f"game id: {game_id}, published: {game_date}, game title: {game_title}")
        new_game = boardgame(game_id, game_title)
        game_list.append(new_game)
    return game_list

def find_game_specific(game_id):
    url = f"https://boardgamegeek.com/xmlapi/boardgame/{game_id}?stats=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("request successful")
        else:
            print(f"error: {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"error: {err}")

    root = ET.fromstring(response.text)
    game = root.find("boardgame")
    if game.find("name") is None:
        return None
    name = game.find("name").text
    min_players = game.find("minplayers").text
    max_players = game.find("maxplayers").text
    description = game.find("description").text
    weight = game.find("statistics").find("ratings").find("averageweight").text
    pic_link = game.find("image").text

    new_game = boardgame(game_id, name)
    new_game.set_weight(weight)
    new_game.set_description(description)
    new_game.set_pic(pic_link)
    new_game.set_min(min_players)
    new_game.set_max(max_players)

    return new_game



    
    
# def main():
#     game = input("What game would you like to add? ")
#     find_game_all(game, False)
#     specific_game = input("please enter the id of the specific game you'd like to add: ")
#     find_game_specific(specific_game)

# if __name__ == "__main__":
#     main()
