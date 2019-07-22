''' basic code using Pygame Zero instead of PyGame'''
import pgzrun
WIDTH = HEIGHT = 600
def draw():
    ''' draw screen contents '''
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')
pgzrun.go()
