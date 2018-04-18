import urllib
import time

link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
noth = str(16044/2)
trig = False

while not trig:
	f = urllib.urlopen(link + noth)
	l = f.readlines()
	trig = True
	print 'Current url',link+noth
	for lines in l:
		lines = lines.split(" ")
		for something in lines:
			if something.isdigit():
	#		if int(something) == 12345:
	#			print 'Links to 12345'
	#			time.sleep(30)
				noth = something
				trig = False
				print 'rolling onto',something
			
		if trig:
			print lines
			time.sleep(30)
	
