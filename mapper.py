'''mapper for word count'''

#!/usr/bin/env python 
import sys

for lines in sys.stdin:
	line=lines.strip()
	allwords=line.split()
	for word in allwords:
		print '%s\t%s' % (word,1)
