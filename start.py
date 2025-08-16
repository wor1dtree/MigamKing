import pygame

# 1. 파이게임 초기화
pygame.init()

# 2. 화면 크기 설정
screen_width = 800  # 가로 크기
screen_height = 600 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 3. 화면 타이틀 설정
pygame.display.set_caption("캐릭터 만들기")

# 4. 배경 이미지 불러오기 (선택 사항)
# background = pygame.image.load("background.png") # 배경 이미지가 있다면 추가

# 5. 캐릭터(스프라이트) 불러오기
character = pygame.image.load("./character/character.png") # 캐릭터 이미지 파일명
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 중앙
character_y_pos = screen_height - character_height             # 화면 세로의 가장 아래

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.5

# 6. 게임 루프
running = True 
while running:
    # 7. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. 눌려있는 키 확인하여 움직임 처리
    keys = pygame.key.get_pressed() # 모든 키의 상태를 리스트로 받아옴

    to_x = 0 # 매번 0으로 초기화

    if keys[pygame.K_LEFT]: # 왼쪽 키가 '눌려 있다면'
        to_x -= character_speed
    if keys[pygame.K_RIGHT]: # 오른쪽 키가 '눌려 있다면'
        to_x += character_speed

    # 8. 캐릭터 위치 정의
    character_x_pos += to_x
    character_y_pos += to_y

    # 경계값 처리 (캐릭터가 화면 밖으로 나가지 않도록)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 9. 화면에 그리기
    # screen.blit(background, (0, 0)) # 배경 그리기 (배경 이미지가 있다면)
    screen.fill((0, 0, 0)) # 단색으로 배경 채우기 (파란색)

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    # 10. 게임 화면 다시 그리기 (필수!)
    pygame.display.update()

# 파이게임 종료
pygame.quit()