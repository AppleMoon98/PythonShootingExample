import pygame
import random
import math
import time

from pygame.color import Color
from pygame.sprite import Sprite

from player import *
from monster import *
from RGBColor import *
from System import *
                
def player_crash(p_x, p_y, s_p_width, s_p_height, s_p_l_x, s_p_l_y, m_x, m_y, xx=8):
    if p_x + (s_p_width/2) - (s_p_life_x/2) < m_x < p_x + (s_p_width/2) - (s_p_life_x/2) + s_p_life_x or m_x < p_x + (s_p_width/2) - (s_p_life_x/2) < m_x + xx:
        if p_y + (s_p_height/2) - (s_p_l_y/2) < m_y < p_y + (s_p_height/2) - (s_p_l_y/2) + s_p_l_y or m_y < p_y + (s_p_height/2) - (s_p_l_y/2) < m_y + xx:
            return True
        else:
            return False

# 이미지 출력
def drawobject(obj, x, y):
        screen.blit(obj, (x, y))

def rectobject(obj, rect):
        screen.blit(obj, rect)
        
# 게임이 구동되는 함수
def runGame():
        # 테스트 하는 곳
        monster_att_xy = []
        font = pygame.font.Font('katun.ttf',80)
        text = font.render(u"게임오버", True, (255, 255, 255))

        font2 = pygame.font.Font('score.ttf',20)
        
        # 플레이어 관련 함수
        p_attack_tf = False

        player_move = p_move()
        
        player_move.rect.x = p_x
        player_move.rect.y = p_y

        #UI 표시되는 플레이어 관련 함수
        player_power = 1.0
        player_life = 3
        player_life_ui = [True,True,True]
        player_score = 0

        # 백그라운드 좌표 값 관련 함수
        back1_move = game_sc_top
        back2_move = game_sc_top - game_sc_y

        # 총알 값 관련 함수
        previous_time = pygame.time.get_ticks()
        bullet_xy = []

        # 몬스터 관련 함수
        monster_001 = obj_monster_001()
        monster_001_att = obj_monster_001_attack()

        monster_item = []
        test_time = pygame.time.get_ticks()

        tt = 800

        # 게임 시작
        run = True
        while run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                                
                # 이동 관련 : <player_move.rect, 좌표> <player_move.s_move, 모션 관련> <p_attack_tf, 일단은 공격>
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:# ←
                        if player_move.rect.x > game_sc_left:
                                player_move.rect.x -= p_move_speed
                                if not p_attack_tf:
                                        player_move.s_move = 1
                                else:
                                        player_move.s_move = 4
                elif keys[pygame.K_RIGHT]:# →
                        if player_move.rect.x < game_sc_right - s_player_width:
                                player_move.rect.x += p_move_speed
                                if not p_attack_tf:
                                        player_move.s_move = 2
                                else:
                                        player_move.s_move = 5
                else:
                        if not p_attack_tf:
                                player_move.s_move = 0
                        else:
                                player_move.s_move = 3
                if keys[pygame.K_UP]:# ↑
                        if player_move.rect.y > game_sc_top:
                                player_move.rect.y -= p_move_speed
                elif keys[pygame.K_DOWN]:# ↓
                        if player_move.rect.y < game_sc_bottom - s_player_height:
                                player_move.rect.y += p_move_speed
                # 공격
                if keys[ord('z')]:
                        p_attack_tf = True
                        # current_time 현재 틱 입력
                        current_time = pygame.time.get_ticks()
                        # 50 딜레이 마다 명령어를 수행
                        if current_time - previous_time > 50:
                                # previous_time 틱 초기화
                                previous_time = current_time
                                bullet_xy.append([player_move.rect.x+(s_player_width/2)+(10-(bullet_x/2)), player_move.rect.y-bullet_y])
                                bullet_xy.append([player_move.rect.x+(s_player_width/2)-17, player_move.rect.y-bullet_y])
                                if player_power >= 3:
                                    bullet_xy.append([player_move.rect.x+(s_player_width/2)-34, player_move.rect.y-bullet_y+16])
                                if player_power >= 4:
                                    bullet_xy.append([player_move.rect.x+(s_player_width/2)+(27-(bullet_x/2)), player_move.rect.y-bullet_y+16])
                else:
                        p_attack_tf = False
                        
                # current_time 현재 틱 입력
                test02_time = pygame.time.get_ticks()
                # 400 딜레이 마다 명령어를 수행
                if test02_time - test_time > tt:
                        # previous_time 틱 초기화
                        test_time = test02_time
                        if tt > 200:
                                tt -= 10
                        player_score += 100
                        monster_001.hp.append(20)
                        random_x = random.randrange(-3,3)
                        if random_x < -1:
                                monster_001.xy.append([1, p_x+100, game_sc_top - 32])
                        elif random_x > 1:
                                monster_001.xy.append([1, p_x-100, game_sc_top - 32])
                        else :
                                monster_001.xy.append([1, p_x, game_sc_top - 32])
                        monster_001.cr.append([0, 0])
                        monster_001.x.append(random_x)

                # 백그라운드 흰색으로 초기화
                screen.fill(White)

                # 백그라운드 이동속도
                back1_move += 1
                back2_move += 1

                # 스테이지 백그라운드 설정 : stage 값이 스테이지에 따라 바뀔 배경을 선택
                if stage == 1:
                        drawobject(stage01, game_sc_left, game_sc_top)
                        drawobject(stage01_1, game_sc_left, back1_move)
                        drawobject(stage01_1, game_sc_left, back2_move)

                        # 움직이는 백그라운드 설정을 위한 초기화 값
                        if back1_move == game_sc_bottom:
                                back1_move = game_sc_top - game_sc_y
                        if back2_move == game_sc_bottom:
                                back2_move = game_sc_top - game_sc_y

                # 총알과 몬스터의 충돌을 계산
                if len(monster_001.xy) != 0 and len(bullet_xy) != 0:
                        for j, mxy in enumerate(monster_001.xy):
                                for i, bxy in enumerate(bullet_xy):
                                        if mxy[1] < bxy[0] < mxy[1] + 32 and mxy[2] < bxy[1] < mxy[2]+32:
                                                bullet_xy.remove(bxy)
                                                monster_001.hp[j] -= 1
                                                if monster_001.hp[j] < 1:
                                                        monster_001.xy.remove(mxy)
                                                        monster_001.hp.remove(monster_001.hp[j])
                                                        monster_001.cr.remove(monster_001.cr[j])
                                                        monster_001.x.remove(monster_001.x[j])
                                                        player_score += 1000
                                                        monster_item.append([mxy[1], mxy[2]])

                # 총알이 맵에 1개 이상 있을 경우
                if len(bullet_xy) != 0:
                        # 각각 총알을 나열
                        for i, bxy in enumerate(bullet_xy):
                                # 총알 이동 : bxy[0] => x값, bxy[1] => y
                                bxy[1] -= bullet_speed
                                bullet_xy[i][1] = bxy[1]
                                drawobject(bullet, bxy[0], bxy[1])
                                if bxy[1] <= game_sc_top - bullet_y:
                                        bullet_xy.remove(bxy)

                # 아이템 아이템 아이템 아이템 아이템
                if len(monster_item) != 0:
                        for i, ixy in enumerate(monster_item):
                                ixy[1] += 2
                                        
                                monster_item[i] = [ixy[0], ixy[1]]
                                drawobject(pygame.image.load('sprite/power.png'),ixy[0], ixy[1])
                                if player_crash(player_move.rect.x, player_move.rect.y, s_player_width, s_player_height, s_p_life_x, s_p_life_y, ixy[0], ixy[1], 32):
                                        monster_item.remove(ixy)
                                        if player_power < 4:
                                            player_power += 0.1
                                        player_score += 500

                # 플레이어 이미지 출력
                # 왼쪽으로 이동할 경우
                player_move.update()
                rectobject(player_move.image, player_move.rect)

                # 플레이어 목숨 이미지 출력
                drawobject(s_p_life, player_move.rect.x + (s_player_width/2) - (s_p_life_x/2),
                           player_move.rect.y + (s_player_height/2) - (s_p_life_y/2))
                
                #몬스터 테스트
                monster_001.update()
                for i, mxy in enumerate(monster_001.xy):
                        drawobject(monster_001.image, mxy[1], mxy[2])
                        monster_att_radians = math.radians(-180) + math.atan2((mxy[2] - player_move.rect.y + (64/2) - (8/2)),(mxy[1] - (player_move.rect.x + (32/2) - (8/2))))
                        monster_att_speed = random.randrange(1,5)
                        monster_att_y = monster_att_speed * math.sin(monster_att_radians)
                        monster_att_x = monster_att_speed * math.cos(monster_att_radians)
                        if monster_001.cr[i][1] == 1:
                                monster_att_xy.append([monster_att_x, monster_att_y])
                                monster_001.cr[i][1] = 2

                monster_001_att.update()
                if len(monster_001.bullet_xy) != 0:
                        for i, bxy in enumerate(monster_001.bullet_xy):
                                bxy[0] += monster_att_xy[i][0]
                                bxy[1] += monster_att_xy[i][1]
                                monster_001.bullet_xy[i] = [bxy[0], bxy[1]]
                                drawobject(monster_001_att.image, bxy[0], bxy[1])

                # 몬스터가 맵에 1마리 이상 있을 경우
                if len(monster_001.xy) != 0:
                        # 각각 몬스터를 나열
                        for i, mxy in enumerate(monster_001.xy):
                                # 맵 바깥으로 나갈 경우
                                if mxy[2] >= game_sc_bottom + 16 or mxy[1] <= game_sc_left-32 or mxy[1] >= game_sc_right or mxy[2] <= game_sc_top - 40:
                                        monster_001.xy.remove(mxy) # 제거
                                        monster_001.cr.remove(monster_001.cr[i]) # 얘도
                                        monster_001.hp.remove(monster_001.hp[i])
                                        monster_001.x.remove(monster_001.x[i])
                                

                #총알 충돌 총알 충돌 총알 충
                if len(monster_001.bullet_xy) != 0:
                        for i, bxy in enumerate(monster_001.bullet_xy):
                                if player_crash(player_move.rect.x, player_move.rect.y, s_player_width, s_player_height, s_p_life_x, s_p_life_y, bxy[0], bxy[1]):
                                        monster_001.bullet_xy.remove(bxy)
                                        monster_att_xy.remove(monster_att_xy[i])
                                        player_life -= 1
                                        player_life_ui[player_life] = False
                                        print("플레이어 목숨 : ", player_life)
                
                
                # UI 이미지 출력
                drawobject(ui, 0, 0)
                
                heart = pygame.image.load('sprite/heart.png')
                heart_zero = pygame.image.load('sprite/heart_zero.png')
                
                for i in range(3):
                        if player_life_ui[i]:
                                drawobject(heart, 450 + (i*50), 70)
                        else:
                                drawobject(heart_zero, 450 + (i*50), 70)

                if player_life < 1:
                        screen.blit(text, [100,100])
                        run = False

                texttext = str("{0:.1f}").format(player_power) + " / 4.0"
                text2 = font2.render(texttext, True, (0, 0, 255))
                screen.blit(text2, [450, 180])

                texttext2 = str(player_score).zfill(8)
                text3 = font2.render(texttext2, True, (0,0,0))
                screen.blit(text3, [490, 442])
                
                pygame.display.update()
                clock.tick(FPS)
		
        time.sleep(3)
        pygame.quit()
        quit()
	
# 실행
initGame()
runGame()
