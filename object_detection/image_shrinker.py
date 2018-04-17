import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import zipfile
import json
import time
import glob
import cv2 as cv

from io import StringIO

from multiprocessing.dummy import Pool as ThreadPool




def shrink_image(image_path):
    image = cv.imread(image_path)
    image_small=cv.resize(image, (320,240))

    cv.imwrite('output/{}'.format(image_path),image_small)


# TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image-{}.jpg'.format(i)) for i in range(1, 4) ]
PATH_TO_TEST_IMAGES_DIR = 'images'

TEST_IMAGE_PATHS = glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.jpg'))

for image_path in TEST_IMAGE_PATHS:
            shrink_image(image_path)

        
