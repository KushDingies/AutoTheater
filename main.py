#from script import Script
#from line import Line
#from character import Character
from stageManager import StageManager
import sys

def main(argv):
    actors = int(argv[0])
    topics = argv[1:]
    pool = ["I like " + topics[0] + ".", "Hello!", "I don't like " + topics[0] + "."]

    manager = StageManager(actors, topics, pool)
    manager.produceScript(topics[0])
    manager.script.printScript()

if __name__ == "__main__": main(sys.argv[1:])