#!/usr/bin/python
# Filename: yolo.py
# ----------------------
# Author: Alex Fu
# Date: 06/02/2017
#

import argparse
import sys
import os
import numpy
import subprocess

if __name__ == '__main__':
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script takes a data sequence directory path   
    ''')
    parser.add_argument('sequence_path', help='data sequence directory (format: directory)', type=str)
    args = parser.parse_args()

    sequence_path = args.sequence_path.strip()
    # sequence_dir = sequence_path.split('/')[-2]

    working_directory = 'darknet/'
    for file in sorted(os.listdir(sequence_path)):
    	if file.startswith('rgb'):
    		# command = './darknet detect cfg/yolo.cfg yolo.weights ' + sequence_path + file
    		file_path = '../' + sequence_path + file
    		# print file_path
    		p = subprocess.Popen(['./darknet', 'detect', 'cfg/yolo.cfg', 'yolo.weights', file_path], cwd=working_directory)
    		p.wait()



