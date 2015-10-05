from character import Character

class Line:
    def __init__(self, line, character):
        self.line = line
        self.character = character

    def printLine(self):
    	print self.character.name + ": " + self.line