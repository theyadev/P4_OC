from menu import print_menu
from input import custom_input


def choose_player_from_list_view(player_list, per_page=10):
    search = custom_input("Enter search: ")

    players = []

    for player in player_list:
        if search.isdigit():
            if player.rating == int(search):
                players.append(player)
            continue

        if search.lower() in player.first_name.lower() or search.lower() in player.last_name.lower():
            players.append(player)

    players = players[:per_page]

    if len(players) == 0:
        input("No players found, press Enter to continue...")
        return None

    player = print_menu([
        (player.__str__(), lambda player=player: player)
        for player in players
    ])

    return player
