# coding=utf-8

import re

class lvl_prepare(object):
    def __init__(self, lvl_conf_f):
        lvl_conf = open(lvl_conf_f, 'r')
        self.__prepared_parce = {}
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

    def load_tiles(self, tiles_key):
        tiles = self.__get_Key(tiles_key)
        varible_name = []
        #Первое: находим пути к файлам тайлов - выносим их в список трассим их по месту пребывания
        for path in tiles:
            tilePath = re.match("([a-z_0-9]+)=('[a-z_ 0-9A-Z\\\./]+')", path)

            if tilePath != None:
                try:
                    open(tilePath.group(2).replace('\'', ''), 'r').close()
                except:
                    raise SyntaxError('Coud not open file: ' + tilePath.group(2))
                print tilePath.group(1), tilePath.group(2).replace('\'','')
            else:
                tile_varible = re.match("([a-zA-Z0-9]+)=\(([a-z_A-Z0-9]+)\)", path)
                selected_math = re.match("([a-zA-Z0-9]+)=\((\d+,\d+,[a-z_A-Z0-9]+)\)", path)
                if tile_varible != None:
                    print tile_varible.group(2)
                elif selected_math != None:
                    print selected_math.group(2).split(',')
                else:
                    raise SyntaxError ('Bad things in line: '+ path)

        print varible_name

    def getDict(self):
        return self.__prepared_parce

    def __get_Key(self, key):
        return self.__prepared_parce[key]


lvl_prepare ('../res/lvl/lvl_conf.gen').load_tiles('tiles')


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