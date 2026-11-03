import pygame
import render_constants
import numpy
from pygame import Event
from move_map import MoveMap, PlayerMove
from renderables import Floor, Player, Sky, GoalLine, Renderable, Goal

def main():
    pygame.init()
    screen = pygame.display.set_mode((render_constants.screen_length, render_constants.screen_height))
    pygame.display.set_caption("Slime Game")
    
    
    running = True
    move_map = MoveMap()
    game_objects = []
    sky = Sky()
    floor = Floor()
    left_goal = Goal(True)
    right_goal = Goal(False)
    goal_line_left = GoalLine(True)
    goal_line_right = GoalLine(False)
    player1 = Player(True)
    player2 = Player(False)

    game_objects.append(sky)
    game_objects.append(floor)
    game_objects.append(goal_line_right)
    game_objects.append(goal_line_left)
    game_objects.append(left_goal)
    game_objects.append(right_goal)
    game_objects.append(player1)
    game_objects.append(player2)
    pygame.key.set_repeat(True)


    while running:
        moves = []
        pressed = pygame.key.get_pressed()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.KEYDOWN and event.key in move_map.map.keys():
        moves += [move_map.map[key] for key in move_map.map.keys() if pressed[key]]
        if len(moves) > 0:
            reduced = reduce(moves)
            player2.set_player_velocity(reduced[1])
            player1.set_player_velocity(reduced[0])
        else:
            player1.reset_player_velocity()
            player2.reset_player_velocity()
        player1.update_player_pos()
        player2.update_player_pos()
        
        render_screen(screen, game_objects)
        pygame.display.flip()
    pyg.quit()

def reduce(moves : list[PlayerMove]):
    player_1_moves = [move for move in moves if move.is_player_one == True] 
    player_2_moves = [move for move in moves if move.is_player_one == False]
    player_1_move = PlayerMove((0,0), True)
    for i in range(len(player_1_moves)):
        player_1_move = player_1_move.add(player_1_moves[i])
    player_2_move = PlayerMove((0,0), False)
    for i in range(len(player_2_moves)):
        player_2_move = player_2_move.add(player_2_moves[i])
    return (player_1_move, player_2_move)


def render_screen(screen, game_objects: list[Renderable]):
    for obj in game_objects:
        obj.render(screen)
    
    
if __name__ == "__main__":
    main()
