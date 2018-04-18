import os
import zipfile

lines = []
with zipfile.ZipFile('6/channel.zip', 'r') as file:
	for info in file.infolist():
		if len(info.comment) > 0 and ' ' not in info.comment and '*' not in info.comment: 
			lines.append(info.comment.decode('UTF-8'))
print ''.join(lines)
