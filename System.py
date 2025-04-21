import pygame

from pygame.color import Color
from pygame.sprite import Sprite
from RGBColor import *

# 스크린 >> 가로 : 640 X 세로 : 480 / FPS : 120
TITLE =  "1724018 종스크롤 슈팅 배지호"
sc_width = 640
sc_height = 480
FPS = 120

# 게임 켜기 위한 부가적인 코드
screen = pygame.display.set_mode([sc_width, sc_height])
clock = pygame.time.Clock()

# 게임 스크린
game_sc_x = 385
game_sc_y = 448

game_sc_top = 16
game_sc_bottom = 464
game_sc_left = 32
game_sc_right = 417

# 이미지 로드
s_p_move_stop = 'sprite/p_move.png'
s_p_move_left = 'sprite/p_move_l.png'
s_p_move_right = 'sprite/p_move_r.png'

s_p_attack_stop = 'sprite/p_attack.png'
s_p_attack_left = 'sprite/p_attack_l.png'
s_p_attack_right = 'sprite/p_attack_r.png'

s_p_life = pygame.image.load('sprite/p_life.png')

s_monster_001 = 'sprite/s_monster_001.png'
s_monster_001_attack = 'sprite/s_monster_001_attack.png'

p_image = pygame.image.load('sprite/player.png')
bullet = pygame.image.load('sprite/bullet.png')
ui = pygame.image.load('sprite/User_Interface.png')

stage01 = pygame.image.load('background/stage01.png')
stage01_1 = pygame.image.load('background/stage01_1.png')

# 플레이어 >> 가로 : 32 X 세로 : 48
s_player_width = 36
s_player_height = 48
s_player_frame = 3

s_p_life_x = 8
s_p_life_y = 8

i_player_width = 120
i_player_height = 392

p_x = int((game_sc_x + s_player_width) / 2)
p_y = game_sc_y - s_player_height

#플레이어 모션 : 0 -> 평상시, 1 -> 공격 모션
s_player_motion = 0

stage = 1

# 플레이어 이동속도 : p_move_speed
p_move_speed = 2
stop = 0

# 말풍선 관련
#font = pygame.font.Font("a카툰.ttf",20)
#text = font.render(u"안녕하세요", True, (255, 255, 255))

# 몬스터 관련
line = [[100,200]]

s_monster_001_width = 32
s_monster_001_height = 32
s_monster_001_frame = 2
s_monster_001_fps = 12

s_monster_001_att_width = 8
s_monster_001_att_height = 8
s_monster_001_att_frame = 2
s_monster_001_att_fps = 12

# 몬스터 기본 이동속도 : m_move_speed
m_move_speed = 2

# 이동 관련 >> 총알 기본 이동속도 : bullet_speed
bullet_x = 14
bullet_y = 32
bullet_speed = 7

# 게임을 초기화하고 시작하는 함수
def initGame():
	# 라이브러리 초기화
	pygame.init()
	pygame.display.set_caption(TITLE)	
	
