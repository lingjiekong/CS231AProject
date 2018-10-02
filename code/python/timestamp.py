#!/usr/bin/python
# Filename: timestamp.py
# ----------------------
# Author: Alex Fu
# Date: 06/02/2017
#

import argparse
import sys
import os
import numpy

if __name__ == '__main__':
    
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script takes a data sequence directory path   
    ''')
    parser.add_argument('sequence_path', help='data sequence directory (format: directory)', type=str)
    args = parser.parse_args()

    sequence_path = args.sequence_path.strip()
    sequence_dir = sequence_path.split('/')[-2]

    # directory = 'temp_' + sequence_dir
    # if not os.path.exists(directory):
    # 	os.makedirs(directory)
    # 	print 'create temp dir:', directory

    # create timestamp files
    tag = ['rgb', 'depth', 'thermal']
    prefix = ['mask_rgb_', 'aligned_depth_', 'thermal_it_']

    fout = []
    for i in range(len(tag)):
    	# f = open(directory + '/' + tag[i] + '.txt', 'w')
    	f = open(tag[i] + '.txt', 'w')
    	f.write('# timestamp: ' + tag[i] + '\n')
    	f.write('# prefix: ' + prefix[i] + '\n')
    	f.write('# formate: <timestamp> <filename>\n')
    	fout.append(f)

    for file in sorted(os.listdir(sequence_path)):
    	for i in range(len(prefix)):
    		if file.startswith(prefix[i]):
    			timestamp = file.split('_')[-1][:-4] # check this
    			fout[i].write(timestamp + ' ' + file + '\n')

