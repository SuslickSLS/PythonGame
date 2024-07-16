import pygame

class Player():

    def __init__(self,playerSpeed,playerX,playerY,playerAnimCount, walkLeft, walkRight, walkUp, walkDown):
        self._playerSpeed = playerSpeed
        self._playerX = playerX
        self._playerY = playerY
        self._playerAnimCount = playerAnimCount
        self._walkLeft = walkLeft
        self._walkRight = walkRight
        self._walkUp = walkUp
        self._walkDown = walkDown
        self._isWalking = True
        self._playerRect = pygame.transform.scale(self._walkLeft[self._playerAnimCount], (self._walkLeft[self._playerAnimCount].get_width() / 5, self._walkLeft[self._playerAnimCount].get_height() / 5)).get_rect(topleft=(self._playerX, self._playerY))

    @property
    def getPlayerX(self): return self._playerX
    @property
    def getPlayerY(self): return self._playerY

    @getPlayerX.setter
    def setPlayerX(self, newX):
        self._playerX = newX

    @getPlayerX.setter
    def setPlayerY(self, newY):
        self._playerY = newY

    def getPlayerRect(self):
        return self._playerRect

    def playerController(self, player,key):
        if key[pygame.K_a]:
            self._playerX -= self._playerSpeed
            player = pygame.transform.scale(self._walkLeft[self._playerAnimCount], (
                self._walkLeft[self._playerAnimCount].get_width() / 3,
                self._walkLeft[self._playerAnimCount].get_height() / 3))
        elif key[pygame.K_d]:
            self._playerX += self._playerSpeed
            player = pygame.transform.scale(self._walkRight[self._playerAnimCount], (
                self._walkRight[self._playerAnimCount].get_width() / 3,
                self._walkRight[self._playerAnimCount].get_height() / 3))
        elif key[pygame.K_w]:
            self._playerY -= self._playerSpeed
            player = pygame.transform.scale(self._walkUp[self._playerAnimCount], (
                self._walkUp[self._playerAnimCount].get_width() / 3,
                self._walkUp[self._playerAnimCount].get_height() / 3))
        elif key[pygame.K_s]:
            self._playerY += self._playerSpeed
            player = pygame.transform.scale(self._walkDown[self._playerAnimCount], (
                self._walkDown[self._playerAnimCount].get_width() / 3,
                self._walkDown[self._playerAnimCount].get_height() / 3))
        return player

    def updateAnim(self):
        self._playerAnimCount += 1

        if self._playerAnimCount == 4:
            self._playerAnimCount = 0



    def drawPlayer(self, surf, player):
        surf.blit(player, (self._playerX, self._playerY))
        self._playerRect = pygame.transform.scale(self._walkLeft[self._playerAnimCount], (self._walkLeft[self._playerAnimCount].get_width() / 3, self._walkLeft[self._playerAnimCount].get_height() / 3)).get_rect(topleft=(self._playerX, self._playerY))



