def play_next_turn(tournament):
    tournament.next_turn()
    tournament.turns[-1].set_scores()
    tournament.save()
