import pygame
import render_constants
from abc import ABC, abstractmethod

class Renderable(ABC):

    @abstractmethod
    def render(screen):
        pass

class Sky(Renderable):
    colour = (1, 1, 255)
    def __init__(self):
        pass

    def render(self, screen):
        screen.fill(self.colour)


class GoalLine(Renderable):

    width = 3
    length = 0
    is_left_line = True
    def __init__(self, is_left_line):
        self.length = render_constants.screen_length*0.1
        self.is_left_line = is_left_line 


    def render(self, screen):
        screen_width = screen.get_size()[0]
        screen_height = screen.get_size()[1]
        if self.is_left_line:
            pygame.draw.line(screen, (255, 255, 255), (0,screen_height*(1-render_constants.floor_size_pct)), (self.length, screen_height*(1-render_constants.floor_size_pct)), self.width)
        else:
            pygame.draw.line(screen, (255, 255, 255), (screen_width-self.length,screen_height*(1-render_constants.floor_size_pct)), (screen_width, screen_height*(1-render_constants.floor_size_pct)), self.width)

class Floor(Renderable):
    height = 0
    color = (128, 128, 128)

    def __init__(self):
        height = render_constants.floor_size_pct * render_constants.screen_height


    def render(self, screen):
        rect = pygame.Rect(0,render_constants.screen_height*(1-render_constants.floor_size_pct),render_constants.screen_length,render_constants.screen_height*render_constants.floor_size_pct)
        screen.fill(self.color, rect)


class Goal(Renderable):
    is_left_goal = True
    def __init__(self, is_left_goal : bool):
        self.is_left_goal = is_left_goal

    def render(self, screen):
        lines_seperation_distance = render_constants.goal_width / 7 

        x_shift = 0

        if self.is_left_goal:
            x_shift = 0
        else:
            x_shift = render_constants.screen_length - render_constants.goal_width

        for i in range(0, 8):
            
            line_width = 1

            if i == 7 and self.is_left_goal:
                line_width = 4
            elif i == 0 and not self.is_left_goal:
                line_width = 4
            point_lower = (x_shift + lines_seperation_distance * i, render_constants.floor_height)
            point_upper = (x_shift + lines_seperation_distance * i, render_constants.floor_height - render_constants.goal_height)
            pygame.draw.line(screen, (255, 255, 255), point_lower, point_upper, line_width)

        for i in range (0, 15):
            point_left = (x_shift, render_constants.floor_height - lines_seperation_distance * i)
            point_right = (x_shift + render_constants.goal_width , render_constants.floor_height - lines_seperation_distance * i)
            pygame.draw.line(screen, (255, 255, 255), point_left, point_right)
