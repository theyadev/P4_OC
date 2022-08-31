from views.create_player import create_player_view
from models.Player import Player


def create_player():
    player_data = create_player_view()

    player = Player.get_player_if_exists(
        player_data[0], player_data[1], player_data[2])

    if player is None:
        player = Player.new(*player_data)
    
    Player.save()

    return player
