#! /usr/bin/python

import md5
import re

salt = "yzbqklnj"


found = False
regex = "000000.*"
i = 1

while not found: 
  plain = salt + str(i)
  hashed = md5.new(plain)
  
  if re.match(regex, hashed.hexdigest()) is not None:
    print "%i match (%s)" % (i, hashed.hexdigest())
    found = True
  elif i % 10000 == 0:
    print "%i no match" % i
  i += 1



