import window.player
import jozin.player
import example.player
from gomoku_tournament import GomokuTournament

playerX = jozin.player.Player(1)
playerO = window.player.Player(-1)

tournament = GomokuTournament(playerX, playerO, 300)
winner = tournament.game()
tournament.save_logs()
print(f'winner is {winner}')
