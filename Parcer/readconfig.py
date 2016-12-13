# coding=utf-8

import re

class parcer(object):
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

