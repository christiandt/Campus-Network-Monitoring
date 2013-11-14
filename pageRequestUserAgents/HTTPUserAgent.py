from xml.etree import ElementTree
import binascii



macs = dict()
files = ['20131021/filtered/httphost.xml', '20131022/filtered/httphost.xml', '20131023/filtered/httphost.xml', '20131024/filtered/httphost.xml', '20131025/filtered/httphost.xml']



def parseXML(file):
	tree = ElementTree.parse(file)
	root = tree.getroot()
	for packet in root.iter('packet'):
		mac = ""
		user_agent = ""
		for field in packet.iter('field'):
			if field.get('name') == "wlan.sa":
				mac = field.get('show')
			if field.get('name') == "http.user_agent":
				user_agent = field.get('show')
			macs[mac] = user_agent

i=0
for file in files:
	i+=1
	print "Working on file ", i
	parseXML(file)

sortedmacs = sorted(macs, key=macs.get, reverse=True)

for mac in sortedmacs:
	print mac, "||", macs[mac]
