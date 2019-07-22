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
pygame.display.set_caption('A bit Racey')


CAR_IMG = pygame.image.load('racecar.png')

def main():
    ''' what the fuck '''
    co_x = (DISPLAY_WIDTH * 0.45)
    co_y = (DISPLAY_HEIGHT * 0.8)

    the_loop(co_x, co_y)

def car(co_x, co_y):
    ''' place the car on-screen '''
    GAME_DISPLAY.blit(CAR_IMG, (co_x, co_y))


def the_loop(co_x, co_y):
    ''' loops until exit '''
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        GAME_DISPLAY.fill(RED)
        car(co_x, co_y)
        pygame.display.update()
        CLOCK.tick(60)

# main()

#pygame.quit()
#quit()

if __name__ == "__main__":
    main()
