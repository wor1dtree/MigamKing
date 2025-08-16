import pygame

# 1. 파이게임 초기화
pygame.init()

# 2. 화면 크기 설정
screen_width = 800  # 가로 크기
screen_height = 600 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 3. 화면 타이틀 설정
pygame.display.set_caption("캐릭터 만들기")

class Unit:
    def __init__(self, x, y, speed):
        """ 유닛 생성자: 위치, 속도, 이미지 등을 초기화합니다. """
        
        # --- 캐릭터 이미지 설정 ---
        # 오른쪽을 보는 원본 이미지
        self.image_right = pygame.image.load("./character/player.png") # 'character.png' 파일이 있어야 합니다.
        # 원본 이미지를 좌우 반전시켜 왼쪽을 보는 이미지 생성
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        
        # 처음에는 오른쪽을 보도록 설정
        self.image = self.image_right
        
        # --- 캐릭터 위치 및 크기 정보 ---
        self.rect = self.image.get_rect() # 이미지의 사각형 정보를 가져옴
        self.character_width = self.rect.size[0]
        self.character_height = self.rect.size[1]
        self.rect.topleft = (x, y-self.character_height)        # 사각형의 왼쪽 상단 좌표를 설정
        
        self.x = x
        self.y = y-self.character_height

        # --- 캐릭터 방향 및 속도 ---
        self.speed = speed
        self.facing_right = True # 현재 오른쪽을 보고 있는지 여부 (True: 오른쪽, False: 왼쪽)

    def move(self, keys):
        """ 키 입력에 따라 캐릭터의 위치를 업데이트하고 방향에 맞춰 이미지를 변경합니다. """
        
        dx = 0 # 수평 이동량
        
        if keys[pygame.K_LEFT]:
            dx -= self.speed
            # 왼쪽으로 이동 시, 현재 이미지가 왼쪽 보는 이미지가 아니라면 변경
            if self.facing_right:
                self.image = self.image_left
                self.facing_right = False
                
        if keys[pygame.K_RIGHT]:
            dx += self.speed
            # 오른쪽으로 이동 시, 현재 이미지가 오른쪽 보는 이미지가 아니라면 변경
            if not self.facing_right:
                self.image = self.image_right
                self.facing_right = True
        
        # 계산된 이동량만큼 캐릭터의 x 좌표 업데이트
        print(dx)
        self.x += dx
        print(self.rect.x)

        # 경계값 처리 (캐릭터가 화면 밖으로 나가지 않도록)
        if self.rect.x < 0:
            self.x = 0
        elif self.rect.x > screen_width - self.character_width:
            self.x = screen_width - self.character_width

    def draw(self, screen):
        """ 캐릭터를 화면에 그립니다. """
        screen.blit(self.image, (self.x, self.y))
    
player = Unit((screen_width / 2), screen_height, 0.3)

# 6. 게임 루프
running = True 
while running:
    # 7. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    # 2. 눌려있는 키 확인하여 움직임 처리
    keys = pygame.key.get_pressed() # 모든 키의 상태를 리스트로 받아옴

    player.move(keys)

    # 9. 화면에 그리기
    # screen.blit(background, (0, 0)) # 배경 그리기 (배경 이미지가 있다면)
    screen.fill((0, 0, 0)) # 단색으로 배경 채우기 (파란색)

    player.draw(screen)

    # 10. 게임 화면 다시 그리기 (필수!)
    pygame.display.update()

# 파이게임 종료
pygame.quit()