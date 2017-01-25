# coding=utf-8
import re
import Graphics.BaseObj
import ast


class ParseLvlConf(object):

    def __init__(self, lvl_conf_f):
        lvl_conf = open(lvl_conf_f, 'r')
        self.__prepared_parce = {}
        self.tiles = {}
        self.sprites = {}
        self.options = {}
        line_count = 0
        key = ''
        for line in lvl_conf:
            remove_comment_line = re.findall('(^[^#\[\n]+)', line.replace('\n', '').replace('\t', '').replace(' ', ''))

            if remove_comment_line != []:
                line_count +=1
                if remove_comment_line[0][0] == '!' and remove_comment_line[0][-1:] == '!':
                    key = remove_comment_line[0].replace('!','')
                    self.__prepared_parce[key] = []
                elif remove_comment_line[0][-1:] == ';':
                    self.__prepared_parce[key].append (remove_comment_line[0].replace(';',''))
                else:
                    raise SyntaxError ('! or ; missed at line: '+str (line_count))
        self.__check_errors()

    def __check_errors(self):
        line_count = 0
        for key in self.__prepared_parce.keys():
            for element in self.__prepared_parce[key]:
                line_count +=1
                match = re.findall("[a-zA-Z_0-9]+=([a-zA-Z0-9]+|\'|\()[a-zA-Z_0-9:,\\\./]+(\'|\))", element)
                if match == []:
                    raise SyntaxError ('Error at ' + element)

    def prepare_oprions (self, key):
        if self.__prepared_parce.has_key(key):
            for option in self.__prepared_parce[key]:
                # split_options
                match = re.match('([a-zA-Z][A-Za-z0-9_]*)=(\([0-9,]+\))', option)
                if match == None:
                    raise SyntaxError ('Option: ' + option + 'Failed')
                self.options[match.group(1)] = ast.literal_eval(match.group(2))
        else:
            raise SyntaxError ('Coud not find options!')

    def tiles_parce(self, tiles_key):
        tiles_key = self.__get_Key(tiles_key)
        tiles_varibles = dict()
        for path in tiles_key:
            tilePath = re.match("([a-z_0-9]+)=('[a-z_ 0-9A-Z\\\./]+')", path)

            if tilePath != None:
                try:
                    open(tilePath.group(2).replace('\'', ''), 'r').close()
                except:
                    raise SyntaxError('Coud not open file: ' + tilePath.group(2))
                tiles_varibles[tilePath.group(1)] = [tilePath.group(2).replace('\'','')]
            else:
                tile_varible = re.match("([a-zA-Z0-9]+)=\(([a-z_A-Z0-9]+)\)", path)
                selected_math = re.match("([a-zA-Z0-9]+)=\((\d+,\d+,[a-z_A-Z0-9]+)\)", path)
                if tile_varible != None:
                    if tiles_varibles.has_key(tile_varible.group(2)):
                        tiles_varibles[tile_varible.group(2)].append(tile_varible.group(1))
                elif selected_math != None:
                    splitted = selected_math.group(2).split(',')
                    if tiles_varibles.has_key(splitted[2]):
                        if re.match("([a-zA-Z][a-zA-Z0-9]*)", selected_math.group(1)) != None:
                            tiles_varibles[splitted[2]].append((selected_math.group(1), int(splitted[0]), int(splitted[1])))
                        else:
                            raise SyntaxError ("Value cannot be the digit! " + selected_math.group(1))
                else:
                    raise SyntaxError ('Bad things in line: ' + path)

        self.tiles = tiles_varibles
        return self.tiles

    def sprites_parce(self, sprite_key):
        sprites_list = self.__prepared_parce[sprite_key]
        for sprites_item in sprites_list:
            # Проверяем пути к спрайтовым атласам
            if re.match('([a-zA-Z][A-Za-z_0-9]*)[= ]+\'([\\/a-zA-Z0-9\.]+)\'', sprites_item)!=None:
                sprite_atlas_mach = re.match('([a-zA-Z][A-Za-z_0-9]*)[= ]+\'([\\/a-zA-Z0-9\.]+)\'', sprites_item)
                try:
                    file(sprite_atlas_mach.group(2), 'r')
                except:
                    raise SyntaxError ('Coud not open file at:' + sprite_atlas_mach.group(2))
                self.sprites[sprite_atlas_mach.group(1)] = [sprite_atlas_mach.group(2)]
            elif re.match('([a-zA-Z][A-Za-z_0-9]*)[ =]+\(([ _a-zA-Z0-9]+)\)', sprites_item):
                match = re.match('([a-zA-Z][A-Za-z_0-9]*)[ =]+\(([ _a-zA-Z0-9]+)\)', sprites_item)
                if self.sprites.has_key(match.group(2)):
                    self.sprites[match.group(2)].append(match.group(1))
            elif re.match('[a-zA-Z][A-Za-z_0-9]*[ =]+\([0-9, ]+([a-z_A-Z0-9]+)\)', sprites_item) != None:
                match = re.match('([a-zA-Z][A-Za-z_0-9]*)[ =]+\(([0-9, ]+)([a-z_A-Z0-9]+)\)', sprites_item)
                if self.sprites.has_key(match.group(3)):
                    accum = [match.group(1)]
                    for integer in match.group(2)[:-1].split (','):
                        accum.append(int(integer))
                    self.sprites[match.group(3)].append(tuple(accum))
        return self.sprites

    def check_names (self, tiles_key, sprites_key):
        tiles = self.tiles_parce(tiles_key)
        sprt = self.sprites_parce(sprites_key)

        for tkey in tiles.keys():
            if sprt.has_key(tkey):
                raise SyntaxError('Syntax Error! match '+tkey)
            for tile in range (1, len (tiles[tkey]), 1):
                if type (tiles[tkey][tile]) is str:
                    for sprtkey in sprt.keys():
                        if type (sprt[sprtkey][1]) is str:
                            if tiles[tkey][tile] == sprt[sprtkey][1]:
                                raise SyntaxError ('Varibles is same ' + tiles[tkey][tile])
                elif type (tiles[tkey][tile]) is tuple:
                    for sk in sprt.keys():
                        if sprt[sk][1][0] == tiles[tkey][tile][0]:
                            raise SyntaxError('Varibles is same ' + tiles[tkey][tile][0])

    def getDict(self):
        return self.__prepared_parce

    def __get_Key(self, key):
        return self.__prepared_parce[key]

    def getOptions(self):
        return self.options

