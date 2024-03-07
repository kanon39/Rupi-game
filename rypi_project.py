### 테스트 진행 ###
print("hellow_test")
print("hellow_test3333")

import pygame
import os
import random
import sys
# Global Constants
SCREEN_HEIGHT = 600 # 스크린 세로 길이
SCREEN_WIDTH = 1100 # 스크린 가로 길이
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 스크린 가로 세로 길이 정하기.
file_path ="C:/Users/stat_/Desktop/개발 프로젝트/rupi_game/"
rupi_path = "C:/Users/stat_/Desktop/개발 프로젝트/rupi_game/이미지/"
GAME_CLEAR_BG = pygame.image.load(os.path.join(rupi_path+"루피", "클리어.png"))
GAME_OVER_BG = pygame.image.load(os.path.join(rupi_path+"루피", "게임오버.png"))
GAME_START_BG1 = pygame.image.load(os.path.join(rupi_path+"루피", "시작1.png"))
GAME_START_BG2 = pygame.image.load(os.path.join(rupi_path+"루피", "시작2.png"))
EXPLAIN_BG1 = pygame.image.load(os.path.join(rupi_path+"루피", "설명1.png"))
EXPLAIN_BG2 = pygame.image.load(os.path.join(rupi_path+"루피", "설명2.png"))
EXPLAIN_BG3 = pygame.image.load(os.path.join(rupi_path+"루피", "설명3.png"))
EXPLAIN_BG4 = pygame.image.load(os.path.join(rupi_path+"루피", "설명4.png"))

RUNNING = [pygame.image.load(os.path.join(rupi_path+"루피", "걷는_루피_1.png")),
    pygame.image.load(os.path.join(rupi_path+"루피", "걷는_루피_2.png"))] # 용이 뛰는 사진
JUMPING = pygame.image.load(os.path.join(rupi_path+"루피",  "점프하는_루피.png"))
DUCKING = [pygame.image.load(os.path.join(rupi_path+"루피", "슬라이드_루피.png")),
           pygame.image.load(os.path.join(rupi_path+"루피", "슬라이드_루피1.png"))] # 용이 엎드린 사진

SMALL_CACTUS = [pygame.image.load(os.path.join(rupi_path+"장애물", "SmallPaper1.png")), # 수정
            pygame.image.load(os.path.join(rupi_path+"장애물", "SmallPaper2.png")),
            pygame.image.load(os.path.join(rupi_path+"장애물", "SmallPaper3.png"))] # 작은 선인장
LARGE_CACTUS = [pygame.image.load(os.path.join(rupi_path+"장애물", "LargePaper1.png")),
            pygame.image.load(os.path.join(rupi_path+"장애물", "LargePaper2.png")),
            pygame.image.load(os.path.join(rupi_path+"장애물", "LargePaper3.png"))] # 큰 선인장

BIRD = [pygame.image.load(os.path.join(rupi_path+"장애물", "Paper_bird1.png")),
    pygame.image.load(os.path.join(rupi_path+"장애물", "Paper_bird2.png"))]

CLOUD = pygame.image.load(os.path.join(file_path+"Assets/Other", "Cloud.png"))

BD = [pygame.image.load(os.path.join(rupi_path+"배경/낮", "건물1.png")),
            pygame.image.load(os.path.join(rupi_path+"배경/낮", "건물2.png")),
            pygame.image.load(os.path.join(rupi_path+"배경/낮", "건물3.png"))]

BG = pygame.image.load(os.path.join(file_path+"Assets/Other", "Track.png"))

ITEMS = [pygame.image.load(os.path.join(file_path+"Assets/Dino", "scissors1.png")),
    pygame.image.load(os.path.join(file_path+"Assets/Dino", "scissors2.png")),
    pygame.image.load(os.path.join(file_path+"Assets/Dino", "scissors3.png"))]

HEARTS = [pygame.image.load(os.path.join(file_path+"Assets/Dino", "hearts1.png")),
    pygame.image.load(os.path.join(file_path+"Assets/Dino", "hearts2.png")),
    pygame.image.load(os.path.join(file_path+"Assets/Dino", "hearts3.png"))]

RUPIMAIN = [pygame.image.load(os.path.join(rupi_path+"루피", "기본_루피.png"))]
RUPIPIVER = [pygame.image.load(os.path.join(rupi_path+"루피", "피버루피.png"))]
#RUPIJUMPE = [pygame.image.load(os.path.join(rupi_path+"/상태창", "장애물_접촉.png"))]


QR_IMAGE = [pygame.image.load(os.path.join(rupi_path+"장애물","beta50011.png")),
            pygame.image.load(os.path.join(rupi_path+"장애물","beta50012.png")),
            pygame.image.load(os.path.join(rupi_path+"장애물","beta50013.png"))]
PIVER_TIME = [pygame.image.load(os.path.join(rupi_path+"루피","분노111.png")),
            pygame.image.load(os.path.join(rupi_path+"루피","분노222.png"))]
BIG_ITEM = [pygame.image.load(os.path.join(rupi_path+"루피","대형비타5001.png")),
            pygame.image.load(os.path.join(rupi_path+"루피","대형비타5004.png"))]
pygame.init()
pygame.mixer.init()
# Global Constants
music_path = "C:/Users/stat_/Desktop/음악파일"
JUMP_MS=pygame.mixer.Sound(os.path.join(music_path, "jump2.wav"))
SLIDE_MS=pygame.mixer.Sound(os.path.join(music_path, "슬라이드1.wav"))
CLEAR_MS=pygame.mixer.Sound(os.path.join(music_path, "clear.wav"))
GAMEOVER_MS=pygame.mixer.Sound(os.path.join(music_path, "gameover.wav"))
ITEM_MS=pygame.mixer.Sound(os.path.join(music_path, "아이템1.wav"))
#PIVER_MS=pygame.mixer.Sound(os.path.join(music_path, "피버.wav"))
GAME_START_MS=pygame.mixer.Sound(os.path.join(music_path, "bgm.wav"))
GAME_START_MS.set_volume(0.5)
PIVER_MS = pygame.mixer.Sound(os.path.join(music_path, "피버.wav"))

class Rupichar: # 루피 CLASS
    # 글로벌 변수 지정 #
    X_POS = 80  # 루피 가로 크기지정 80
    Y_POS = 310 # 루피 세로 크기지정 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5 

    def __init__(self): # 루피 CLASS 내 함수들의 기본정보를 불러옴.(인수에 self가 들어가면 매번 아래값으로 초기화됨.)
        # 즉 루피가 처음 뛰기전 자리로 초기화 됨 #
        self.duck_img = DUCKING # duck_img 객체에 DUCKING 이미지들 저장
        self.run_img = RUNNING  # run_img 객체에 RUNNING 이미지들 저장
        self.jump_img = JUMPING # JUMP_img 객체에 JUMPING 이미지들 저장
        self.piver_img = PIVER_TIME # 피버 #######################################
        self.dino_duck = False # dino_duck 객체의 기본값은 False
        self.dino_run = True # dino_run 객체의 기본값은 True
        self.dino_jump = False # dino_jump 객체의 기본값은 False

        self.step_index = 0 # 장애물과의 거리
        self.jump_vel = self.JUMP_VEL # 점프 높이 지정
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect() #실제 반응하는 그림은 사각형
        self.dino_rect.x = self.X_POS #사각형 가로크기 초기화 
        self.dino_rect.y = self.Y_POS #사긱형 세로크기 초기화

    def update(self, userInput):# 키 입력에 따라 루피 위치 변경
        if self.dino_duck: 
            if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000) : ###########################################
                self.piverrun() ###########################################
            else :
                self.duck() # Run 함수 실행

        if self.dino_run: 
            if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000) : ###########################################
                self.piverrun() ###########################################
            else :
                self.run() # Run 함수 실행

        if self.dino_jump: 
            if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000) : ###########################################
                self.piverrun() ###########################################
            else :
                self.jump() # Run 함수 실행


        if self.step_index >= 10 : # 10: #장애물과의 거리가 10보다 더 커지면 장애물에 걸림
            self.step_index = 0 # ???

        if userInput[pygame.K_UP] and not self.dino_jump: # 키보드 업키를 누르며 루피가 점프중이 아니라면
            self.dino_duck = False # 엎드리기 불가
            self.dino_run = False # 달리기 불가
            self.dino_jump = True # 점프 가능
        elif userInput[pygame.K_DOWN] and not self.dino_jump: #키보드 다운키를 누르며 루피가 점프중이아니라면
            self.dino_duck = True # 엎드리기 가능
            self.dino_run = False # 달리기 불가능
            self.dino_jump = False # 점프 불가능
        elif not (self.dino_jump or userInput[pygame.K_DOWN]): # 루피가 점프하거나 키보드 다운키 둘중 하나가 아니라면
            self.dino_duck = False # 엎드리기 불가능
            self.dino_run = True # 달리기 가능
            self.dino_jump = False # 점프 불가능

    def duck(self):# 엎드리기 함수
        self.image = self.duck_img[self.step_index // 5] # 엎드릴 경우 장애물과의 거리가 5로 나누어짐
        self.dino_rect = self.image.get_rect() #__init__ 함수내 루피 초기 형태가져오기
        self.dino_rect.x = self.X_POS #__init__ 함수 내 루피 초기 형태가져오기
        self.dino_rect.y = self.Y_POS_DUCK #__init__ 함수 내 루피 초기 형태가져오기
        self.step_index += 5 # ?? 아직 이해 못함
        SLIDE_MS.play()

    def run(self): # 달리기 함수
        self.image = self.run_img[self.step_index // 5] # 달릴 경우 장애물과의 거리가 5로 나누어짐
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 5

    def piverrun(self): # 달리기 함수 ################################################3
        self.image = self.piver_img[self.step_index // 5] # 달릴 경우 장애물과의 거리가 5로 나누어짐
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS - 120
        self.step_index += 5


    def jump(self): # 점프 함수

        if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000) : ###########################################
            self.image = self.jump_img # 뛸 경우 뛰는 이미지 가져오기
            #self.jump_vel = 1
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 1 # 뛸 경우 기존 뛰는 거리의 4배만큼  # 4
                self.jump_vel -= 0.8
                JUMP_MS.play()
            if self.jump_vel < - self.JUMP_VEL:
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL
                JUMP_MS.play()
        else :
            #self.jump_vel = 8.5
            self.image = self.jump_img # 뛸 경우 뛰는 이미지 가져오기
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4 # 뛸 경우 기존 뛰는 거리의 4배만큼  # 4
                self.jump_vel -= 0.8
                JUMP_MS.play()
            if self.jump_vel < - self.JUMP_VEL:
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL
                JUMP_MS.play()


    def draw(self, SCREEN): # 루피 위치 시시각각 그리기
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud: # 구름이미지
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000) # 800에서 1000사이의 거리가 랜덤으로 선택됨
        self.y = random.randint(50, 100) # y는 50에서 100사이의 거리가 랜덤으로 선택됨
        self.image = CLOUD # 구름 이미지 같이 하기
        self.width = self.image.get_width() # 가로 같이 하기

    def update(self):
        self.x -= game_speed 
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Building_img1: # 건물이미지
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(300, 500) # 800에서 1000사이의 거리가 랜덤으로 선택됨
        self.y = -470 #random.randint(50, 100) # y는 50에서 100사이의 거리가 랜덤으로 선택됨
        self.image = BD[0]
        self.width = self.image.get_width() 

    def update(self):
        self.x -= game_speed 
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(300, 500)
            self.y = -470#random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Building_img2: # 건물이미지
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(2000, 3000) # 800에서 1000사이의 거리가 랜덤으로 선택됨
        self.y = -470 #random.randint(50, 100) # y는 50에서 100사이의 거리가 랜덤으로 선택됨
        self.image = BD[1] 
        self.width = self.image.get_width() # 가로 같이 하기

    def update(self):
        self.x -= game_speed 
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2000, 3000)
            self.y = -470#random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Building_img3: # 건물이미지
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(5000, 8000) # 800에서 1000사이의 거리가 랜덤으로 선택됨
        self.y = -470 #random.randint(50, 100) # y는 50에서 100사이의 거리가 랜덤으로 선택됨
        self.image = BD[2]
        self.width = self.image.get_width() # 가로 같이 하기

    def update(self):
        self.x -= game_speed 
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(5000, 8000)
            self.y = -470#random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

## 작은 비타 이미지 ##
class QRObstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            qrobstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class Qrclass(QRObstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
## 큰비타 이미지 ##
class bigbita:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            bigbitas.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class bigbitaclass(bigbita):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
##########################

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
        
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, qrobstacles, bigbitas
    run = True
    rupi_one = False
    rupi_two = False
    clock = pygame.time.Clock()
    player = Rupichar()
    cloud = Cloud()
    Building1 = Building_img1()
    Building2 = Building_img2()
    Building3 = Building_img3()
    if rupi_one :
        game_speed = 20 # 20
        points = 0
    else : 
        game_speed = 30
        points = 500

    x_pos_bg = 0
    y_pos_bg = 380
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    qrobstacles = []
    obstacles = []
    bigbitas= []
    death_count = 0


        

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
        
    ### 유저 가위 추가 부분 ##
    #def items():
    #    SCREEN.blit(ITEMS[0], (150, 65))
    #    SCREEN.blit(ITEMS[1], (190, 65))
    #    SCREEN.blit(ITEMS[2], (230, 65))

    ### 하트 추가 부분 ##
    #def hearts():
    #    SCREEN.blit(HEARTS[0], (150, 35))
    #    SCREEN.blit(HEARTS[1], (190, 35))
    #    SCREEN.blit(HEARTS[2], (230, 35))

    ### 루피 프로필 부분 ##
    def rupi_main():
        #SCREEN.blit(RUPIMAIN[0], (10, 10))
        if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000):
            SCREEN.blit(RUPIPIVER[0], (10, 10))
            #pygame.display.update()
        else :
            SCREEN.blit(RUPIMAIN[0], (10, 10))
            #pygame.display.update()

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
    

    time_limit = 120  # 시간 제한(초)
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    remaining_time = 100
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()

        cloud.draw(SCREEN)
        cloud.update()

        Building1.draw(SCREEN)
        Building1.update()
        
        #Building2.draw(SCREEN)
        #Building2.update()

        Building3.draw(SCREEN)
        Building3.update()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0: # 장애물 랜덤으로 등장
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))


        if len(qrobstacles) == 0: # 장애물 랜덤으로 등장
            if random.randint(0, 2) == 0:
                qrobstacles.append(Qrclass(QR_IMAGE))
        
        for qrobstacle in qrobstacles: # 충돌 발생
            if player.dino_rect.colliderect(qrobstacle.rect):
                ITEM_MS.play()
                qrobstacles.remove(qrobstacle)
                #pygame.time.delay(2000)
                points += 500
                #menu(death_count)
            qrobstacle.draw(SCREEN)
            qrobstacle.update()

        # 거대 비타 500 #
        #if (1000<=points<2000) or (3000<=points<4000):
        #    for event in pygame.event.get():
        #        if event.type == pygame.KEYDOWN :
        #            ### 캐릭터 선택 1 ###
        #            if event.key == pygame.K_RIGHT:
        #                if len(bigbitas) == 0: # 장애물 랜덤으로 등장
        #                    if random.randint(0, 1) == 0:
        #                        bigbitas.append(bigbitaclass(BIG_ITEM))
        #
        #            for bigbita in bigbitas: # 충돌 발생
         #               if player.dino_rect.colliderect(bigbita.rect):
          #                  ITEM_MS.play()
           #                 bigbitas.remove(bigbita)
            #                #pygame.time.delay(2000)
             ##              #menu(death_count)
               #         bigbita.draw(SCREEN)
                #        bigbita.update()
            #pygame.time.delay(2000)

        ##### 전체 시간 계산 ######
        # 남은 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(0, time_limit - elapsed_time)

        # 시간 표시
        text = font.render(f"Time: {remaining_time}s", True, (0, 0, 0))
        SCREEN.blit(text, (950, 70))

        # 게임 클리어 조건 #
        if (remaining_time <= 0) :
            game_clear()
        #########################

         ##### 스테이지별 문구 추가 ######
        if (remaining_time>=100) and (remaining_time<=120) :
            stage1 = font.render(f"Stage 1", True, (0, 0, 0))
            SCREEN.blit(stage1, (550, 40))
            #pygame.display.update()
        elif (remaining_time>=70) and (remaining_time<100) :
            stage2 = font.render(f"Stage 2", True, (0, 0, 0))
            SCREEN.blit(stage2, (550, 40))
            #pygame.display.update()
        elif (remaining_time>=30) and (remaining_time<70) :
            stage3 = font.render(f"Stage 3", True, (0, 0, 0))
            SCREEN.blit(stage3, (550, 40))
            #pygame.display.update()
        elif (remaining_time<30) :
            stage4 = font.render(f"Stage 4", True, (0, 0, 0))
            SCREEN.blit(stage4, (550, 40))
            #pygame.display.update()


            #if skill_count >= 5:
        #    clock = pygame.time.Clock()
        #    #print("clock : " ,clock)
        #    limitTime = 5000
        #    elapsedTime = 0
        #    #print("clock.get_time() : " , clock.get_time())
        #    elapsedTime += clock.get_time()
        #    #print("elapsedTime : " , clock.get_time())
        ##    if elapsedTime < limitTime :
         #       print("피버타임중")
        #        game_speed +=5
        #    else :
        #        print("피버타임끝")
        #        game_speed -=5
            

        
        #current_time = pygame.time.get_ticks()
        ##if (not fever_active and current_time - fever_start_time >= fever_duration) and skill_count >= 10:
        #    fever_active = True
        #fever_start_time = pygame.time.get_ticks()
        
        

        for obstacle in obstacles: # 충돌 발생
            #if (skill_count >= 5 )  : # 피버타임 #
            if (1000<=points<3000) or (5000<=points<8000) or (12000<=points<15000) or (18000<=points<20000):
                SCREEN.blit(RUPIPIVER[0], (10, 10))
                PIVER_MS.play()
                if player.dino_rect.colliderect(obstacle.rect):
                    obstacles.remove(obstacle)
                obstacle.draw(SCREEN)
                obstacle.update()
            else :
                SCREEN.blit(RUPIMAIN[0], (10, 10))
                PIVER_MS.stop()
                if player.dino_rect.colliderect(obstacle.rect):
                    #obstacles.remove(obstacle)
                    pygame.time.delay(2000)
                    game_over()
                obstacle.draw(SCREEN)
                obstacle.update()

        score()
        #items()
        rupi_main()
        


        clock.tick(30)
        pygame.display.update()

 
############################################
#### 사장 ####
def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_over()
############################################
# 캐릭터 이미지 로드
CHAR1 = pygame.image.load(os.path.join(rupi_path+"루피", "게임오버_1.png"))  # 캐릭터1 이미지 파일명에 맞게 수정
CHAR2 = pygame.image.load(os.path.join(rupi_path+"루피", "게임오버_2.png"))  # 캐릭터2 이미지 파일명에 맞게 수정
SELECT_CHAR = [pygame.image.load(os.path.join(file_path+"Assets/Dino", "white.png")),
               pygame.image.load(os.path.join(rupi_path+"루피", "걷는_루피_1.png")),
               pygame.image.load(os.path.join(file_path+"Assets/Dino", "white.png")),
               pygame.image.load(os.path.join(rupi_path+"루피", "걷는_루피_2.png"))]
clock = pygame.time.Clock()

## 캐릭터 선택창 ##
def character_selection():
    global points, CHAR1
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.SysFont('malgungothic', 15)

        # 캐릭터 이미지 출력
        SCREEN.blit(CHAR1, (300, 150))

        #################
        SCREEN.blit(CHAR2, (300, 300))
 
        # 이미지별 설명 #
        char1_explain = font.render("경력자: 난이도 (하).", True, (204, 102, 0))
        SCREEN.blit(char1_explain, (450,120))
        char1_explain = font.render("특징: 상대적으로 느린 속도로 진행된다. ", True, (0, 0, 0))
        SCREEN.blit(char1_explain, (450,160))
        char1_explain = font.render("클리어 가능성이 높기에 포인트를 얻을 수 있는 확률이 높다!", True, (0, 0, 0))
        SCREEN.blit(char1_explain, (450,210))
        #################
        SCREEN.blit(CHAR2, (300, 300))
        char1_explain = font.render("신입: 난이도 (상). < SPEED UP >", True, (204, 102, 0))
        SCREEN.blit(char1_explain, (450,290))
        char1_explain = font.render("특징: 더 빠른 속도로 진행되며 추가점수 5000점이 있다. ", True, (0, 0, 0))
        SCREEN.blit(char1_explain, (450,330))
        char1_explain = font.render("짧은 시간 내에 포인트 얻기가 가능하다.", True, (0, 0, 0))
        SCREEN.blit(char1_explain, (450,380))

        #################
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            ### 캐릭터선택 코드 ###
            if event.type == pygame.KEYDOWN :
                ### 캐릭터 선택 1 ###
                if event.key == pygame.K_UP:
                    rupi_one = True
                    for i in range(0,3) :
                       for j in range(0,4) :
                           CHAR_SELECT = SELECT_CHAR[j]
                           SCREEN.blit(CHAR_SELECT, (300, 150))
                           pygame.time.delay(100)
                           pygame.display.flip()
                    main()
                ### 캐릭터 선택 2 ###
                elif event.key == pygame.K_DOWN:
                    rupi_two = True
                    for i in range(0,3) :
                        for j in range(0,4) :
                           CHAR_SELECT = SELECT_CHAR[j]
                           SCREEN.blit(CHAR_SELECT, (300, 300))
                           pygame.time.delay(100)
                           pygame.display.flip()
                    main()




############################################
## 엔딩 화면 ##
def game_over():
    global points, CHAR1, CHAR2
    run = True
    GAMEOVER_MS.play()
    while run:
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        SCREEN.blit(GAME_OVER_BG, (0,0))
        score = font.render("Your Score: " + str(points), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
        SCREEN.blit(score, scoreRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                start1()

## 클리어 화면 ##
def game_clear():
    global points, CHAR1, CHAR2
    run = True
    while run:
        GAMEOVER_MS.play()
        SCREEN.blit(GAME_CLEAR_BG, (0,0))
        font = pygame.font.Font('freesansbold.ttf', 30)
        score = font.render("Your Score: " + str(points), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
        SCREEN.blit(score, scoreRect)

        # 캐릭터 이미지 출력
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                start1()

## 설명 화면4 ##
def game_explain3():
    global points, CHAR1, CHAR2
    run = True
    while run:
        # 캐릭터 이미지 출력
        SCREEN.blit(EXPLAIN_BG4, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                GAME_START_MS.stop()
                character_selection()
## 설명 화면3 ##
def game_explain2():
    global points, CHAR1, CHAR2
    run = True
    while run:
        # 캐릭터 이미지 출력
        SCREEN.blit(EXPLAIN_BG3, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                #GAME_START_MS.stop()
                game_explain3()
## 설명 화면2 ##
def game_explain1():
    global points, CHAR1, CHAR2
    run = True
    while run:
        # 캐릭터 이미지 출력
        SCREEN.blit(EXPLAIN_BG2, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                #GAME_START_MS.stop()
                game_explain2()
## 설명 화면1 ##
def game_explain():
    global points, CHAR1, CHAR2
    run = True
    while run:
        # 캐릭터 이미지 출력
        SCREEN.blit(EXPLAIN_BG1, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                #GAME_START_MS.stop()
                game_explain1()


def start2():
    global points, CHAR1, CHAR2
    run = True
    while run:
        #GAME_START_MS.play()
        SCREEN.blit(GAME_START_BG2, (0,0))
        #font = pygame.font.SysFont('malgungothic', 15)
        # 캐릭터 이미지 출력
        #SCREEN.blit(CHAR1, (300, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                game_explain()
## 시작 화면 ##
def start1():
    global points, CHAR1, CHAR2
    run = True
    GAMEOVER_MS.stop()
    while run:
        GAME_START_MS.play()
        SCREEN.blit(GAME_START_BG1, (0,0))
        #font = pygame.font.SysFont('malgungothic', 15)
        # 캐릭터 이미지 출력
        #SCREEN.blit(CHAR1, (300, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                start2()

# 시작 #
start1()