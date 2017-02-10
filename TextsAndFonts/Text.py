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
        self.corner, self.line, self.lap = [], [], []
    #Вводим угол, вертикальный спрайт, горизонтальный спрайт, перемычку

    def set_border_sprites (self, cornerlst, linelst, laplst):
        self.corner = cornerlst
        self.line = linelst
        self.lap = laplst

    def construct_upperline (self, strtpos):
        group = BaseO.UniteSprite ()
        sprt = BaseO.StaticSprite (strtpos[0], strtpos[1], self.corner.get_width(), self.corner.get_height(), color='#000000')
        sprt.setSurface(self.corner)
        strtpos[0] += self.corner.get_width()
        group.add(sprt)
        for k in range (0, self.boxSize[0]-2*self.line.get_width(), self.line.get_width()):
            sprt = BaseO.StaticSprite(strtpos[0], strtpos[1], self.corner.get_width(), self.corner.get_height(), color='#000000')
            sprt.setSurface(self.line)
            strtpos[0] += self.corner.get_width()
            group.add(sprt)
        return group
    def draw (self, screen):
        self.construct_upperline([20, 450]).draw(screen)
        #screen.blit (self.corner, (150, 150))