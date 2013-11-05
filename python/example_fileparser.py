f = open("dns.txt", 'r')
URLs = dict()

for line in f:
	if "A " in line:
		URL = line.split("A ")[1].strip('\n')
		if URL in URLs:
			URLs[URL] += 1
		else:
			URLs[URL] = 1

for URL in URLs:
	print URL, URLs[URL]

#print max(URLs, key=URLs.get)

f.close()