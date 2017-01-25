# coding=utf-8

import construct.GameObject as GameObject
import construct.LvlBuild as LvlBuild
import Graphics.BaseObj
import pygame
import Mech

def main ():
    screen = pygame.display.set_mode((800, 600))
    Tank = GameObject.Player(10, 100, 100, 50, 50)
    Tank.LoadImage('res\sprite\up.png')
    bg = GameObject.Static_BG(0, 0, 800, 600)
    bg.LoadImage('res/bg/ccc.jpg')
    playerG = Graphics.BaseObj.UniteSprite(Tank)
    block = GameObject.Block(0, 200, 200, 50, 50)
    block.health = 100
    blockG = Graphics.BaseObj.UniteSprite(block)
    tile_lvl = LvlBuild.JustDoMyTileDict('res/lvl/lvl1.gen', 'res/lvl/lvl_conf.gen').Build_lvl('tiles', 'prepare',
                                                                                               'tile_size')

    bgG = Graphics.BaseObj.UniteSprite (bg)
    bgGMove = Mech.Mech.ScrollingSimple(pygame.Rect(50,50, 640, 480), bg, Tank, [bgG, blockG, tile_lvl], screensize=screen.get_size())
    pygame.init()
    FPS = pygame.time.Clock()
    isWorking=True


    while (isWorking):
        FPS.tick(60)

        #
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False

        if key[pygame.K_LEFT]:
            Tank.set_direction(True, False, False, False)
            bgGMove.scroll_left()

        if key[pygame.K_RIGHT]:

            Tank.set_direction(False, True, False, False)
            bgGMove.scroll_right()

        if key[pygame.K_UP]:

            Tank.set_direction(False, False, True, False)
            bgGMove.scroll_up()

        if key[pygame.K_DOWN]:

            Tank.set_direction(False, False, False, True)
            bgGMove.scroll_down()

        screen.fill(pygame.Color('#FFFFFF'))
        bgG.draw(screen)
        tile_lvl.draw(screen)
        playerG.draw(screen)
        blockG.draw(screen)


        pygame.display.flip()

if __name__ == '__main__':
    main()