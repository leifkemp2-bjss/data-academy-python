#!/usr/bin/env python3
# run chmod +x nextbus_expanded.py so that you do not have to run python3 with the file anymore

import urllib.request
import sys
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus_expanded.py route stopid')
print('Command options: ', sys.argv)

route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen(f'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={stopid}&route={route}')
data = u.read()
# print(data)

doc = XML(data)
# print(doc)

#import pdb; pdb.set_trace() # Launches debugger, like a manual breakpoint

for pt in doc.findall('.//pt'):
    print(pt.text)

# Debugging tips:
# Running the program with -i launches interactive window
# Import pdb and running pdb.pm() lets you get a post-mortem to show the error and line of failure