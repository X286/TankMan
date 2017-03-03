# coding=utf-8

import Graphics.BaseObj as Graphics # Вкорячиваем часть графики
import Mech.Mech as Mech #Вкорячиваем механику
import pygame


class Static_BG (Graphics.GraphicObject):
    def __init__(self, Gx, Gy, GW, GH, color='#ffff00'):
        Graphics.GraphicObject.__init__(self, Gx, Gy, GW, GH, color=color)


# Вызов Блока с движением (например какой то заградительный блок, например передвижной бетонный блок)
class Block (Graphics.StaticSprite, Mech.Movement):
    def __init__(self, Gx, Gy, GW, GH, color = '#00ff00', health=None):
        Graphics.StaticSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self)
        # -1 - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = health

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

# Анимированный объект, например колыхающие деревья
class AnimatedObject (Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, Gx, Gy, GW, GH, color='#00ffff', health= None):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self)
        # None - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = health

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

# Игрок класс
class Player(Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, Gx, Gy, GW, GH, color='#00ffff'):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self)
        self.hit_power = 50


class LaserShooting (Block):
    def __init__(self, playersprt):
        super(LaserShooting, self).__init__(10, 10, 800, 2, color='#FFFFFF')
        self.playser = playersprt
        self.damage = 100

    def set_damage(self, damage):
        self.damage = damage

    def shoot(self, dxdy, laserLeng):
        if dxdy[0] > 0:
            self.rect.left = self.playser.rect.centerx
            self.rect.y = self.playser.rect.centery

        if dxdy[0] < 0:
            self.rect.right = self.playser.rect.centerx
            self.rect.y = self.playser.rect.centery

        if dxdy[1] > 0:
            self.image = pygame.Surface(laserLeng)
            self.changeColor('#FFFFFF')
            self.rect = self.image.get_rect()
            self.rect.y = self.playser.rect.centery
            self.rect.x = self.playser.rect.centerx

        if dxdy[1] < 0:
            self.image = pygame.Surface(laserLeng)
            self.rect = self.image.get_rect()
            self.changeColor('#FFFFFF')
            self.rect.y = self.playser.rect.centery-800
            self.rect.x = self.playser.rect.centerx - 2

#  Класс - снаряд, точнее его полет
class Bullet(Block, Mech.Movement):
    def __init__(self, player, width, height):
        Block.__init__(self, player.rect.centerx, player.rect.centery, width, height)
        Mech.Movement.__init__(self)
        self.__direction = (0, 0)

    def set_direction_and_speed (self, x, y, speed):
        self.__direction = (x*speed, y*speed)

    def get_direction_and_speed (self):
        return self.__direction


class BulletGroup(Graphics.UniteSprite):
    def __init__(self, *sprites):
        super(BulletGroup, self).__init__(sprites)

    def deleteBullet (self, width, height, *collideG):

        for sprt in self:
            if sprt.rect.x > width or sprt.rect.x < 0:
                self.remove(sprt)
            elif sprt.rect.y < 0 or sprt.rect.y > height:
                self.remove(sprt)
        for collided in collideG:

            if pygame.sprite.groupcollide(self, collided, False, False) != {}:
                print 'BANG'


    def draw(self, screen):
        for sprt in self.sprites():
            sprt.move(sprt.get_direction_and_speed()[0], sprt.get_direction_and_speed()[1])
            screen.blit(sprt.image, (sprt.rect.x, sprt.rect.y))


class Enemy(Player):
    def __init__(self, Gx, Gy, GW, GH, color='#00ffff'):
        super(Enemy, self).__init__(Gx,Gy,GW,GH, color=color)
        self.dxdy = (1, 0)

    def move_to_player (self, playersprt, screen):
        if self.rect.center != playersprt.rect.center:
            direction = [0,0]
            if self.rect.centerx > playersprt.rect.centerx:
                direction[0] = -1
            elif self.rect.centerx < playersprt.rect.centerx:
                direction[0] = 1
            if self.rect.centery > playersprt.rect.centery:
                direction[1] = -1
            elif self.rect.centery < playersprt.rect.centery:
                direction[1] = 1
            self.dxdy = (direction[0], direction[1])
            alarm_rect = pygame.draw.circle(screen, pygame.Color('#00FF00'), (self.rect.centerx, self.rect.centery), 150, 3)
            if alarm_rect.colliderect(playersprt.rect) == 1:
                self.move (direction[0], direction[1])

