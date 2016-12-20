# coding=utf-8

import construct.GameObject as GameObject
import Graphics.BaseObj
import pygame
import Mech

def main ():
    screen = pygame.display.set_mode((800, 600))
    BrickBlock = GameObject.AnimatedObject(10, 100, 100, 50, 50)

    BrickBlock1 = GameObject.AnimatedObject(3, 100, 200, 50, 50, color="#ccff00")

    #rect_vis = GameObject.AnimatedObject(3, 50, 50, 640, 480, color="#000000")
    bg = GameObject.Static_BG(3, 0, 0, 800, 600)
    bg.LoadImage('res/bg/ccc.jpg')
    bgG = Graphics.BaseObj.UniteSprite (bg, BrickBlock1)
    bgGMove = Mech.Mech.ScrollingSimple(pygame.Rect(50,50, 640, 480), bg, BrickBlock, [bgG], screensize=screen.get_size())
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
            bgGMove.scroll_left()


        if key[pygame.K_RIGHT]:
            bgGMove.scroll_right()


        if key[pygame.K_UP]:
            bgGMove.scroll_up()


        if key[pygame.K_DOWN]:
            bgGMove.scroll_down()

        screen.fill(pygame.Color('#000000'))

        bgG.draw(screen)
        #rect_vis.draw(screen)
        BrickBlock.draw(screen)
        BrickBlock1.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()