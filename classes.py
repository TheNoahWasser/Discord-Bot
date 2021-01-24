from enum import Enum

class Account:

    winrate = 0
    elo = 0
    lastCheckElo = 0
    

    def __init__(self, name, id, tier, rank, lp,):
        self.name = name
        self.id = id
        self.elo = self.rankToLp(tier, rank, lp)

    def rankToLp(tier, rank, lp):
        for t in tierVal:
            if(tier == t.name):
                elo += t.value
        if(rank == "III"): elo += 100
        if(rank == "II"): elo += 200
        if(rank == "I"): elo += 300
        elo += lp

class Elo:
    realLp = 0

    

    def compare(self, elo):
        return self.realLp - elo.realLp

class tierVal(Enum):

    BRONZE = 400
    SILVER = 800
    GOLD = 1200
    PLATINUM = 1600
    DIAMOND = 2000

test = Account("XDDD", "sdedefgsdgsdg", "GOLD", "III", 56)
print(test.realLp)


