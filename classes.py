from riotwatcher import LolWatcher, ApiError
from enum import Enum
import pickle

watcher = object()

def initWatcher(key):
    watcher = LolWatcher(key)

class Account:

    winrate = 0
    elo = 0
    lastCheckElo = 0
    

    def __init__(self, name, id, tier, rank, lp,):
        self.name = name
        self.id = id
        self.elo = self.rankToLp(tier, rank, lp)

    def __init__(self, name):

    def rankToLp(self, tier, rank, lp):
        for t in tierVal:
            if(tier == t.name):
                self.elo += t.value
        if(rank == "III"): self.elo += 100
        if(rank == "II"): self.elo += 200
        if(rank == "I"): self.elo += 300
        self.elo += lp
    
    def save(self):
        with open("accounts/" +self.name + ".account", "wb") as output:
            pickle.dump(self, output, 1)

class tierVal(Enum):

    BRONZE = 400
    SILVER = 800
    GOLD = 1200
    PLATINUM = 1600
    DIAMOND = 2000

test = Account("XDDD", "sdedefgsdgsdg", "GOLD", "III", 56)


