def check(a):
	return ord(a) >= ord('a') and ord(a) <= ord('z')
file = open("p3.txt", "r")
lines = file.readlines()
for l in lines:
	for i in xrange(4, len(l) - 4):
		if check(l[i]):
			#now to see the body guards
			if not check(l[i - 3]) and not check(l[i - 2]) and not check(l[i - 1]):
				if not check(l[i + 1]) and not check(l[i + 2]) and not check(l[i + 3]):
					if check(l[i - 4]) and check(l[i+4]):
						print l[i-3],l[i-2],l[i-1], l[i], l[i+1],l[i+2],l[i+3]
