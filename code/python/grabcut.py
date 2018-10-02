# http://docs.opencv.org/3.2.0/d8/d83/tutorial_py_grabcut.html

import argparse
import numpy as np
import cv2
from matplotlib import pyplot as plt


def grabcut(input_name, output_name, rect):
    img = cv2.imread(input_name)
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    # rect = (14, 249, 352, 223)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    # plt.imshow(img),plt.colorbar(),plt.show()
    cv2.imwrite(output_name, img)


if __name__ == '__main__':

    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script takes bounding box file name   
    ''')
    parser.add_argument('bbox_file', help='bounding box file name')
    args = parser.parse_args()

    # print args.bbox_file
    fin = open(args.bbox_file, 'r')
    # count = 0
    while True:
    # while count < 5:
        l = fin.readline()
        if not l:
            break
        if not l.startswith('\t'):
            input_name = l.strip()
            output_name = 'mask_' + input_name.split('/')[-1]
            # print output_name
            # print 'f', filename
            l = fin.readline()
            bbox = l.strip().split(',')
            left = int(bbox[0].strip())
            right = int(bbox[1].strip())
            top = int(bbox[2].strip())
            bot = int(bbox[3].strip())
            rect = (left, top, right-left, bot-top)
            # print 'b', rect
            grabcut(input_name, output_name, rect)
            # count += 1
