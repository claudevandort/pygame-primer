import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
player = Player()

'''
Game Loop
* Processes user input
* Update state of game objects
* Updates display and audio output
* Maintains the speed of the game
'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

pygame.quit()
