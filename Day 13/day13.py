from itertools import permutations

persons = dict()

class Person:
    def __init__(self, playerName):
        self.name = playerName
        self.peerList = dict()


def loadPlayerPeers(loadLine):
    playerName, _, gainLose, points, _, _, _, _, _, _, peerName = loadLine.replace('.', '').split()
    if gainLose == "gain": points = int(points)
    else: points = int(points) * -1
    if playerName not in persons.keys(): persons[playerName] = Person(playerName)
    persons[playerName].peerList[peerName] = points


with open('input.txt', 'r') as file:
    for line in file:
        loadPlayerPeers(line)
    file.close()


def calcHappiness(playerList):
    sums = list()
    playerList = playerList + playerList[:2]
    for i in range(1, len(playerList) - 1):
        sums.append(persons[playerList[i]].peerList[playerList[i - 1]])
        sums.append(persons[playerList[i]].peerList[playerList[i + 1]])
    return sums



def calcAll():
    highestHappiness = 0
    playerPerms = list(permutations(persons.keys()))
    playerSums = dict()
    for perm in playerPerms:
        playerSums[perm] = calcHappiness(perm)
    for s in playerSums:
        happinessSum = sum(playerSums[s])
        if happinessSum > highestHappiness:
            highestHappiness = happinessSum
    return highestHappiness


sum1 = calcAll()
print("star 1: " + str(sum1))

me = "DJ"
loadPlayerPeers(me + " would gain 0 happiness units by sitting next to " + me)
for person in persons:
    loadPlayerPeers(person + " would gain 0 happiness units by sitting next to " + me)
    loadPlayerPeers(me + " would gain 0 happiness units by sitting next to " + person)

sum2 = calcAll()
print("star 2: " + str(sum2))
