import urllib.request
from xml.etree.ElementTree import XML

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()
print(data)

doc = XML(data)
print(doc)

for pt in doc.findall('.//pt'):
    print(pt.text)