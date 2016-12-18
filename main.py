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
    bgGMove = Mech.Mech.ScrollingSimple([10, 750], [10, 550], 3, [BrickBlock], [bgG])
    bgGMove.scrolluntil = pygame.Rect (0,0, 2683-800, 1059-600)

    pygame.init()
    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 200)
    FPS = pygame.time.Clock()
    isWorking=True

    while (isWorking):
        FPS.tick(60)
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False
            if event.type == MoveFigure_down:
                pass

        if key[pygame.K_LEFT]:
            isStop = bgGMove.move_left()
            if isStop is False:
                BrickBlock.move_left()
            else:
                bgGMove.scroll('left')

        if key[pygame.K_RIGHT]:
            isStop = bgGMove.move_right()
            if isStop is False:
                BrickBlock.move_right()
            else:
                bgGMove.scroll('right')

        if key[pygame.K_UP]:
            isStop = bgGMove.move_up()
            if isStop is False:
                BrickBlock.move_up()
            else:
                bgGMove.scroll('up')

        if key[pygame.K_DOWN]:
            isStop = bgGMove.move_down()
            if isStop is False:
                BrickBlock.move_down()
            else:
                bgGMove.scroll('down')
        screen.fill(pygame.Color('#000000'))

        bgG.draw(screen)
        BrickBlock.draw(screen)

        pygame.display.flip()



if __name__ == '__main__':
    main()