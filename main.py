# coding=utf-8
import construct.GameObject as GameObject
import construct.LvlBuild as LvlBuild
import Graphics.BaseObj
import pygame
import Mech


def main():
    display_size = (800, 600)
    screen = pygame.display.set_mode(display_size)
    # Название игры
    pygame.display.set_caption('TankMan')
    # Указываем размер сцены
    bg = GameObject.Static_BG(0, 0, 2683, 1059)
    # Инициализация игрока
    Tank = GameObject.Player(50, 50, 50, 50)
    Tank.LoadImage('res\sprite\up.png')
    playerG = Graphics.BaseObj.UniteSprite(Tank)
    tile_lvl = LvlBuild.JustDoMyTileLevel('res/lvl/lvl1.gen', 'res/lvl/lvl_conf.gen').Build_lvl('tiles', 'prepare',
                                                                                               'tile_size')
    spritesG = LvlBuild.JustPlaceMySpritesOnLevel('res/lvl/lvl_conf.gen', 'sprites', 'prepare').PlaceSptites('res/lvl/lvl1_sprt.gen',
                                                                                            'Static',
                                                                                            GameObject.Block)
    scrolling = Mech.Mech.ScrollingSimple(Tank, pygame.Rect(50, 50, 640, 480), bg, screen, [tile_lvl, spritesG])
    pygame.init()
    FPS = pygame.time.Clock()
    isWorking=True
    speedXL, speedXR, speedYU, speedYD = -10, 10, -10, 10
    previousmove = (0,0)

    bulletz = GameObject.BulletGroup()

    while (isWorking):
        FPS.tick(60)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False

        if key[pygame.K_LEFT]:
            dxdy = Tank.move(speedXL, 0)
            Mech.Mech.Collides.collide_walls(dxdy, playerG, spritesG, False, False)
            scrolling.scroll_left(dxdy)
            previousmove = (dxdy)

        if key[pygame.K_RIGHT]:
            dxdy = Tank.move(speedXR, 0)
            Mech.Mech.Collides.collide_walls(dxdy, playerG, spritesG, False, False)
            scrolling.scroll_right(dxdy)
            previousmove = (dxdy)

        if key[pygame.K_UP]:
            dxdy = Tank.move(0, speedYU)
            Mech.Mech.Collides.collide_walls(dxdy, playerG, spritesG, False, False)
            scrolling.scroll_up(dxdy)
            previousmove = (dxdy)

        if key[pygame.K_DOWN]:
            dxdy = Tank.move(0, speedYD)
            Mech.Mech.Collides.collide_walls(dxdy, playerG, spritesG, False, False)
            scrolling.scroll_down(dxdy)
            previousmove = (dxdy)

        if key[pygame.K_SPACE]:
            b = GameObject.Bullet(Tank, 5, 5)
            b.set_direction_and_speed(previousmove[0], previousmove[1],2)
            bulletz.add(b)
            # Выстрел лазера необходимо перпеписать ввиду размеров видимого экрана
            #laser = GameObject.LaserShooting(Tank)
            #laser.shoot(previousmove, (2, 800))
            #print pygame.sprite.groupcollide(Graphics.BaseObj.UniteSprite(laser), spritesG, False, False)
            #laser.draw(screen)

        tile_lvl.draw(screen)
        spritesG.draw(screen)
        playerG.draw(screen)
        bulletz.deleteBullet(display_size[0], display_size[1], spritesG)
        bulletz.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()