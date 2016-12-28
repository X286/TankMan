# coding=utf-8

import pygame

class Movement(object):
    def __init__(self, speedX, speedY = -1):
        if speedY == -1:
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


# Прокрутка.
# 1 - pygame.Rect - прямоугольник в котором не происходит скроллинга
# 2 - pygame.Rect - текущая сцена на вход можно подать sprite (а так же его наследников) или rect
# 3 - игрок - его спрайт
# 4 - группы спрайтов, которые необходимо двигать, например, группы заднего плана и/или группы переднего плана
# 5 - размер основного экрана например :(800, 600)
# return -  возвращает left right up down соотвественно, когда игрок ударятеся в край поля
class ScrollingSimple(Movement):
    def __init__(self, scrolling_rect_obj, sence_sprite, player, sprite_groups, screensize):
        self.player = player
        super(ScrollingSimple, self).__init__(player.speedX, speedY=player.speedY)
        self.scroll_rect = scrolling_rect_obj
        self.player = player
        if type (sprite_groups) is list:
            self.sprite_groups = sprite_groups
        else:
            raise TypeError('List of Groups only!')

        if type(sence_sprite) is pygame.Rect:
            self.maincence = sence_sprite
        else:
            try:
                self.maincence = sence_sprite.rect
            except:
                raise TypeError ('pyGame Rect or pyGame Sprite Only!')
        self.screensize = screensize

    def scroll_left(self):
        if self.player.rect.x > self.scroll_rect.x:

            self.player.move_left()
        else:
            if self.maincence.x + self.scroll_rect.x < self.scroll_rect.x - self.player.speedX:
                for group in self.sprite_groups:
                    for item in group:
                        item.rect.x += self.player.speedX
            else:
                if self.player.rect.x > 0:
                    self.player.move_left()
                else:
                    self.player.rect.x = 0
                    return 'left'

    def scroll_right(self):
        if self.player.rect.x + self.player.rect.width < self.scroll_rect.x + self.scroll_rect.width:
            self.player.move_right()
        else:
            if self.maincence.x + self.maincence.width - \
                    (self.screensize[0] - self.scroll_rect.x - self.scroll_rect.width + self.player.speedX) > \
                            self.scroll_rect.x + self.scroll_rect.width:
                for group in self.sprite_groups:
                    for item in group:
                        item.rect.x -= self.player.speedX
            else:
                if self.player.rect.x + self.player.rect.width + self.player.speedX < self.screensize[0]:
                    self.player.move_right()
                else:
                    self.player.rect.x = self.screensize[0] - self.player.rect.width
                    return 'right'

    def scroll_up(self):
        if self.player.rect.y > self.scroll_rect.y:
            self.player.move_up()
        else:
            if self.maincence.y + self.scroll_rect.y < self.scroll_rect.y:
                for group in self.sprite_groups:
                    for item in group:
                        item.rect.y += self.player.speedY
            else:
                if self.player.rect.y > 0:
                    self.player.move_up()
                else:
                    self.player.rect.y = 0
                    return 'up'

    def scroll_down(self):
        if self.player.rect.y + self.player.rect.height < self.scroll_rect.y + self.scroll_rect.height:
            self.player.move_down()
        else:
            if self.maincence.y + self.maincence.height - (self.screensize[1] - self.scroll_rect.y - self.scroll_rect.height + self.player.speedY) > \
                            self.scroll_rect.y + self.scroll_rect.height:
                for group in self.sprite_groups:
                    for item in group:
                        item.rect.y -= self.player.speedY
            else:
                if self.player.rect.y + self.player.rect.height + self.player.speedY < self.screensize[1]:
                    self.player.move_down()
                else:
                    self.player.rect.y = self.screensize[1] - self.player.rect.height
                    return 'down'

