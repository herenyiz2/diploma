# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import os

image_path = r"C:\Users\Ildikó\Desktop\proba.png"
image_path = r"C:\proba.png"


image = cv2.imread(image_path)

plt.figure()
plt.imshow(image[:, :, 0])
# plt.close()
