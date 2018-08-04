from PIL import Image
import os
import random

ori_img = "zero.png"


# ori_img = Image.open(ori_img)
#
#
# rot_angle = random.randint(0, 360)
# trans_img = ori_img.rotate(rot_angle)
#
# trans_img.show()


# shift = 1
# image = Image.open(ori_img)
# inverted_image = Image.invert(image)
#
# out = image[:image.rfind('.')]
# inverted_image.save('%s-n.JPG'%out)

# Shift the image 5 pixels
# width, height = image.size
# shifted_image = Image.new("RGB", (width+shift, height))
# shifted_image.paste(image, (1, 0))
# shifted_image.show()

#shifted_image.save('%s-shifted.JPG' % out)

# Affine Transformation
# Image.transform(size, method, data)
# with method=Image.AFFINE returns a copy of an image
# where an affine transformation matrix
# (given as 6-tuple (a, b, c, d, e, f)via data) has been applied.
# For each pixel (x, y),
# the output will be calculated as (ax+by+c, dx+ey+f).
# So if you want to apply a translation,
# you only have to look at the c and f values of your matrix.

ori_image='three.png'
img = Image.open(ori_image)
#Apply scaling by changing a and e values
a = 3
b = 0
c = 0 #left/right (i.e. 5/-5)
d = 0
e = 3
f = 0 #up/down (i.e. 5/-5)
img = img.transform(img.size, Image.AFFINE, (a, b, c, d, e, f))
img.save("3.jpg")
img.show()