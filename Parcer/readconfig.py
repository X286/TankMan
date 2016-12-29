# coding=utf-8

import re

class lvl_prepare(object):
    def __init__(self, lvl_conf_f):
        lvl_conf = open(lvl_conf_f, 'r')
        self.__prepared_parce = {}
        self.tiles = {}
        self.sprites = {}
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

    def tiles_sprites_parce(self, tiles_key, setTileOrTile):
        tiles_key = self.__get_Key(tiles_key)
        tiles_varibles = dict()
        #Первое: находим пути к файлам тайлов - выносим их в список трассим их по месту пребывания
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
        if type (setTileOrTile) is bool:
            if setTileOrTile == True:
                self.tiles = tiles_varibles
            else:
                self.sprites = tiles_varibles
            return tiles_varibles
        else:
            raise SyntaxError ('Bool Needed')


    def check_tiles (self, tiles_key, sprites_key):
        tiles = self.tiles_sprites_parce(tiles_key, True)
        sprt = self.tiles_sprites_parce(sprites_key, False)
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


parce = lvl_prepare ('../res/lvl/lvl_conf.gen')
print parce.tiles_sprites_parce('tiles', True)
print parce.tiles_sprites_parce('sprites', False)
parce.check_tiles('tiles', 'sprites')


'''
    def __init__(self, f_path):
        self.parced = file(f_path, 'r')

    # первое чтение, разбиение его в словарь для обработки
    def preread_first (self):
        self.parced.seek(0)
        output_dict, key = {}, ''
        for line in self.parced:
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            line = line.replace(' ', '')
            line = line.replace('"', '')
            line = line.replace('\'', '')
            all = re.findall('(^[^#\[\n]+)', line)
            if all != []:
                for line in all:
                    if (line[-1:] == '!' and line [0]=='!'):
                        replacedLine = line.replace('!', '')
                        output_dict[replacedLine] = ''
                        key = replacedLine
                    elif line[-1:] == ';':
                        output_dict[key] += line
                    else:
                        raise SyntaxError ('Operator ! or ; missed!')

        return output_dict

    # разбиение на элементы и частичное приведение к типам
    def extended_split_dict(self):
        dict = self.preread_first()
        for key in dict.keys():
            subdict = {}
            for line in dict[key][:-1].split (';'):
                subdict_re= re.match('([a-zA-Z_0-9]+)=([\\(\){\}\ =_:0-9a-zA-Z/\.\,]+)', line)
                if subdict_re != None:
                    if re.match('[0-9]+', subdict_re.group(2)):
                        subdict[subdict_re.group(1)] = int(subdict_re.group(2))
                    elif re.match('[0-9]+[\.][0-9]+', subdict_re.group(2)):
                        subdict[subdict_re.group(1)] = float(subdict_re.group(2))
                    else:
                        subdict[subdict_re.group(1)] = subdict_re.group(2)
            dict[key] = {}
            dict[key] = subdict
        return dict

    # расширенное разбиение на элементы.
    def expandread (self):
        dict_ex = self.extended_split_dict()
        return dict_ex

'''