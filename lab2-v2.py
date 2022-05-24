import re

class iReader:
    def __init__(self, filePath):
        self.filePath = filePath
        self.string = ''
    
    def swapWords(self, string, numStep):
        words = re.sub(r'[^\w\s]', ' ', string).split()
        for i in range(1, len(words), numStep):
            if (len(words[i - 1]) > 1 and words[i - 1].isalpha() and len(words[i]) > 1 and words[i].isalpha()):
                temp = words[i]
                words[i] = words[i - 1]
                words[i - 1] = temp
        return words
    
    def print(self, words):
        for word in words:
            print(word, end=' ')
    
    def readFile(self):
        try:
            with open(self.filePath, 'r', encoding='utf8') as file:
                sepFlag = False
                for line in file:
                    for symbol in line:
                            if self.string.endswith('000') == False:
                                self.string += symbol
                            else:
                                if sepFlag == False:
                                    self.print(self.swapWords(self.string[0:-3], 2))
                                    self.string = symbol 
                                    sepFlag = True
                                else:
                                    self.string += symbol
                self.print(self.swapWords(self.string, 6))
        except FileNotFoundError:
            pass
        except ValueError:
            pass
        
p = iReader('test.txt')
p.readFile()