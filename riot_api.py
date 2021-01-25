from riotwatcher import LolWatcher, ApiError

api_key = ""
watcher = LolWatcher(api_key)
region = "euw1"

me = watcher.summoner.by_name(region, "Lockdown72")
stats = watcher.league.by_summoner(region, me["id"])
#print(me["id"]) 
print(me["name"] + ": " + stats[0]["tier"] + " " + stats[0]["rank"])

def getWR(stats):
    for s in stats:
        if(s["queueType"] == "RANKED_SOLO_5x5"):
            wins = s["wins"]
            losses = s["losses"]
            return(wins/(wins+losses))
    return

print(str(round((getWR(stats)*100),2))+"%")
