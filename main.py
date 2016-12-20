# coding=utf-8

import construct.GameObject as GameObject
import Graphics.BaseObj
import pygame
import Mech

def main ():
    screen = pygame.display.set_mode((800, 600))
    Tank = GameObject.Player(10, 100, 100, 50, 50)
    Tank.LoadImage('res\sprite\up.png')
    tankDict = {'up': [pygame.image.load ('res\sprite\up.png'), pygame.image.load ('res\sprite\up_anim1.png'), pygame.image.load ('res\sprite\up_anim2.png')],
                'down': [pygame.image.load ('res\sprite\down.png'), pygame.image.load ('res\sprite\down_anim1.png'), pygame.image.load ('res\sprite\down_anim2.png')],
                'left': [pygame.image.load ('res\sprite\left.png'), pygame.image.load ('res\sprite\left_anim1.png'), pygame.image.load ('res\sprite\left_anim2.png')],
                'right':[pygame.image.load ('res\sprite\\right.png'), pygame.image.load ('res\sprite\\right_anim1.png'), pygame.image.load ('res\sprite\\right_anim2.png')]}
    Tank.set_animation_dict(tankDict)
    bg = GameObject.Static_BG(0, 0, 800, 600)
    bg.LoadImage('res/bg/ccc.jpg')
    bgG = Graphics.BaseObj.UniteSprite (bg)
    bgGMove = Mech.Mech.ScrollingSimple(pygame.Rect(50,50, 640, 480), bg, Tank, [bgG], screensize=screen.get_size())
    bgGMove.scrolluntil = pygame.Rect (0,0, 2683-800, 1059-600)

    bulletz = Graphics.BaseObj.UniteSprite ()

    pygame.init()
    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 10)

    MoveFigure_animate = pygame.USEREVENT + 2
    pygame.time.set_timer(MoveFigure_animate, 100)

    FPS = pygame.time.Clock()
    isWorking=True
    while (isWorking):
        FPS.tick(60)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False
            if event.type == MoveFigure_animate:
                Tank.animate()
            if event.type == MoveFigure_down:
                for bullet in bulletz:
                    if bullet.isExsist is False:
                        bulletz.remove(bullet)
                    else:
                        if (True, False, False, False)==  bullet.bulletDirection:
                            bullet.shoot_left()
                        elif (False, True, False, False) == bullet.bulletDirection:
                            bullet.shoot_right()
                        elif (False, False, True, False) == bullet.bulletDirection:
                            bullet.shoot_up()
                        elif (False, False, False, True) == bullet.bulletDirection:
                            bullet.shoot_down()



        if key [pygame.K_SPACE]:
            bullet = GameObject.Bullet(Tank, 2, 40, 20, 5, 5, color='#FF00FF')
            bullet.range = 200
            bullet.set_direction()
            bulletz.add(bullet)

        if key[pygame.K_LEFT]:
            Tank.set_animation_dict_to_list('left')
            Tank.set_direction(True, False, False, False)
            bgGMove.scroll_left()

        if key[pygame.K_RIGHT]:
            Tank.set_animation_dict_to_list('right')
            Tank.set_direction(False, True, False, False)
            bgGMove.scroll_right()

        if key[pygame.K_UP]:
            Tank.set_animation_dict_to_list('up')
            Tank.set_direction(False, False, True, False)
            bgGMove.scroll_up()

        if key[pygame.K_DOWN]:
            Tank.set_animation_dict_to_list('down')
            Tank.set_direction(False, False, False, True)
            bgGMove.scroll_down()

        screen.fill(pygame.Color('#000000'))
        bgG.draw(screen)
        Tank.draw(screen)
        bulletz.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()