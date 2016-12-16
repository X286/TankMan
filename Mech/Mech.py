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
    def __init__(self, scrollingX, scrollingY, speedX, players, all):
        super(ScrollingSimple, self).__init__(speedX, speedY=0)
        if (not (type (scrollingX) is list)and (type (scrollingY)is list)):
            raise SyntaxError (u'[X][Y], pos coords in list')
        self.scrollingX = scrollingX
        self.scrollingY = scrollingY
        self.all = all
        self.players = players

    def move_left(self):
        in_board = 0
        for player in self.players:
            if self.scrollingX[0] < player.rect.x:
                in_board +=1
        if in_board == len(self.players):
            for group in self.all:
                for item in group:
                    item.move_left()
            return True
        else:
            return False

    def move_right(self):

        in_board = 0
        for player in self.players:
            if self.scrollingX[1] > player.rect.x > 0:
                in_board += 1
        if in_board == len(self.players):
            for group in self.all:
                for item in group:
                    item.move_right()
            return True
        else:
            return False

    def move_up(self):
        in_board = 0
        for player in self.players:
            if self.scrollingY[0] > player.rect.y > 0:
                in_board += 1
        if in_board == len(self.players):
                for group in self.all:
                    for item in group:
                        item.move_down()
                return True
        else:
                return False

    def move_down(self):
        in_board = 0
        for player in self.players:
            if self.scrollingY[1] < player.rect.y :
                in_board += 1
        if in_board == len(self.players):
                for group in self.all:
                    for item in group:
                        item.move_up()
                return True
        else:
            return False


    # может скроллить, если все игроки находятся в секторе скроллинга
    #[Вверх вверх, вправо влево]
    def scroll (self):
        merge = []
        merge.append(self.move_down())
        merge.append(self.move_up())
        merge.append(self.move_right())
        merge.append(self.move_left())
        return merge


# Скроллинг - прямоугольник т.е. персонаж бегает в каком то прямоугольнике и
# пересекая его, начинается скроллинг основной сцены
class ScrollRect(Movement): pass
