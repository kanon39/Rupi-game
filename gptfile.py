import pygame
import random
import sys

# 초기화
pygame.init()

# 게임 창 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("다이노 코인 먹기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# 다이노 설정
dino_size = 50
dino_x = 50
dino_y = screen_height - dino_size - 50
dino_speed = 5

# 코인 설정
coin_size = 30
coin_speed = 5
coin_list = []

# 폰트 설정
font = pygame.font.SysFont(None, 55)

# 코인 생성 함수
def create_coin():
    coin_x = screen_width
    coin_y = random.randint(50, screen_height - coin_size - 50)
    coin_list.append([coin_x, coin_y])

# 게임 루프
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 다이노 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        dino_y -= dino_speed
    if dino_y > screen_height - dino_size - 50:
        dino_y = screen_height - dino_size - 50

    # 코인 생성 및 이동
    create_coin()
    for coin in coin_list:
        coin[0] -= coin_speed

    # 코인과 다이노 충돌 확인
    for coin in coin_list:
        if (
            dino_x < coin[0] + coin_size
            and dino_x + dino_size > coin[0]
            and dino_y < coin[1] + coin_size
            and dino_y + dino_size > coin[1]
        ):
            coin_list.remove(coin)
            score += 1

    # 화면 초기화
    screen.fill(black)

    # 다이노 그리기
    pygame.draw.rect(screen, white, [dino_x, dino_y, dino_size, dino_size])

    # 코인 그리기
    for coin in coin_list:
        pygame.draw.rect(screen, yellow, [coin[0], coin[1], coin_size, coin_size])

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [10, 10])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 제어
    clock.tick(30)