import pygame
import math
import random

from pygame.color import Color
from pygame.sprite import Sprite

from player import *
from System import *
from animation import *

def drawobject(obj, x, y):
        screen.blit(obj, (x, y))

def monster_move_y(y, count, r, scy, hp):
    if y < scy/2 and count == 0:
        y += 0.5*math.sin(45)*r + 0.5*1*math.pow(r,2)
        if r < 5:
            r += 0.05
    elif y < scy and count == 0:
        y += 0.5*math.sin(90)*r + 0.5*1*math.pow(r,2)
        if r > 2:
            r -= 0.001
    else:
        if count == 0:
            count = 1
        y -= 0.1*math.sin(45)*r + 0.1*1*math.pow(r,2)
        r += 0.05
    return y, [r, count]

class obj_monster_001(Animation):
    def __init__(self):
        self.s_image = s_monster_001
        self.s_width = s_monster_001_width
        self.s_height = s_monster_001_height
        self.s_columns = s_monster_001_frame
        self.fps = s_monster_001_fps
        self.init_animation()
        
        self.hp = []
        self.xy = []
        self.cr = []
        self.x = []

        self.bullet_xy = []

    def update(self):
        monster_att = obj_monster_001_attack()
        if len(self.xy) != 0:
            self.calc_next_frame()
            for i, mxy in enumerate(self.xy):
                mxy[1] += self.x[i]
                mxy[2], self.cr[i] = monster_move_y(mxy[2], self.cr[i][1], self.cr[i][0], 200, self.hp[i])
                    
                if self.cr[i][1] == 1:
                    monster_att_radians = math.radians(-180) + math.atan2((mxy[2] - p_y),(mxy[1] - p_x))
                    monster_att_x = 4*math.cos(monster_att_radians)
                    monster_att_y = 4*math.sin(monster_att_radians)
                    self.bullet_xy.append([mxy[1], mxy[2]])
                self.xy[i][2] = mxy[2]
                
        rect = (self.s_width*self.c_frame, 0,
                self.s_width, self.s_height)
        self.image.blit( self.s_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))

class obj_monster_001_attack(Animation):
    def __init__(self):
        self.s_image = s_monster_001_attack
        self.s_width = s_monster_001_att_width
        self.s_height = s_monster_001_att_height
        self.s_columns = s_monster_001_att_frame
        self.fps = s_monster_001_att_fps
        self.init_animation()

    def update(self):
        self.calc_next_frame()
        
        rect = (self.s_width*self.c_frame, 0,
                self.s_width, self.s_height)
        self.image.blit( self.s_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))
