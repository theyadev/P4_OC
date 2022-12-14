"""Controller to play all turns."""


def play_all_turns(tournament):
    """Play all turns."""
    while tournament.max_turns > tournament.current_round:
        tournament.next_turn()
        tournament.turns[-1].set_scores()
        tournament.save()
