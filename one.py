file = open("p2.txt", "r")
str = file.readlines()
for k in str:
	for c in k: 
		if c != ' ':
			print chr((2 + ord(c)))
		else:
			print ' '
file.close()
