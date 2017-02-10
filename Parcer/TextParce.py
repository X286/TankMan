# coding: utf-8
import re

class SimpleParceText (object):
    def __init__(self, text_file):
        text = open(text_file, 'r')
        self.dictShow={}
        for line in text:
            line = line.replace('\n', '').replace('\t', '')
            match = re.match('([0-9]+)[ =]+(.+)', line, re.U)
            if match is not None:
                self.dictShow[match.group(1)]= match.group(2).split('|')
    def get_dialog(self, key):
        return self.dictShow[key]

class SimpleParceTextForRPGLikeDialog (object):
    def __init__(self, text_file):
        text = open(text_file, 'r')
        self.dictShow={}
        for line in text:
            line = line.replace('\n', '').replace('\t', '')
            match = re.match('([0-9]+)[ =]+(.+)', line, re.U)
            if match is not None:
                self.dictShow[match.group(1)]= match.group(2)
    def get_dialog(self, key):
        return self.dictShow[key]
