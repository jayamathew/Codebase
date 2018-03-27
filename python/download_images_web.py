#sample code to download an image from the web
#repo of sample images to test: https://homepages.cae.wisc.edu/~ece533/images/

import urllib.request
import os

#add in the url for the image you want to download
img = 'https://homepages.cae.wisc.edu/~ece533/images/airplane.png'

#retrieve and save the image to a specified location 
urllib.request.urlretrieve(img, r'C:\Users\...\test' +os.path.basename(img))