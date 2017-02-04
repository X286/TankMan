# coding=utf-8

import pygame

class Movement (object):

    def move(self, dx, dy):
        if dx != 0:
            self.rect.centerx += dx
        if dy != 0:
            self.rect.centery += dy
        return (dx, dy)


class Collides (object):
    @staticmethod
    def collide_walls (tdxdy, G1, G2, DoKill1, DoKill2):
        if tdxdy != (0,0):
            collide_g = pygame.sprite.groupcollide(G1, G2, DoKill1, DoKill2)
            if collide_g != {}:
                if tdxdy[0] > 0: # right collision
                    for key in collide_g.keys():
                        for sprt in collide_g[key]:
                            key.rect.right = sprt.rect.left

                if tdxdy[0] < 0: # left collision
                    for key in collide_g.keys():
                        for sprt in collide_g[key]:
                            key.rect.left = sprt.rect.right

                if tdxdy[1] < 0: # up collision
                    for key in collide_g.keys():
                        for sprt in collide_g[key]:
                            key.rect.top = sprt.rect.bottom

                if tdxdy[1] >0: # Down collision
                    for key in collide_g.keys():
                        for sprt in collide_g[key]:
                            key.rect.bottom = sprt.rect.top

# Прокрутка.
# 1 - pygame.Rect - прямоугольник в котором не происходит скроллинга
# 2 - pygame.Rect - текущая сцена на вход можно подать sprite (а так же его наследников) или rect
# 3 - игрок - его спрайт
# 4 - группы спрайтов, которые необходимо двигать, например, группы заднего плана и/или группы переднего плана
# 5 - размер основного экрана например :(800, 600)
# return -  возвращает left right up down соотвественно, когда игрок ударятеся в край поля

class ScrollingSimple (object):
    def __init__(self, scrolling_sprite, scrolling_rect, scene_size, screen, other_objects=[]):
        self.scr_sprite = scrolling_sprite
        self.srect = scrolling_rect
        self.ssize = scene_size
        self.other = other_objects
        self.screen = screen.get_rect()

    def scroll_right(self, scrolldierct):
        if self.ssize.rect.right - self.ssize.rect.width > self.ssize.rect.width:
            if self.scr_sprite.rect.right > self.screen.right:
                self.scr_sprite.rect.right = self.screen.right
        elif self.scr_sprite.rect.right > self.srect.right:
            self.scr_sprite.rect.right = self.srect.right
            for group in self.other:
                for sprt in group:
                    sprt.rect.centerx += (-1)*scrolldierct[0]
            self.ssize.rect.centerx += scrolldierct[0]

    def scroll_left(self, scrolldierct):
        if self.scr_sprite.rect.left < self.srect.left:
            self.ssize.rect.x += scrolldierct[0]
            if self.ssize.rect.left <= self.screen.left:
                self.ssize.rect.left = self.screen.left
                if self.scr_sprite.rect.left < self.screen.left:
                    self.scr_sprite.rect.left = self.screen.left
            else:
                self.scr_sprite.rect.left = self.srect.left
                for group in self.other:
                    for sprt in group:
                        sprt.rect.centerx += (-1) * scrolldierct[0]

    def scroll_up(self, scrolldierct):
        if self.scr_sprite.rect.top < self.srect.top:
            self.ssize.rect.y += scrolldierct[1]
            if self.ssize.rect.top <= self.screen.top:
                self.ssize.rect.top = self.screen.top
                if self.scr_sprite.rect.top < self.screen.top:
                    self.scr_sprite.rect.top = self.screen.top
            else:
                self.scr_sprite.rect.top = self.srect.top
                for group in self.other:
                    for sprt in group:
                        sprt.rect.centery += (-1) * scrolldierct[1]

    def scroll_down(self, scrolldierct):
        if self.ssize.rect.height - self.screen.height < self.ssize.rect.top:
            if self.screen.bottom < self.scr_sprite.rect.bottom:
                self.scr_sprite.rect.bottom = self.screen.bottom

        elif self.srect.bottom < self.scr_sprite.rect.bottom:
            self.scr_sprite.rect.bottom = self.srect.bottom
            self.ssize.rect.y += scrolldierct[1]
            for group in self.other:
                for sprt in group:
                    sprt.rect.centery += (-1)*scrolldierct[1]