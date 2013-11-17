import csv, re, ast, sys


occurrences = 0
macsTotal = []
urls = dict()

with open('SSLIP.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
	    add = row[0]
	    ip = row[1]
	    req = row[2]
	    urls[add] = int(req)

sortedURLs = sorted(urls, key=urls.get, reverse=True)

for url in sortedURLs:
	print url, ",", urls[url]

