# coding=utf-8
# Собираем уровень из тайлов

import re

class CreateTileMap(object):
    def __init__(self, path):
        self.parcedMapa = []
        try:
            self.mapfile = open(path, 'r')
        except:
            raise IOError ('coud not open file: '+ path)
        self.__syntax_check()


    def __syntax_check(self):
        start = False
        end = False
        for line in self.mapfile:
            line = line.replace('\t', '')
            line = line.replace('\n', '')
            line = line.replace(' ', '')
            if line == '[':
                start = True
            elif line == ']':
                end = True
            else:
                matched = re.match('[a-zA-Z\{0-9\}, ]+;', line)
                if  matched != None:
                    getMapString = matched.group(0).replace(';','')
                    self.parcedMapa.append(getMapString)
                else:
                    raise SyntaxError ('Missed statement in block lower block ' + getMapString)
        if (start is False) or (end is False):
            raise SyntaxError ('missed start block or end block')

    def MapaTiles (self):
        splittedMapa = []
        for line in self.parcedMapa:
            ragnar = []
            for subline in line.split(','):
                whith_counter = re.match('[a-zA-Z0-9]+\{[0-9]+\}', subline)
                whithout_counter = re.match('[a-zA-Z0-9]+', subline)
                if whith_counter is not None:
                    gets = whith_counter.group(0)
                    retz = re.search('([a-zA-Z0-9]+)\{([0-9]+)\}', gets)
                    for i in range(0, int (retz.group(2)),1):
                        ragnar.append(retz.group(1))
                elif whithout_counter is not None:
                    ragnar.append(whithout_counter.group(0))
            splittedMapa.append(ragnar)
        return splittedMapa

class CreateSptitesOnMap(object):

    def __init__(self, spritepathf):
        self.sptiteplace = []
        try:
            self.sprtf = open(spritepathf, 'r')
        except:
            raise IOError ('Coud not open sprite file' + spritepathf)
        self.__syntax_check()

    def __syntax_check (self):
        start = False
        end = False
        for line in self.sprtf:
            line = line.replace('\t', '')
            line = line.replace('\n', '')
            line = line.replace(' ', '')
            if line == '[':
                start = True
            elif line == ']':
                end = True
            else:
                matched = re.match('[a-zA-Z\{0-9\}, ]+;', line)
                if matched != None:
                    getSpriteString = matched.group(0).replace(';', '')
                    self.sptiteplace.append(getSpriteString)
                else:
                    raise SyntaxError('Missed statement in block lower block ' + getSpriteString)
        if (start is False) or (end is False):
            raise SyntaxError('missed start block or end block')

    def SpritePlaced(self):
        splittedSprite = {}
        for line in self.sptiteplace:
            valid_value = re.match('([a-zA-Z][A-Za-z0-9]*)\{(\d+),(\d+)\}', line)
            if valid_value is not None:
                if splittedSprite.has_key(valid_value.group(1)):
                    splittedSprite[valid_value.group(1)].append([int(valid_value.group(2)), int(valid_value.group(3))])
                else:
                    splittedSprite[valid_value.group(1)] = []
                    splittedSprite[valid_value.group(1)].append([int(valid_value.group(2)), int(valid_value.group(3))])

            else:
                raise SyntaxError ('Coud not find sprite coords ' + line)
        return splittedSprite





