''' Python / Pygame test '''
import pygame
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CLOCK = pygame.time.Clock()

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A JS to Py conversion')

grid = {0, 0, 0, 0}

def main():
    ''' what the fuck '''
    the_loop()


def the_loop():
    ''' loops until exit '''
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        GAME_DISPLAY.fill(WHITE)

        pygame.draw.rect(GAME_DISPLAY, BLACK, [10, 10, 10, 10], 2)

        pygame.display.update()

        CLOCK.tick(60)

# main()

if __name__ == "__main__":
    main()

pygame.quit()
quit()
