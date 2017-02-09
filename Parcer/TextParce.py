import re

class ParceText (object):
    def __init__(self, text_file):
        try:
            self.text = open(text_file,'r')
        except:
            raise IOError ('file '+text_file +'does not exisit')

        dialogDict = {}
        dictKey = ''
        for line in self.text:
            header = re.match('\!(.+)\!', line)
            if header != None:
                dictKey = header.group(1)
                dialogDict [dictKey] = []
            elif dictKey !='':
                dialogDict[dictKey].append (line)
        print dialogDict
ParceText('../res/Text/SaySomething')