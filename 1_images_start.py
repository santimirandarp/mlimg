
# LOAD/SHOW/SAVE images in PYTHON
# Usin 2 different libs: PIL & CV2

#FIRST using CV2
import cv2
#cv2 Docs https://tinyurl.com/y5ejrtmg
from glob import glob

catsNameList = glob("images/raw/cats/*")
# images should be stored here ^^^^

# let's use only one
# you can always loop
One = catsNameList[0]
catImg = cv2.imread(One, 1)
cv2.imshow(name, catImg)

# Using matplot lib + cv2
import matplotlib.pyplot as plt
catImg = cv2.imread(One, 1)
plt.imshow(catImg)
plt.show()


# SECOND using PIL 
from PIL as Image
catImg = Image.open(One) 
catImg.show()

#using PIL + matplotlib
catImg = Image.open(One) 
plt.imshow(catImg)
plt.show()


