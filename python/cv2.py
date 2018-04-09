
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


# Sample image from: http://www.sample-videos.com/download-sample-jpg-image.php
img = cv2.imread('Sampleimg.jpg',0)


# In[3]:


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

