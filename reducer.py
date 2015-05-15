'''word count reducer'''

#!/usr/bin/env python 
import sys

for lines in sys.stdin:
	line=lines.strip()
	allwords=line.split()
	for word in allwords:
		print '%s\t%s' % (word,1)
[root@localhost harish_code]# cat reducer.py 
#!/usr/bin/env python

from operator import itemgetter
import sys

current_word=None
current_cout=0
word=None


for line in sys.stdin:
	line=line.strip()
	word,count=line.split('\t',1)
	try:
		count=int(count)
	except ValueError:
		continue
	if current_word==word:
		current_count+=count
	else:
		if current_word:
			print 'Count - >%s\t%s' % (current_word,current_count)
		current_count=count
		current_word=word
		
if current_word==word:
	print '%s\t%s' % (current_word,current_count)
