"""Controller to render the list rounds view."""

from views.list_rounds import list_rounds_view


def list_rounds(tournament):
    """List rounds."""
    list_rounds_view(tournament.turns)
