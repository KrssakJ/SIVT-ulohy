from random import randint

enemy_moves=[]
# AVOID 4-line, 3-line, 2-2, 1-3, 3/3


class Player:
    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'example'
    def play(self, opponent_move):
        if opponent_move == None:
            return (7, 7)
        enemy_moves.append(opponent_move)
        row, col = opponent_move
        return (row-2, col+3)
