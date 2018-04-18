file = open("p2.txt", "r")
dict_ = {"0": 0}
count = 0
l = file.readlines()
for line in l:
	#count += 1
	if count > 15:
		break
	for c in line:
		#print c
		if c in dict_:
			dict_[c] = str(int(dict_[c]) + 1)
		else:
			dict_[c] = '1'
#dict_ = sorted(dict_)
print dict_	

file.close()
