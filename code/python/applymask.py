import argparse
import sys
import os
import numpy
import cv2

if __name__ == '__main__':
    
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script takes a data sequence directory path   
    ''')
    parser.add_argument('sequence_path', help='data sequence directory (format: directory)', type=str)
    args = parser.parse_args()

    sequence_path = args.sequence_path.strip()
    # sequence_dir = sequence_path.split('/')[-2]

    # print sequence_path

    indices = []
    for file in sorted(os.listdir('./')):
        if file.endswith('.png'):
            temp = file.split('.')[0]
            index = temp.split('_')[-1]
            indices.append(index)
    # print indices

    for file in sorted(os.listdir(sequence_path)):
        if file.startswith('rgb_'):
            # print file
            filepath = sequence_path + file
            img = cv2.imread(filepath)
            # print filepath
            temp = file.split('.')[0]
            index = temp.split('_')[-1]
            if index in indices:
                # print index
                img_mask = cv2.imread('./mask_' + file)
                img_out = img - img_mask
            else:
                img_out = img
            cv2.imwrite(sequence_path + 'mask_' + file, img_out)