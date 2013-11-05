from xml.etree import ElementTree
import binascii
import sys

tree = ElementTree.parse(sys.argv[1])
root = tree.getroot()

ciphers = dict()


for field in root.iter('field'):
    if field.get('name') == "ssl.handshake.ciphersuite":
    	cipher = field.get('showname')[14:-9]
    	if cipher not in ciphers:
    		ciphers[cipher] = 1
    	else:
    		ciphers[cipher] += 1

sortedCiphers = sorted(ciphers, key=ciphers.get, reverse=True)

for cipher in sortedCiphers:
	print cipher, ciphers[cipher]