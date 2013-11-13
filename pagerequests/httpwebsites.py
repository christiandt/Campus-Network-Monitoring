from xml.etree import ElementTree
import binascii



pages = dict()
files = ['20131021/filtered/httphost.xml', '20131022/filtered/httphost.xml', '20131023/filtered/httphost.xml', '20131024/filtered/httphost.xml', '20131025/filtered/httphost.xml']



def parseXML(file):
	tree = ElementTree.parse(file)
	root = tree.getroot()
	for field in root.iter('field'):
	    if field.get('name') == "http.host":
	    	page = field.get('show')
	    	if page not in pages:
	    		pages[page] = 1
	    	else:
	    		pages[page] += 1


for file in files:
	parseXML(file)


sortedPages = sorted(pages, key=pages.get, reverse=True)

for page in sortedPages:
	print page, pages[page]