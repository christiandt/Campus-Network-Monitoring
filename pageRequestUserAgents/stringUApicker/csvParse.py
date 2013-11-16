import csv, re, ast, sys

matchString = sys.argv[1]

occurrences = 0
macsTotal = []

with open('HTTPRequestUserAgent.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
	    ua = row[0]
	    req = row[1]
	    unique = row[2]
	    macs= row[3]
	    macs = ast.literal_eval(macs)
	    if matchString in ua.lower():
		    for mac in macs:
		    	if mac not in macsTotal:
		    		macsTotal.append(mac)
		    		occurrences+=1

print occurrences