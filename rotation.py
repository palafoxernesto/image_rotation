##################################################
# Code by Ernesto Palafox                       .#
# May 17th 2018                                  #
##################################################

import argparse
import os
import cv2
import math
import numpy as np
from scipy.ndimage import rotate

def rotate_image(img_path, rotation_degrees, name):
    ''' Rotates an image and saves it into a temporal directory
    inputs:
        img_path: Path to the ID to be rotated.
    outputs:
        img_path2: Path to the rotated image.
    '''
    tmp_dir = "tmp"
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)

    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img2 = rotate(img, float(int(rotation_degrees)))

    file_name = rotation_degrees + 'º_' + name
    img_path2 = os.path.join(tmp_dir,file_name)
    cv2.imwrite(img_path2,img2)

    return img_path2


def main():
    parser = argparse.ArgumentParser(
        description='Peforms image rotation. ')
    parser.add_argument('img_path', help='Path to the image.')
    parser.add_argument('-a', '--angle', help='Rotantion angle.')
    parser.add_argument('-n', '--name', help= 'Image_name', default="rotated_image.jpg")
    args = parser.parse_args()
    rotate_image(args.img_path, args.angle, args.name)

if __name__ == '__main__':
    main()
