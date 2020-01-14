''' Python / Pygame test '''
import pygame
pygame.init()

DIMENSIONS = (800, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SEMI_GREY = (192, 192, 192, 192)

CLOCK = pygame.time.Clock()

GAME_DISPLAY = pygame.display.set_mode(DIMENSIONS, 0, 32)
pygame.display.set_caption('edit the code to draw things')

def main():
    ''' what the fuck '''
    drawIt()

def drawIt():
    image = pygame.Surface((32,32), pygame.SRCALPHA, 32)
    pygame.draw.rect(image, WHITE, [2, 2, 28, 28])
    pygame.draw.rect(image, SEMI_GREY, [2, 2, 28, 28], 2)
    image = image.convert_alpha()

    pygame.image.save(image, "image.png")

if __name__ == "__main__":
    main()

pygame.quit()
quit()
