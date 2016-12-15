# coding=utf-8

class Movement(object):
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
class ScrollingSimple(Movement):
    def __init__(self, scrollingX, scrollingY, speedX, players, *all):
        super(ScrollingSimple, self).__init__(speedX, speedY=0)
        print type (scrollingX)
        if (not (type (scrollingX) is list)and (type (scrollingY)is list)):
            raise SyntaxError (u'[X][Y], pos coords in list')
        self.scrollingX = scrollingX
        self.scrollingY = scrollingY
        self.all = all
        self.players = players
        print self.players

    def move_left(self):
        for player in self.players:

            if self.scrollingX[0] < player.rect.x:
                for group in self.all:
                    for objects, index in enumerate(group):
                        index.move_left()
                        return True
            else:
                return False
        # not needed
        #else:
        #    for player in self.players:
        #        player.move_right()


    def move_right(self):
        if self.scrollingX[0] > self.players[0].rect.x:
            for group in self.all:
                for objects, index in enumerate(group):
                    index.move_left()
                    # if players two
        else:
            for player in self.players:
                player.move_right()

    def move_up(self):
        pass

    def move_down(self):
        pass

# Скроллинг - прямоугольник т.е. персонаж бегает в каком то прямоугольнике и
# пересекая его, начинается скроллинг основной сцены
class ScrollRect(Movement): pass
