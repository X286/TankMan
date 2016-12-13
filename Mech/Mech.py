# coding=utf-8

class Movement (object):
    def __init__(self, speedX, speedY =0):
        if speedY == 0:
            speedY = speedX
        self.speedX = speedX
        self.speedY = speedY

    def move_left(self):
        self.rect.x -= self.speedX

    def move_right(self):
        self.rect.x += self.speedX

    def move_up(self):
        self.rect.y -= self.speedY

    def move_down(self):
        self.rect.y += self.speedY


# скроллинг без участия игрока, всегда вверх, например
# тут *all - тут смещение всех элеметов, которые мы хотим сместить
class shoot_em_up_scroll (Movement):
    def __init__(self, speedX, speedY =0, *all):
        self.all = all
        super(shoot_em_up_scroll, self).__init__(speedX, speedY)


    def move_left(self):
        for iter, idx in enumerate (self.all):
            for one in self.all[iter]:
                one.rect.x -= self.speedX

    def move_right(self):
        for iter, idx in enumerate(self.all):
            for one in self.all[iter]:
                one.rect.x += self.speedX

    def move_up(self):
        for iter, idx in enumerate(self.all):
            for one in self.all[iter]:
                one.y -= self.speedY

    def move_down(self):
        for iter, idx in enumerate(self.all):
            for one in self.all[iter]:
                one.y += self.speedY

# Простой скроллинг, движение если блок приблизился к экрану
# тут старт скроллинг - это когда начинать скроллинг
# игровой спрайт - игроки
# screen основное окно
class Scrolling_Simple (Movement):
    def __init__(self, start_crollingX, start_crollingY, speedX, screen,  speedY=0, *playerSprite):
        super(Scrolling_Simple, self).__init__(speedX, speedY)
        self.start_crollingX = start_crollingX
        self.start_crollingY = start_crollingY


# Скроллинг - прямоугольник т.е. персонаж бегает в каком то прямоугольнике и
# пересекая его, начинается скроллинг основной сцены
class Scroll_Rect (object): pass
