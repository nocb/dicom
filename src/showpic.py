# use simpleITK  package read dcm file,and show the picture .

import os
import pydicom
import SimpleITK as sitk
import numpy as np
from PIL import Image


def showImage(img_array, frame_num = 0):
    img_bitmap = Image.fromarray(img_array[frame_num])
    return img_bitmap

file = sitk.ReadImage('pic/MR-MONO2-16-head')

print(file.GetSize())

# file.GetOrigin()
# file.GetSpacing()
# file.GetDirection()

print(file)

pixel_array = sitk.GetArrayFromImage(file)

print(pixel_array)

im=showImage(pixel_array)
im.show()
print('-----111')
