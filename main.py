# coding=utf-8
import construct.GameObject as GameObject
import construct.LvlBuild as LvlBuild
import Graphics.BaseObj
import pygame
import Mech


def main():

    screen = pygame.display.set_mode((800, 600))
    #Название игры
    pygame.display.set_caption('TankMan')
    #Указываем размер сцены
    bg = GameObject.Static_BG(0, 0, 2683, 1059)
    #Инициализация игрока
    Tank = GameObject.Player(100, 100, 50, 50, MSpeedX=10, MSpeedY=10)
    Tank.LoadImage('res\sprite\up.png')
    playerG = Graphics.BaseObj.UniteSprite(Tank)

    tile_lvl = LvlBuild.JustDoMyTileLevel('res/lvl/lvl1.gen', 'res/lvl/lvl_conf.gen').Build_lvl('tiles', 'prepare',
                                                                                               'tile_size')
    spritesG = LvlBuild.JustPlaceMySpritesOnLevel('res/lvl/lvl_conf.gen', 'sprites', 'prepare').PlaceSptites('res/lvl/lvl1_sprt.gen',
                                                                                            'Static',
                                                                                            GameObject.Block, 2, 2)
    bgG = Graphics.BaseObj.UniteSprite(bg)
    bgGMove = Mech.Mech.ScrollingSimple(pygame.Rect(50,50, 640, 480), bg, Tank, [bgG, tile_lvl, spritesG], screensize=screen.get_size())
    pygame.init()
    FPS = pygame.time.Clock()
    isWorking=True
    while (isWorking):
        FPS.tick(60)
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
        GameObject.Collide_United(playerG, spritesG,False, False)
        tile_lvl.draw(screen)
        spritesG.draw(screen)
        playerG.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()