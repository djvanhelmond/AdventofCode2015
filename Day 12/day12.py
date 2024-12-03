
def parseCmd(cmdStr):
    inpStr = list(cmdStr)
    num = list()
    while "".join(inpStr[0]) in "-0123456789":
        num.append(inpStr.pop(0))
    if len(num) > 0:
        return "".join(num)



sum1 = 0
sum2 = 0

lines = list()
i = 0
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line)
    file.close()

'''
for line in lines:
    while i < len(line):
        val = parseCmd(line[i:])
        if val:
            i = i + len(val)
            sum1 = sum1 + int(val)
        else:
            i = i + 1
'''


def findEndBracket(string):
    braceCount = 0
    i = 0
    while i < len(string):
        if string[i] == '{':
            braceCount = braceCount + 1
        if string[i] == '}' and braceCount != 0:
            braceCount = braceCount - 1
        i = i + 1
        if braceCount == 0:
            return string[:i]



cleanLines = list()
i = 0
for line in lines:
    while i < len(line):
        if line[i] == "{":
            braceVal = findEndBracket(line[i:])
            if "red" in braceVal:
                print(len(braceVal))
                print(braceVal)
                i = i + len(braceVal)
        else: cleanLines.append(line[i])
        i = i + 1

cleanLines = "".join(cleanLines)
i = 0
while i < len(cleanLines):
    val = parseCmd(line[i:])
    if val:
        print(val)
        i = i + len(val)
        sum2 = sum2 + int(val)
    else:
        i = i + 1

print("star 1: " + str(sum1))
print("star 2: " + str(sum2))

