import csv, re, ast, sys, tldextract


macsTotal = []
urls = dict()

with open('httphosts.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		url = row[0]
		occurrences = int(row[1])
		if 'amazonaws.com' in url: url = 'amazonaws.com'
		if 'cloudfront.net' in url: url = 'cloudfront.net'
		if 'blogspot.com' in url: url = 'blogspot.com'
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
