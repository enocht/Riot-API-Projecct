from riotwatcher import LolWatcher

api_key = ''  # input your api key here
watcher = LolWatcher(api_key)

region = input("Enter Server: ")
username = input("Enter Username: ")

user = watcher.summoner.by_name(region, username)
userRank = watcher.league.by_summoner(region, user['id'])
matches = watcher.match.matchlist_by_puuid(region, user['accountId'])
lastMatch = matches['matches'][0]
matchDetail = watcher.match.by_id(region,  lastMatch['gameId'])

# Printing Data
print('User:', user)
print('Rank:', userRank)
print('Number of Matches:', matches)
print('Last Match:', lastMatch)
print('Detail of Last Match:', matchDetail)
