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
class Bullet(Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, player, MSpeedX, Gx, Gy, GW, GH, color='#00ffff', MSpeedY=-1):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self)
        self.player = player
        self.rect.x = player.rect.x + Gx
        self.rect.y = player.rect.y + Gy
        self.range = 500
        self.__range_count = 0
        self.isExsist = True
        self.bulletDirection = []


    def set_direction(self):
            self.bulletDirection = self.player.direction

    def shoot_right(self):
        if self.range > self.__range_count:
            self.move_right()
            self.__range_count += self.speedX
            self.isExsist = True
        else:
            self.isExsist = False
        return self.isExsist

    def shoot_left(self):
        if self.range > self.__range_count:
            self.move_left()
            self.__range_count += self.speedX
            self.isExsist = True
        else:
            self.isExsist = False
        return self.isExsist

    def shoot_up(self):
        if self.range > self.__range_count:
            self.move_up()
            self.__range_count += self.speedY
            self.isExsist = True
        else:
            self.isExsist = False
        return self.isExsist

    def shoot_down(self):
        if self.range > self.__range_count:
            self.move_down()
            self.__range_count += self.speedY
            self.isExsist = True
        else:
            self.isExsist = False
        return self.isExsist


class Enemy(object): pass



