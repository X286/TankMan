import re

class CreateSptitesOnMap(object):

    def __init__(self, spritepathf, tile_size):
        self.sptitedict = {}
        try:
            self.sprtf = open(spritepathf, 'r')

        except:
            raise IOError ('Coud not open sprite file' + spritepathf)
        self.__split_sprites_to_dict(tile_size)

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
                mached = re.match('(([a-zA-Z][a-zA-Z0-9]*)\{([0-9]+),([0-9]+)\}[,;])+', line)
                if not self.sptitedict[currentkey].has_key(mached.group(2)):
                    self.sptitedict[currentkey][mached.group(2)] = [(tile_size[0]*int(mached.group(3)), tile_size[1]*int(mached.group(4)))]
                else:
                    self.sptitedict[currentkey][mached.group(2)].append ((tile_size[0]*int(mached.group(3)), tile_size[1]*int(mached.group(4))))

        if openedSprites != closedSprites:
            raise SyntaxError('cloded or opened tag ] [!text! messed!')


#CreateSptitesOnMap ('../res/lvl/lvl1_sprt.gen', (50,50))