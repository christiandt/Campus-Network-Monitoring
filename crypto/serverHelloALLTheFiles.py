from xml.etree import ElementTree
import binascii
import sys



ciphers = dict()
files = ['/Users/christue/Desktop/20131021/filtered/serverHello.xml', '/Users/christue/Desktop/20131022/filtered/serverHello.xml', '/Users/christue/Desktop/20131023/filtered/serverHello.xml', '/Users/christue/Desktop/20131024/filtered/serverHello.xml', '/Users/christue/Desktop/20131025/filtered/serverHello.xml']



def parseXML(file):
	tree = ElementTree.parse(file)
	root = tree.getroot()
	for field in root.iter('field'):
	    if field.get('name') == "ssl.handshake.ciphersuite":
	    	cipher = field.get('showname')[14:-9]
	    	if cipher not in ciphers:
	    		ciphers[cipher] = 1
	    	else:
	    		ciphers[cipher] += 1


for file in files:
	parseXML(file)


sortedCiphers = sorted(ciphers, key=ciphers.get, reverse=True)

for cipher in sortedCiphers:
	print cipher, ciphers[cipher]