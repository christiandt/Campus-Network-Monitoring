from xml.etree import ElementTree
import binascii, subprocess



user_agents = dict()

files = ['20131021/filtered/httphost.xml', '20131022/filtered/httphost.xml', '20131023/filtered/httphost.xml', '20131024/filtered/httphost.xml', '20131025/filtered/httphost.xml']
#files = ['/Users/christue/Desktop/filtered.xml']


def parseXML(file):
	tree = ElementTree.parse(file)
	root = tree.getroot()
	for packet in root.iter('packet'):
		
		for field in packet.iter('field'):
			if field.get('name') == "wlan.sa":
				mac = field.get('show')
			if field.get('name') == "http.user_agent":
				user_agent = field.get('show')
				if user_agent not in user_agents:
					macs = {mac:0}
					user_agents[user_agent] = [0, macs]
					user_agents[user_agent][0] = 1
				else:
					user_agents[user_agent][0] += 1
					user_agents[user_agent][1][mac] = 0

i=0
for file in files:
	i+=1
	print "Working on file ", i
	parseXML(file)
	subprocess.call('/Applications/terminal-notifier.app/Contents/MacOS/terminal-notifier -title "Done" -message "file %s is filtered" -sound default'%i, shell=True)


sortedUA = sorted(user_agents, key=user_agents.get, reverse=True)

for user_agent in sortedUA:
	if "\\" not in user_agent:
		print user_agent, "----", user_agents[user_agent][0], "----", len(user_agents[user_agent][1]), "----", [key for key in user_agents[user_agent][1].keys()]