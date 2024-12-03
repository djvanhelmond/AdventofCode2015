import json

with open('input.txt', 'r') as file:
    for line in file:
        day12 = json.loads(line)
    file.close()


def parseData(data):
    for k in data:
        if isinstance(k, list):
            parseData(k)
        if isinstance(k, dict):
            parseData(k.values())
        if isinstance(k, int):
            allInts.append(k)


def parseNoRedData(data):
    for k in data:
        if isinstance(k, list):
            parseNoRedData(k)
        if isinstance(k, dict):
            if "red" not in k.values():
                parseNoRedData(k.values())
        if isinstance(k, int):
            noRed.append(k)


allInts = list()
parseData(day12)
print("star 1: " + str(sum(allInts)))

noRed = list()
parseNoRedData(day12)
print("star 2: " + str(sum(noRed)))





