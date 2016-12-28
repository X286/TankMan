# coding=utf-8

import Graphics.BaseObj as Graphics # Вкорячиваем часть графики
import Mech.Mech as Mech #Вкорячиваем механику


class Static_BG (Graphics.GraphicObject):
    def __init__(self, Gx, Gy, GW, GH, color='#ffff00'):
        Graphics.GraphicObject.__init__(self, Gx, Gy, GW, GH, color=color)



# Вызов Блока с движением (например какой то заградительный блок, например передвижной бетонный блок)
class Block (Graphics.StaticSprite, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color = '#00ff00', MSpeedY = -1):
        Graphics.StaticSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
        # -1 - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = -1


#
class AnimatedObject (Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color='#00ffff', MSpeedY=-1):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
        # -1 - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = -1


class Player(Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color='#00ffff', MSpeedY=-1):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
        self.direction = [False, False, False, False]
        self.hit_power = 50

    def set_direction(self, *direction):
        if len (direction) != 4:
            raise ValueError ('Direction must me len 4 ')
        else:
            self.direction = direction

class Bullet(Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, player, MSpeedX, Gx, Gy, GW, GH, color='#00ffff', MSpeedY=-1):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
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