import construct.GameObject as GameObject
import Graphics.BaseObj
import pygame
import Mech

def main ():
    screen = pygame.display.set_mode((800, 600))
    BrickBlock = GameObject.AnimatedObject(3, 100, 100, 50, 50)
    BrickBlock1 = GameObject.AnimatedObject(3, 50, 490, 50, 50)
    bg = GameObject.Static_BG(3, 0, 0, 800, 600)
    bg.LoadImage('res/bg/ccc.jpg')
    bgG = Graphics.BaseObj.UniteSprite (bg)
    bgGMove = Mech.Mech.ScrollingSimple([640, 100], [100, 480], 3, [BrickBlock, BrickBlock1], [bgG])
    pygame.init()
    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 50)
    FPS = pygame.time.Clock()
    isWorking=True

    while (isWorking):
        FPS.tick(60)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False
            #if event.type == MoveFigure_down:
                #bgGMove.move_down()
        poses = bgGMove.scroll()
        if key[pygame.K_RIGHT]:

            if poses[3] == False:
                BrickBlock.move_right()

        if key[pygame.K_LEFT]:
            if poses[2] == False:
                BrickBlock.move_left()

        if key[pygame.K_UP]:
            if poses[1] == False:
                BrickBlock.move_up()

        if key[pygame.K_DOWN]:
            if poses[0] == False:
                BrickBlock.move_down()

        screen.fill(pygame.Color('#000000'))

        bgG.draw(screen)
        BrickBlock.draw(screen)
        BrickBlock1.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()