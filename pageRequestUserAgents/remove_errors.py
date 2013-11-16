f = open("HTTPRequestUserAgent_grr.csv", 'r')

for line in f:
	if '\\x' not in line:
			print line.rstrip('\n')
			
f.close()