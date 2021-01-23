from riotwatcher import LolWatcher, ApiError

api_key = "RGAPI-17576f68-6539-4efb-bc03-6913e054bda4"
watcher = LolWatcher(api_key)
region = "euw1"

me = watcher.summoner.by_name(region, "420buttslap")
stats = watcher.league.by_summoner(region, me["id"])
print(me["id"])
print(stats)