# coding=utf-8

import pygame

class Movement(object):
    def __init__(self, speedX, speedY =0):
        if speedY == 0:
            speedY = speedX
        self.speedX = speedX
        self.speedY = speedY

    def move_left(self):
        self.rect.x -= self.speedX
        return self.rect
    def move_right(self):
        self.rect.x += self.speedX
        return self.rect
    def move_up(self):
        self.rect.y -= self.speedY
        return self.rect
    def move_down(self):
        self.rect.y += self.speedY
        return self.rect

    def set_speed(self, speedX, speedY=0):
        if speedY == 0:
            speedY = speedX
        self.speedX = speedX
        self.speedY = speedY

    def get_speed(self):
        return self.speedX, self.speedY


# скроллинг без участия игрока,
# тут *all - тут смещение всех элеметов, которые мы хотим сместить
class ShootEmUpScroll(Movement):
    def __init__(self, speedX, speedY =0, *all):
        self.all = all
        super(ShootEmUpScroll, self).__init__(speedX, speedY)

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
                one.rect.y -= self.speedY

    def move_down(self):
        for iter, idx in enumerate(self.all):
            for one in self.all[iter]:
                one.rect.y += self.speedY


# Простой скроллинг, движение если блок приблизился к экрану
# тут старт скроллинг - это когда начинать скроллинг
# игровой спрайт - игроки
# screen основное окно
# конец скроллинга не прописан
class ScrollingSimple(Movement):
    def __init__(self, scrollingX, scrollingY, speedX, players, all, speedY=0):
        super(ScrollingSimple, self).__init__(speedX, speedY=speedY)
        self.scrollingrectX = scrollingX
        self.scrollingrectY = scrollingY
        self.players = players
        self.all = all

    def move_left(self):
        for player in self.players:
            if player.rect.x - self.speedX < self.scrollingrectX[0]:
                player.rect.x = self.scrollingrectX[0]
                return True
        else:
            return False

    def move_right(self):
        for player in self.players:
            if player.rect.x +self.speedX > self.scrollingrectX[1]:
                player.rect.x = self.scrollingrectX[1]
                return True
        else:
            return False

    def move_up(self):
        for player in self.players:
            if player.rect.y - self.speedY < self.scrollingrectY[0]:
                player.rect.y = self.scrollingrectY[0]
                return True
        else:
            return False

    def move_down(self):
        for player in self.players:
            if player.rect.y + self.speedY > self.scrollingrectY[1]:
                player.rect.y = self.scrollingrectY[1]
                return True
        else:
            return False



# Скроллинг - прямоугольник т.е. персонаж бегает в каком то прямоугольнике и
# пересекая его, начинается скроллинг основной сцены
class ScrollRect(Movement): pass
