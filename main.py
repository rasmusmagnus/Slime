import pygame
import render_constants
from renderables import Floor, Sky, GoalLine, Renderable, Goal

def main():
    pygame.init()
    screen = pygame.display.set_mode((render_constants.screen_length, render_constants.screen_height))
    pygame.display.set_caption("Slime Game")
    
    
    running = True
    game_objects = []
    sky = Sky()
    floor = Floor()
    left_goal = Goal(True)
    right_goal = Goal(False)
    goal_line_left = GoalLine(True)
    goal_line_right = GoalLine(False)
    game_objects.append(sky)
    game_objects.append(floor)
    game_objects.append(goal_line_right)
    game_objects.append(goal_line_left)
    game_objects.append(left_goal)
    game_objects.append(right_goal)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render_screen(screen, game_objects)
        pygame.display.flip()
    pyg.quit()

def render_screen(screen, game_objects: list[Renderable]):
    for obj in game_objects:
        obj.render(screen)
    
    
if __name__ == "__main__":
    main()
