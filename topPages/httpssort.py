import csv, re, ast, sys, tldextract


macsTotal = []
urls = dict()

with open('SSLSorted.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		url = str(row[0]).strip()
		occurrences = int(row[1])
		if 'amazonaws.com' in url: url = 'amazonaws.com'
		ext = tldextract.extract(url)
		if ext.suffix != '':
			result = '*.' + ext.domain + '.' + ext.suffix
			if result in urls:
				urls[result] += occurrences
			else:
				urls[result] = occurrences

sortedURLs = sorted(urls, key=urls.get, reverse=True)

for url in sortedURLs:
	printed = url+","+str(urls[url])
	print printed



#ext = tldextract.extract('http://forums.bbc.co.uk')
