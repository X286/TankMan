# coding=utf-8

import Graphics.BaseObj as Graphics # Вкорячиваем часть графики
import Mech.Mech as Mech #Вкорячиваем механику


class Static_BG (Graphics.GraphicObject, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color='#ffff00', MSpeedY=0):
        Graphics.GraphicObject.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)


# Вызов Блока с движением (например какой то заградительный блок, например передвижной бетонный блок)
class Block (Graphics.StaticSprite, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color = '#00ff00', MSpeedY =0):
        Graphics.StaticSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
        # -1 - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = -1


#
class AnimatedObject (Graphics.AnimatedSprite, Mech.Movement):
    def __init__(self, MSpeedX, Gx, Gy, GW, GH, color='#00ffff', MSpeedY=0):
        Graphics.AnimatedSprite.__init__(self, Gx, Gy, GW, GH, color=color)
        Mech.Movement.__init__(self, MSpeedX, MSpeedY)
        # -1 - не убиваемый блок, 0 - прозрачный блок (кусты) - остальное можно уничтожить (HP)
        self.health = -1


