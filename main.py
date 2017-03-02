# coding=utf-8
import construct.GameObject as GameObject
import construct.LvlBuild as LvlBuild
import Graphics.BaseObj
import pygame
import Mech
import TextsAndFonts.Text as TBaloon
import Parcer

def main():
    display_size = (800, 600)
    screen = pygame.display.set_mode(display_size)
    # Название игры
    pygame.display.set_caption('TankMan')
    # Указываем размер сцены
    bg = GameObject.Static_BG(0, 0, 2683, 1059)
    # Инициализация игрока
    Tank = GameObject.Player(100, 100, 40, 40)
    Tank.LoadImage('res\sprite\up.png')
    surf = pygame.transform.scale(Tank.image, (38,38))
    Tank.setSurface(surf)
    playerG = Graphics.BaseObj.UniteSprite(Tank)

    # Враг
    Enemy = GameObject.Enemy(50, 189, 50, 50, color='#000000')
    Enemy.LoadImage('res\sprite\left.png')
    surf = pygame.transform.scale(Enemy.image, (45, 45))
    Enemy.setSurface(surf)
    EnemyG = Graphics.BaseObj.UniteSprite(Enemy)


    tile_lvl = LvlBuild.JustDoMyTileLevel('res/lvl/lvl1.gen', 'res/lvl/lvl_conf.gen').Build_lvl('tiles', 'prepare',
                                                                                               'tile_size')
    spritesG = LvlBuild.JustPlaceMySpritesOnLevel('res/lvl/lvl_conf.gen', 'sprites', 'prepare').PlaceSptites('res/lvl/lvl1_sprt.gen',
                                                                                            'Static',
                                                                                            GameObject.Block)
    dialog_sprt = LvlBuild.JustPlaceMySpritesOnLevel('res/lvl/lvl_conf.gen', 'dialog', 'prepare').sprites

    bulletz = GameObject.BulletGroup()
    scrolling = Mech.Mech.ScrollingSimple(Tank, pygame.Rect(100, 100, 540, 380), bg, screen, [tile_lvl, spritesG, bulletz])
    pygame.init()
    FPS = pygame.time.Clock()
    isWorking=True
    speedXL, speedXR, speedYU, speedYD = -10, 10, -10, 10
    previousmove = (0,0)

    Scenario_Text = Parcer.TextParce.SimpleParceText('res/Text/ScenarioFile')

    DialogTextBox = TBaloon.RPGLikeTextDialog('res/Fonts/Pixelplay.ttf', 30, (790, 200))
    DialogTextBox.set_border_sprites(dialog_sprt['d2'], dialog_sprt['d1'], dialog_sprt['d3'])
    DialogTextBox.setDialogpos(5, 400)
    DialogTextBox.setText(Scenario_Text.get_dialog('1'), '#00FF00')
    # инициализация текста
    pygame.font.init()

    #TT = TBaloon.TextConstructOnOnePage('res/Fonts/Pixelplay.ttf', 30)
    #Scenario_Text.get_dialog('0')
    #TT.set_text(Scenario_Text.get_dialog('1'), color='#00FF00')

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
            #TT.set_text(Scenario_Text.dictShow['2'], color='#FF00FF')
            # Выстрел лазера необходимо перпеписать ввиду размеров видимого экрана
            laser = GameObject.LaserShooting(Tank)
            laser.shoot(previousmove, (2, 800))
            laser.draw(screen)


        tile_lvl.draw(screen)
        spritesG.draw(screen)
        playerG.draw(screen)
        #EnemyG.draw(screen)



        bulletz.deleteBullet(display_size[0], display_size[1], spritesG)
        bulletz.draw(screen)

        #TT.draw(screen, (40, 400), 750)
        #DialogTextBox.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()