# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 19:09:23 2015

@author: Misha Kushnir
"""

from line import Line

class Script:
    def __init__(self, title):
        self.lines = []
        self.title = title
        
    def addLine(self, line):
        self.lines.append(line)
        
    def addLineAtIndex(self, index, line):
        self.lines.insert(index, line)
        
    def printScript(self):
        print "\n" + self.title
        for line in self.lines:
            print line.character.name + ": " + line.line
        print "~fin~\n"