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

        # 키보드 입력 처리
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 키에서 손을 뗐을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

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
    screen.fill((0, 0, 255)) # 단색으로 배경 채우기 (파란색)

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    # 10. 게임 화면 다시 그리기 (필수!)
    pygame.display.update()

# 파이게임 종료
pygame.quit()