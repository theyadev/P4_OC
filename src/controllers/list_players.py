"""Controller to render the list players view."""

from views.list_players import list_players_view
from models.Player import Player


def list_players():
    """List players."""
    list_players_view(Player._list)
