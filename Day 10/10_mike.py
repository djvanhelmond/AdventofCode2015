#! /usr/bin/python

from itertools import groupby

def say(input):
    say = ""
    repeats = [list(g) for k, g in groupby(str(input))]
    for group in repeats:
        say += str(len(group)) + str(group[0])
    return say

output = "1321131112"
for _ in range(40):
    input = output
    output = say(input)

print(len(output))
