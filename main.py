# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 19:02:17 2015

@author: Misha Kushnir
"""

from script import Script
from line import Line
from character import Character
import sys

def main(argv):
    
    script = Script("TEST SCRIPT")
    steve = Character("STEVE")
    bob = Character("BOB")
    line = Line("I like " + argv[0] + ".", steve)
    line2 = Line("Dude, me too!", bob)
    script.addLine(line)
    script.addLine(line2)
    script.printScript()

if __name__ == "__main__": main(sys.argv[1:])