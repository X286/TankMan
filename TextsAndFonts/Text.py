#coding:utf-8
import pygame
import Graphics.BaseObj as BaseO

class TextObject (pygame.font.Font):
    def __init__(self, fpath, fsize):
        super(TextObject, self).__init__(fpath, fsize)
        self.fsize = fsize
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

# На выходе мы получаем группу спрайтов
class RPGLikeTextDialog (TextObject):
    def __init__(self, fpath, fsize, boxSize):
        super(RPGLikeTextDialog, self).__init__(fpath, fsize)
        self.boxSize = boxSize
        self.corner, self.line, self.empty = [], [], []
        self.pos = [0, 0]
        self.dialog_gr = ''
        self.text_g = ''
        self.offset = [10, 10]
    #Вводим угол, вертикальный спрайт, горизонтальный спрайт, перемычку

    def set_border_sprites(self, cornerlst, linelst, laplst):
        self.corner = cornerlst
        self.line = linelst
        self.empty = laplst
        self.setDialogpos(0, 0)


    def setDialogpos (self, x, y):
        self.pos = [x, y]
        self.dialog_gr = self.construct_TBaloon ((x, y))

    def setText (self, scenario, textColor):

        splitted = scenario[0].decode('UTF-8').split('\\')
        self.text_g = BaseO.UniteSprite()
        for line in splitted:
            text = BaseO.StaticSprite(self.pos[0] + self.offset[0], self.pos[1]+self.offset[1], self.boxSize[0]-self.offset[0], self.boxSize[1]-self.offset[1], ('#000000'))
            renderedSurface = self.render(line, True, pygame.Color(textColor))
            if renderedSurface.get_width() > self.boxSize[0]-2*self.offset[0] - self.pos[0]:
                # определяем что есть длинная линия
                print 'big line!\n', line, len(line), renderedSurface.get_width()
                splitted_line = line.split(' ')
                print splitted_line[0]


            else:
                text.setSurface(renderedSurface)
                self.text_g.add(text)
                self.pos[1] += self.fsize
            #print len(scenario[0].decode('UTF-8')), text.image.get_width(), self.boxSize[0]-2*self.offset[0] - self.pos[0], text.image.get_width()



    def setTextOffset (self, x,y):
        self.offset = (x,y)

    # Рисуем Baloon
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

    def draw(self, screen):
        self.dialog_gr.draw(screen)
        self.text_g.draw (screen)
