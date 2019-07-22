''' basic tile drawing '''
import pygame
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption('A few blocks')

grid = [0, 1, 3]

GAME_DISPLAY.fill(WHITE)


def drawSqr(co_x, co_y):
    pygame.draw.rect(GAME_DISPLAY, GREEN, [co_x * 100, 20, 10, 10], 10)
    pygame.draw.rect(GAME_DISPLAY, RED, [co_x * 100, 20, 10, 10], 0)

for x in grid:
    print(x)
    drawSqr(x, x)


pygame.display.update()

CLOCK = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        CLOCK.tick(60)

pygame.quit()
