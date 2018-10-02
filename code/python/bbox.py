# clean up output from yolo, leave only bounding box for hands
# <filename>
# \t<bbox_1>
# \t<bbox_2>

import sys
import os

fin = open('yolo.txt', 'r')
# fin = open('temp_yolo.txt', 'r')

while True:
	l = fin.readline()
	if not l:
		break
	if l.startswith('[filename]'):
		filename = l.strip().split('\t')[1][3:]
	if l.startswith('[label]'):
		label_line = l.strip().split('\t')[1]
		temp = label_line.split(':')
		label = temp[0]
		prob = int(temp[1].strip()[:-1])
		l = fin.readline()
		bbox_line = l.strip().split('\t')[1]
		# temp = bbox_line.split(',')
		if ('person' in label) and (prob >= 35):
			print filename
			# print '\t', label, prob, bbox_line
			print '\t', bbox_line
fin.close()