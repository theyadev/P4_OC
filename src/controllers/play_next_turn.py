"""Controller to render the play next turn view."""


def play_next_turn(tournament):
    """Play next turn."""
    tournament.next_turn()
    tournament.turns[-1].set_scores()
    tournament.save()
