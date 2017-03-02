import re

class CreateSptitesOnMap(object):

    def __init__(self, spritepathf, tile_size):
        self.sptitedict = {}
        try:
            self.sprtf = open(spritepathf, 'r')

        except:
            raise IOError ('Coud not open sprite file' + spritepathf)
        self.__split_sprites_to_dict(tile_size)
    #syntax [!Name! varible {posx, posy};...etc] - create sprites on map
    def __split_sprites_to_dict(self, tile_size):
        openedSprites = 0
        closedSprites = 0
        currentkey = ''

        for line in self.sprtf:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            match = re.match('\[!([A-Za-z][a-zA-Z0-9]*)!', line)
            if  match is not None:
                openedSprites +=1
                self.sptitedict[match.group(1)] = {}
                currentkey = match.group(1)
            elif line == ']':
                closedSprites += 1
            else:
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace(' ', '')
                mached = re.match('(([a-zA-Z][a-zA-Z0-9]*)\{([0-9]+),([0-9]+)\}[,;])+', line)
                if mached != None:
                    for item in mached.group(0)[:-1].split(';'):
                        sprt = re.match('([a-zA-Z0-9][a-zA-Z0-9]*)\{([0-9]+),([0-9]+)\}', item)
                        if not self.sptitedict[currentkey].has_key(sprt.group(1)):
                            self.sptitedict[currentkey][sprt.group(1)]= [(tile_size[0]*int(sprt.group(2)), tile_size[1]*int(sprt.group(3)))]
                        else:
                            self.sptitedict[currentkey][sprt.group(1)].append ((tile_size[0]*int(sprt.group(2)), tile_size[1]*int(sprt.group(3))))

        if openedSprites != closedSprites:
            raise SyntaxError('cloded or opened tag ] [!text! messed!')


#print CreateSptitesOnMap ('../res/lvl/lvl1_sprt.gen', (50,50)).sptitedict