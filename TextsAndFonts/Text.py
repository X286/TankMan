#coding:utf-8
import pygame
import Graphics.BaseObj as BaseO

class TextObject (pygame.font.Font):
    def __init__(self, fpath, fsize):
        super(TextObject, self).__init__(fpath, fsize)
    def place_down_screen(self):
        pass
    def place_up_screen(self):
        pass
#
class TextConstructOnOnePage(TextObject):
    def __init__(self, fpath, fsize):
        super(TextConstructOnOnePage, self).__init__(fpath, fsize)
        self.text = []

    def set_text(self, text, color):
        self.text = []
        for line in text:
            self.text.append(self.render(line.decode('utf-8'), True, pygame.Color(color)))
    def draw(self, screen, pos, block_width):
        chpos = list(pos)
        for text in self.text:
            chpos[1] += self.get_height()
        bg = BaseO.GraphicObject(pos[0]-5, pos[1]-5, block_width, chpos[1], color='#FFFFFF')
        bg.draw(screen)
        chpos = list(pos)
        for text in self.text:
            screen.blit(text, chpos)
            chpos[1] += self.get_height()

#На выходе мы получаем группу спрайтов
class RPGLikeTextDialog (TextObject):
    def __init__(self, fpath, fsize, boxSize):
        super(RPGLikeTextDialog, self).__init__(fpath, fsize)
        self.boxSize = boxSize
        self.corner, self.line, self.empty = [], [], []
    #Вводим угол, вертикальный спрайт, горизонтальный спрайт, перемычку

    def set_border_sprites(self, cornerlst, linelst, laplst):
        self.corner = cornerlst
        self.line = linelst
        self.empty = laplst

    def construct_TBaloon(self, strtpos):
        group = BaseO.UniteSprite()
        for y in range(strtpos[1], self.boxSize[1]+strtpos[1], self.empty.get_height()):
            if y == strtpos[1]: #Это первая строка
                for x in range(strtpos[0], self.boxSize[0]+strtpos[0], self.empty.get_width()):
                    if x  == strtpos[0]:
                        sprt = BaseO.StaticSprite(x,y,self.empty.get_width(), self.empty.get_height(), color='#000000')
                        sprt.setSurface(self.corner)
                        group.add(sprt)
                    elif x == self.boxSize[0]+strtpos[0]-self.empty.get_width():
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(), color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.corner, -90))
                        group.add(sprt)
                    else:
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(), color='#000000')
                        sprt.setSurface(self.line)
                        group.add(sprt)
            elif y == self.boxSize[1]+strtpos[1] - self.empty.get_height():
                for x in range(strtpos[0], self.boxSize[0]+strtpos[0], self.empty.get_width()):
                    if x == strtpos[0]:
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),
                                                  color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.corner, 90))
                        group.add(sprt)
                    elif x == self.boxSize[0]+strtpos[0] - self.empty.get_width():
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),
                                                  color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.corner, -180))
                        group.add(sprt)
                    else:
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),
                                                  color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.line, 180))
                        group.add(sprt)
            else:
                for x in range(strtpos[0], self.boxSize[0]+strtpos[0], self.empty.get_width()):
                    if x == strtpos[0]:
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),
                                                  color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.line,90))
                        group.add(sprt)
                    elif x == self.boxSize[0]+strtpos[0] - self.empty.get_width():
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),color='#000000')
                        sprt.setSurface(pygame.transform.rotate(self.line, -90))
                        group.add(sprt)
                    else:
                        sprt = BaseO.StaticSprite(x, y, self.empty.get_width(), self.empty.get_height(),
                                                  color='#000000')
                        sprt.setSurface(self.empty)
                        group.add(sprt)
        return group
    def draw (self, screen):
        self.construct_TBaloon([60, 30]).draw(screen)
