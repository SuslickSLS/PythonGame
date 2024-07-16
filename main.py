import menu
import player
import sceneManager
import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1500,900))
pygame.display.set_caption("TestGame")

# Для анимации ходьбы
walkLeft = [
    pygame.image.load(".venv/Images/Player/Left/1.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Left/2.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Left/3.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Left/4.png").convert_alpha(),
]

walkRight = [
    pygame.image.load(".venv/Images/Player/Right/1.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Right/2.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Right/3.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Right/4.png").convert_alpha(),
]

walkUp = [
    pygame.image.load(".venv/Images/Player/Up/1.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Up/2.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Up/3.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Up/4.png").convert_alpha(),
]

walkDown = [
    pygame.image.load(".venv/Images/Player/Down/1.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Down/2.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Down/3.png").convert_alpha(),
    pygame.image.load(".venv/Images/Player/Down/4.png").convert_alpha(),
]

player = player.Player(10,600,600,0, walkLeft, walkRight, walkUp, walkDown)

playerImg = pygame.transform.scale(walkDown[0],(walkDown[0].get_width() / 3, walkDown[0].get_height() / 3))
#________________________________________________

#Меню выбора этажа
currentNumberFloor = 1
bgMenu = pygame.Surface((600,400))

def menuFloorDraw():
    global menuFloor
    bgMenu.fill('white')
    screen.blit(bgMenu,(350,350))
    menuFloor.draw(screen,550,380,50)

def selectFloor(numberFloor):
    global currentNumberFloor
    currentNumberFloor = numberFloor

def switchFloor():
    global currentNumberFloor
    print(currentNumberFloor)
    if currentNumberFloor == 1:
        scene.set_current_option_index(1)
        player.setPlayerX = 320
        player.setPlayerY = 320
    else:
        scene.set_current_option_index(2)
        player.setPlayerX = 1150
        player.setPlayerY = 770
    pass

menuFloor = menu.Menu()
menuFloor.append_option("Этаж 1", lambda : selectFloor(1))
menuFloor.append_option("Этаж 2", lambda : selectFloor(2))
menuFloor.append_option("Этаж 3", lambda : selectFloor(3))
menuFloor.append_option("Этаж 4", lambda : selectFloor(4))
menuFloor.append_option("Этаж 5", lambda : selectFloor(5))
menuFloor.append_option("Этаж 6", lambda : selectFloor(6))
menuFloor.append_option("Этаж 7", lambda : selectFloor(7))
#________________________________________________

#Сцены

square = pygame.Surface((20,20))
square.fill('red')
elevator = pygame.image.load(".venv/Images/Lift.png").convert_alpha()

#Стены
wallsScene1 = []
wall1 = pygame.Surface((250,267))
wall1.fill('black')
wall2 = pygame.Surface((1500,200));
wall2.fill('black')
wall3 = pygame.Surface((70,90));
wall3.fill('black')
wall4 = pygame.Surface((105,65));
wall4.fill('black')
wall5 = pygame.Surface((56,56));
wall5.fill('black')
wall6 = pygame.Surface((56,56));
wall6.fill('black')
wall7 = pygame.Surface((13,337));
wall7.fill('black')
wall8 = pygame.Surface((334,132));
wall8.fill('black')
wall9 = pygame.Surface((59,58));
wall9.fill('black')
wall10 = pygame.Surface((91,91));
wall10.fill('black')
wall11 = pygame.Surface((91,56));
wall11.fill('black')

wall12 = pygame.Surface((1042, 287))
wall12.fill('black')
wall13 = pygame.Surface((1500, 232));
wall13.fill('black')

def Scene4():
    pass
def Scene3():
    global playerImg

    wallsScene1 = []

    wallRect1 = wall12.get_rect(topleft=(0, 0))
    wallRect2 = wall13.get_rect(topleft=(0, 616))

    wallsScene1.append(wallRect1)
    wallsScene1.append(wallRect2)

    floor = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 50).render("%d Floor" % currentNumberFloor, True, 'black')

    numberCabinet1 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 70), True, 'black')
    numberCabinet2 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 69), True, 'black')
    numberCabinet3 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 68), True, 'black')
    numberCabinet4 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 67), True, 'black')
    numberCabinet5 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 66), True, 'black')
    numberCabinet6 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 65), True, 'black')
    numberCabinet7 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 64), True, 'black')
    numberCabinet8 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 63), True, 'black')
    numberCabinet9 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 62), True, 'black')
    numberCabinet10 = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 20).render("Кабинет: %d" % (currentNumberFloor * 100 + 60), True, 'black')

    isWalking = True
    player.updateAnim()

    key = pygame.key.get_pressed()


    if isWalking:
        playerImg = player.playerController(playerImg, key)

    isMenuOpen = False

    background = pygame.image.load(".venv/Images/ScenesImg/Scene3.png").convert_alpha()
    screen.blit(background, (0, 0))
    screen.blit(square, (1070, 800))
    squareRect = square.get_rect(topleft=(1070, 800))
    pygame.draw.rect(screen, 'black', player.getPlayerRect())

    player.drawPlayer(screen, playerImg)

    #Номера кабинетов
    screen.blit(numberCabinet1,(30,200))
    screen.blit(numberCabinet3,(260,200))
    screen.blit(numberCabinet5,(547,200))
    screen.blit(numberCabinet7,(828,200))
    screen.blit(numberCabinet9,(1079,200))
    screen.blit(numberCabinet10,(1346,200))

    screen.blit(numberCabinet2,(30,640))
    screen.blit(numberCabinet4,(270,640))
    screen.blit(numberCabinet6,(550,640))
    screen.blit(numberCabinet8,(830,640))

    screen.blit(floor, (100, 100))

    if squareRect.colliderect(player.getPlayerRect()):
        menuFloorDraw()
        isMenuOpen = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menuFloor.switch(-1)
            if event.key == pygame.K_DOWN:
                menuFloor.switch(1)
            if event.key == pygame.K_SPACE and isMenuOpen:
                menuFloor.select()
                switchFloor()

    pass
def Scene2():
    global playerImg

    #Стены
    isWalking = True
    proverka = player.getPlayerRect()
    wallRect1 = wall1.get_rect(topleft=(0,0))
    wallRect2 = wall2.get_rect(topleft=(0,780))
    wallRect3 = wall3.get_rect(topleft=(495,730))
    wallRect4 = wall4.get_rect(topleft=(890,730))
    wallRect5 = wall5.get_rect(topleft=(506,254))
    wallRect6 = wall6.get_rect(topleft=(931,254))
    wallRect7 = wall7.get_rect(topleft=(560,0))
    wallRect8 = wall7.get_rect(topleft=(920,0))
    wallRect9 = wall8.get_rect(topleft=(1166,0))
    wallRect10 = wall9.get_rect(topleft=(1228,132))
    wallRect11 = wall10.get_rect(topleft=(1157,275))
    wallRect12 = wall11.get_rect(topleft=(1409,277))

    wallsScene1.append(wallRect1)
    wallsScene1.append(wallRect2)
    wallsScene1.append(wallRect3)
    wallsScene1.append(wallRect4)
    wallsScene1.append(wallRect5)
    wallsScene1.append(wallRect6)
    wallsScene1.append(wallRect7)
    wallsScene1.append(wallRect8)
    wallsScene1.append(wallRect9)
    wallsScene1.append(wallRect10)
    wallsScene1.append(wallRect11)
    wallsScene1.append(wallRect12)

    player.updateAnim()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        proverka = playerImg.get_rect(topleft=(player.getPlayerX - 10,player.getPlayerY))
    elif key[pygame.K_d]:
        proverka = playerImg.get_rect(topleft=(player.getPlayerX + 10,player.getPlayerY))
    elif key[pygame.K_w]:
        proverka = playerImg.get_rect(topleft=(player.getPlayerX,player.getPlayerY - 10))
    elif key[pygame.K_s]:
        proverka = playerImg.get_rect(topleft=(player.getPlayerX, player.getPlayerY + 10))

    for wallRect in wallsScene1:
        if proverka.colliderect(wallRect) == False:
            isWalking = True
        else:
            isWalking = False
            break

    if isWalking:
        playerImg = player.playerController(playerImg, key)

    isMenuOpen = False

    background = pygame.image.load(".venv/Images/ScenesImg/Hall.png").convert_alpha()
    screen.blit(background,(0,0))
    screen.blit(square, (300,300))
    squareRect = square.get_rect(topleft=(300,300))
    pygame.draw.rect(screen,'black', player.getPlayerRect())

    player.drawPlayer(screen,playerImg)

    if squareRect.colliderect(player.getPlayerRect()):
        menuFloorDraw()
        isMenuOpen = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menuFloor.switch(-1)
            if event.key == pygame.K_DOWN:
                menuFloor.switch(1)
            if event.key == pygame.K_SPACE and isMenuOpen:
                menuFloor.select()
                switchFloor()

def Scene1():
    GameName = pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 120).render("Опять опоздал", True, 'black')
    background = pygame.image.load(".venv/Images/YRGY.jpg").convert_alpha()
    background = pygame.transform.scale(background, (1500, 600))

    screen.fill('white')
    screen.blit(background, (0, 200))
    screen.blit(GameName, (150, 20))

    menuGame.draw(screen, 150, 150, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                menuGame.switch(-1)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                menuGame.switch(1)
            if event.key == pygame.K_SPACE:
                menuGame.select()

scene = sceneManager.SceneManager();
scene.append_option("1", Scene1)
scene.append_option("2", Scene2)
scene.append_option("3", Scene3)
#________________________________________________

#Начальное меню
def startGame():
    scene.set_current_option_index(1)

menuGame = menu.Menu()
menuGame.append_option("Старт", startGame)
menuGame.append_option('Выход', quit)
#________________________________________________


running = True
while running:
    clock.tick(10)

    scene.draw()

    if scene.get_isSwitch():
        scene.select()

    pygame.display.update()



