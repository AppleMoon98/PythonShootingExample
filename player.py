import pygame

from pygame.color import Color
from animation import Animation
from RGBColor import *
from System import *

class p_move(Animation):
    def __init__(self):
        self.s_image = s_p_move_stop
        self.s_move = 0
        self.s_width = s_player_width
        self.s_height = s_player_height
        self.s_columns = s_player_frame
        self.fps = 8
        self.init_animation()

    def update(self):
        self.calc_next_frame()
        if self.s_move == 0:
            self.s_sheet = pygame.image.load(s_p_move_stop).convert()
        elif self.s_move == 1:
            self.s_sheet = pygame.image.load(s_p_move_left).convert()
        elif self.s_move == 2:
            self.s_sheet = pygame.image.load(s_p_move_right).convert()
        elif self.s_move == 3:
            self.s_sheet = pygame.image.load(s_p_attack_stop).convert()
        elif self.s_move == 4:
            self.s_sheet = pygame.image.load(s_p_attack_left).convert()
        elif self.s_move == 5:
            self.s_sheet = pygame.image.load(s_p_attack_right).convert()

        rect = (self.s_width*self.c_frame, 0,
                self.s_width, self.s_height)
        self.image.blit( self.s_sheet, (0, 0), rect)
