# coding=utf-8

import pygame
import PIL.Image as IPIL


# Основной класс для графики, он же основной задник
class GraphicObject(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color='#FF0000'):
        super(GraphicObject, self).__init__()
        self.image = pygame.Surface([width, height])
        if type(color) == str:
            self.color = pygame.Color(color)
        else:
            self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(self.color)

    def LoadImage(self, path_to_img):
        x, y = self.rect.x, self.rect.y
        self.image = pygame.image.load(path_to_img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def setSurface(self, surface):
        x, y = self.rect.x, self.rect.y
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def get_size (self):
        return self.image.get_size()

    def get_current_pos (self):
        return self.rect

    def draw(self, screen):
        screen.blit (self.image, (self.rect.x, self.rect.y))


# Класс этот будет храниться в памяти пока не закроется программа.
# Я это сделал потому, что тайлы и спрайты нужны протяжении всей игры.
class ImgEditClass(object):
    def __init__(self, path):
        self.img = IPIL.open(path)
        self.size = self.img.size

    # Вырезка спрайта или тайла из картинки или атласа
    def cut_image(self, startposX, startposY, width, height):
        cutted = self.img.crop((startposX, startposY, startposX+width, startposY+height))
        return pygame.image.frombuffer(cutted.tobytes(), cutted.size, cutted.mode)

    # Конвертирование в self.Surface. Да, да, можно и по другому, но это ж PIL!
    def convert_to_surface(self):
        mode = self.img.mode
        size = self.img.size
        data = self.img.tobytes()
        return pygame.image.frombuffer(data, size, mode)

    # Статика, "посмотреть картинку", открвыем и смотрим на что мы там наделали
    # file = ImgClass ('file.png')
    # file.show (file.cut_image)
    @staticmethod
    def show(img):
        img.show()


# Объеденение кусков в один прекрасный background, зачем? Потому что собрать проще чем рисовать
class UniteImg(object):
    def __init__(self, resolutionX, resolutionY, *images):
        self.Unite = IPIL.new("RGBA", (resolutionX, resolutionY), (0, 0, 0, 0))
        place = [0,0]
        for image in images:
            self.Unite.paste(image, (place[0], place[1]))
            if place[0]+ image.size[0] < 640:
                place [0] += image.size[0]
            else:
                place[0] = 0
                if place[1]+image.size[1] < 480:
                    place[1] += image.size[1]
                else:
                    break

    def convert_to_surface(self):
        mode = self.Unite.mode
        size = self.Unite.size
        data = self.Unite.tobytes()
        return pygame.image.frombuffer(data, size, mode)


# Объединение спрайтов в группу,  остальное из pygame.sprite.Group
class UniteSprite(pygame.sprite.Group):
    def __init__(self, *sprites):
        super(UniteSprite, self).__init__()
        self.add(sprites)



# Статический спрайт
class StaticSprite(GraphicObject):
    def __init__(self, x, y, width, height, color):
        super(StaticSprite, self).__init__(x, y, width, height, color)


# Анимированный спрайт
class AnimatedSprite(StaticSprite):
    def __init__(self, x, y, width, height, color='#00ff00'):
        super(AnimatedSprite, self).__init__(x, y, width, height, color)
        # блок анимации
        self.anim_block = []
        # кадр анимации
        self.__clip = 0

    # Создание списка анимаций ImgEditClass.cut_image
    def set_animation_list(self, *imglink):
        for img in imglink:
            self.anim_block.append(img)
        self.image = self.anim_block[0]

    def ret_animblock (self):
        return self.anim_block

    # Анимация кадра для анимации необходимо запихнуть эту функуцию в основной блок программы
    def animate(self):
        if self.__clip < len(self.anim_block):
            self.image = self.anim_block[self.__clip]
            self.__clip += 1
        else:
            self.__clip = 0

    # вернуть кадр - отладка и его номер
    def ret_clip (self):
        return self.__clip, self.anim_block[self.__clip]


# Cетка для отладки и визуального представления
class Net (object):
    def __init__(self, tileWidthHeight = (32,32), line_width = 10):
        self.net = pygame.sprite.Group()
        self.tile_WidthHeight = tileWidthHeight
        self.line_width = line_width

    # Эта функция позволяет рисовать сетку зная ширину и высоту сетки в пикселях
    def print_on_resolution (self, startXYpos =[0,0], endPoint = (640,480)):

        getoldpost = [startXYpos[0], startXYpos[1]]

        # Считаем пустое пространство в ячейках
        empty_block_part = (self.tile_WidthHeight[0]-self.line_width, self.tile_WidthHeight[1]-self.line_width)

        # Считаем количество блоков
        blocknum = (endPoint[0]/self.tile_WidthHeight[0], endPoint[1]/self.tile_WidthHeight[1])

        # Рисуем линии
        for i in range(1,blocknum[0] + 1, 1):
            self.net.add(GraphicObject (startXYpos[0], startXYpos[1],self.line_width, empty_block_part[0]*(blocknum[1])))
            startXYpos[0] += empty_block_part[0]
        self.net.add(GraphicObject(startXYpos[0], startXYpos[1], self.line_width, empty_block_part[0] * (blocknum[1])+self.line_width))

        # Рисуем линии, чтобы сетка была сеткой
        startXYpos = getoldpost
        for i in range(1, blocknum[1] + 1, 1):
            self.net.add(GraphicObject(startXYpos[0], startXYpos[1], empty_block_part[1] * (blocknum[0]), self.line_width))
            startXYpos[1] += empty_block_part[1]
        self.net.add(GraphicObject(startXYpos[0], startXYpos[1], empty_block_part[1] * (blocknum[0]), self.line_width))

        # Эта функция позволяет рисовать сетку тайлами
    def printOnTiles (self, startXYpos = [0,0], block_num = (20,15)):
        getoldpost = [startXYpos[0], startXYpos[1]]
        # Считаем пустое пространство в ячейках
        empty_block_part = (self.tile_WidthHeight[0] - self.line_width, self.tile_WidthHeight[1] - self.line_width)
        # Рисуем линии
        for i in range(1, block_num[0] + 1, 1):
            self.net.add(
                GraphicObject(startXYpos[0], startXYpos[1], self.line_width, empty_block_part[0] * (block_num[1])))
            startXYpos[0] += empty_block_part[0]
        self.net.add(GraphicObject(startXYpos[0], startXYpos[1], self.line_width,
                                   empty_block_part[0] * (block_num[1]) + self.line_width))

        # Рисуем линии, чтобы сетка была сеткой
        startXYpos = getoldpost
        for i in range(1, block_num[1] + 1, 1):
            self.net.add(
                GraphicObject(startXYpos[0], startXYpos[1], empty_block_part[1] * (block_num[0]), self.line_width))
            startXYpos[1] += empty_block_part[1]
        self.net.add(GraphicObject(startXYpos[0], startXYpos[1], empty_block_part[1] * (block_num[0]), self.line_width))

    def draw (self, screen):
        self.net.draw(screen)
