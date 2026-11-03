from pygame import K_a, K_d, K_w, K_s, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_k

class MoveMap:
    map = {}
    def __init__(self):
        self.map = {K_a : PlayerMove((-0.125,0), True),
               K_d : PlayerMove((0.125,0), True),
               K_w: PlayerMove((0,-0.125), True),
               K_s : PlayerMove((0,0.125), True),
               K_LEFT : PlayerMove((-0.125,0), False),
               K_RIGHT : PlayerMove((0.125,0), False),
               K_UP: PlayerMove((0,-0.125), False),
               K_DOWN : PlayerMove((0,0.125), False)
               }

class PlayerMove:
    is_player_one = True
    move = (0,0)
    def __init__(self, move, is_player_one):
        self.move = move
        self.is_player_one = is_player_one

    def add(self, playerMove : PlayerMove) -> PlayerMove:
        if playerMove.is_player_one != self.is_player_one:
            raise Exception("Cannot add player moves with incompatible player owners")
        move = [playerMove.move[i]+self.move[i] for i in range(len(playerMove.move)) ]
        return PlayerMove(move, self.is_player_one)
