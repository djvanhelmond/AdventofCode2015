#! /usr/bin/python

import numpy


def parseline ( line ):
  action = [0, [0, 0], [0, 0]]
  command = line.split(' ')
  if command[0] == "toggle":
    action[0] = "1"
    action[1] = command[1].split(',')
    action[2] = command[3].split(',')
  elif command[0] == "turn":
    if command[1] == "on":
      action[0] = "2"
      action[1] = command[2].split(',')
      action[2] = command[4].split(',')
    elif command[1] == "off":
      action[0] = "3"
      action[1] = command[2].split(',')
      action[2] = command[4].split(',')
  return action

def toggle( begin, end ):
  for i in range(int(begin[0]), int(end[0])+1):
    for j in range(int(begin[1]), int(end[1])+1):
      lights[i,j] += 2

def turn_on( begin, end ):
  for i in range(int(begin[0]), int(end[0])+1):
    for j in range(int(begin[1]), int(end[1])+1):
      lights[i,j] += 1

def turn_off( begin, end ):
  for i in range(int(begin[0]), int(end[0])+1):
    for j in range(int(begin[1]), int(end[1])+1):
      if lights[i,j] > 0:
        lights[i,j] -= 1


filename = './input'
size = 1000


lights = numpy.zeros((size, size), dtype=int)
total = 0


with open(filename) as f:
  for linen in f:
    line = linen.rstrip('\n')
    action = parseline(line)
    if action[0] == "1":
      toggle(action[1], action[2])
    elif action[0] == "2":
      turn_on(action[1], action[2])
    elif action[0] == "3":
      turn_off(action[1], action[2])
 #   print "--"
    print line
 #   print lights


for i in range(0, size):
  for j in range(0, size):
    if lights[i,j]:
      total += lights[i,j]

print total
