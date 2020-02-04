from src import constant
from src import combination

class player(object):
    def __init__(self, number):
        self.id = "constant.PLAYER" + str(number)
        self.keys = eval(self.id)
        self.name = ""
        self.combi = combination.combination(self.keys)
        self.posid = "constant.PLAYER" + str(number) + "POS"
        self.pos = eval(self.posid)
        self.scoreid = "constant.SCORE" + str(number) + "POS"
        self.scorePos = eval(self.scoreid)

    def setName(self, name):
        self.name = name

