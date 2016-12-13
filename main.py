import construct.GameObject as GameObject
import Graphics.BaseObj
import pygame
import Mech

def main ():
    screen = pygame.display.set_mode((800, 600))
    BrickBlock = GameObject.AnimatedObject(3, 100, 100, 50, 50)
    bg = GameObject.Static_BG(3, 0, 0, 800, 600)
    bg.LoadImage('res/bg/ccc.jpg')
    bgG = Graphics.BaseObj.UniteSprite (bg)
    bgGMove = Mech.Mech.shoot_em_up_scroll(3, 0, bgG)
    pygame.init()
    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 350)
    FPS = pygame.time.Clock()
    isWorking=True
    while (isWorking):
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False
            if event.type == MoveFigure_down:
                bgGMove.move_left()



        screen.fill(pygame.Color('#000000'))
        bgG.draw(screen)
        BrickBlock.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()