import pygame
import sys

pygame.init()

gauge_show = False

# --- 화면 설정 ---
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("캐릭터 만들기")

# --- 리소스 ---
character = pygame.image.load("./character/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# --- 캐릭터 상태 ---
character_x_pos = (screen_width / 2) - (character_width / 2)
ground_y = screen_height - character_height
character_y_pos = ground_y

to_x = 0
to_y = 0
character_speed = 5      # 프레임당 px (좌우이동용, 간단히 프레임 기준으로 둠)

# --- 점프/중력 ---
gravity = 0.6            # 프레임당 속도 증가(아래로)
is_jumping = False
velocity_y = 0.0

# --- 점프 게이지 ---
is_charging = False      # 스페이스를 누르고 있어 게이지를 모으는 중인지
charge = 0.0             # 0.0 ~ 1.0
charge_rate = 0.04       # 프레임당 게이지 증가량
min_jump_v = 8.0         # 최소 점프 초기 속도
max_jump_v = 18.0        # 최대 점프 초기 속도
auto_fire_when_full = True

# 살짝 웅크리기(게이지 모을 때) 연출
crouch_pixels = 8        # 최대 웅크리는 정도(아래로 살짝 내려감)

clock = pygame.time.Clock()
running = True

def start_jump_from_charge():
    """게이지를 점프로 변환하고 상태 리셋"""
    global is_charging, is_jumping, velocity_y, charge, character_y_pos
    # 게이지 비율로 초기 속도 보간
    jump_v = min_jump_v + (max_jump_v - min_jump_v) * charge
    is_jumping = True
    is_charging = False
    velocity_y = -jump_v
    charge = 0.0
    # 웅크리기 복원
    character_y_pos = min(character_y_pos, ground_y)
    
def gauge_jump():
    gauge_w = 200
    gauge_h = 14
    gauge_x = 20
    gauge_y = screen_height - 20 - gauge_h
    
    # 바탕(테두리)
    pygame.draw.rect(screen, (100, 100, 100), (gauge_x - 2, gauge_y - 2, gauge_w + 4, gauge_h + 4), width=2)
    # 충전량
    if is_charging:
        fill_w = int(gauge_w * charge)
        pygame.draw.rect(screen, (50, 180, 50), (gauge_x, gauge_y, fill_w, gauge_h))
    else:
        # 점프 중에는 페이드아웃된 빈 게이지
        pygame.draw.rect(screen, (40, 40, 40), (gauge_x, gauge_y, gauge_w, gauge_h))    

while running:
    dt = clock.tick(60)  # 60 FPS 고정
    # --- 이벤트 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 스페이스: 누르면 게이지 충전 시작(지상일 때만)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (not is_jumping) and (character_y_pos >= ground_y) and (not is_charging):
                is_charging = True
                charge = 0.0

        # 스페이스: 떼면 저장된 게이지 만큼 점프
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and is_charging:
                start_jump_from_charge()

    # Key Horver
    keys = pygame.key.get_pressed()
    to_x = 0
    if keys[pygame.K_LEFT]:
        to_x -= character_speed
    if keys[pygame.K_RIGHT]:
        to_x += character_speed
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # 점프 중이 아닐 때만 수동 상하 이동 허용 (원하면 삭제)
    if not is_jumping and not is_charging:
        if keys[pygame.K_UP]:
            to_y = -character_speed
        elif keys[pygame.K_DOWN]:
            to_y = character_speed
        else:
            to_y = 0
    else:
        to_y = 0

    # --- 위치 반영(좌우/임의 상하) ---
    character_x_pos += to_x
    character_y_pos += to_y

    # --- 게이지 충전 처리(웅크리기 연출 포함) ---
    if is_charging:
        # 게이지 증가
        charge = min(1.0, charge + charge_rate)
        # 웅크리기: 게이지에 비례해서 살짝 아래로
        crouch = int(crouch_pixels * charge)
        character_y_pos = ground_y + crouch

        # 가득 차면 자동 점프(선택)
        if auto_fire_when_full and charge >= 1.0:
            start_jump_from_charge()

    # --- 점프 물리 ---
    if is_jumping:
        character_y_pos += velocity_y
        velocity_y += gravity

        # 착지
        if character_y_pos >= ground_y:
            character_y_pos = ground_y
            is_jumping = False
            velocity_y = 0.0

    # --- 경계 처리 ---
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > ground_y:
        character_y_pos = ground_y
        is_jumping = False
        velocity_y = 0.0

    # --- 렌더링 ---
    screen.fill((0, 0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            print("gauge option change")
            if gauge_show == False:
                gauge_show = True
            else :
                gauge_show = False
         
    # 게이지 표시
    if gauge_show == True:
        gauge_jump()

    pygame.display.update()

pygame.quit()

