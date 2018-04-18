import pickle
import sys

file = 'peak.p'

_file = pickle.load(open(file, 'rb'))

for arr in _file:
	for elem in arr:
		sys.stdout.write(elem[0] * elem[1])
	print sys.stdout.write('\n')
