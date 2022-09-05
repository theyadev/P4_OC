"""Controller to render the list matches view."""

from views.list_matches import list_matches_view


def list_matches(turn):
    """List matches."""
    list_matches_view(turn.matchs)
