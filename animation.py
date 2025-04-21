import pygame
from pygame import Surface
from pygame.color import Color
from pygame.sprite import Sprite


class Animation(Sprite):
    def init_animation(self):
        Sprite.__init__(self)

        self.s_sheet = pygame.image.load(self.s_image).convert()
        self.c_frame = 0
        self.image = Surface((self.s_width, self.s_height))

        rect = (self.s_width*self.c_frame, 0,
                self.s_width, self.s_height)
        self.image.blit( self.s_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))
        self.rect = self.image.get_rect()
        self.elapsed = pygame.time.get_ticks()
        self.threshold =    1000/self.fps

    def calc_next_frame(self):
        tick = pygame.time.get_ticks()
        if tick - self.elapsed > self.threshold:
            self.elapsed = tick
            if self.c_frame == self.s_columns:
                self.c_frame = 0
            else:
                self.c_frame += 1
