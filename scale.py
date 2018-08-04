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

# ori_image='three.png'
# scale_img_path=''
# img = Image.open(ori_image)
#Apply scaling by changing a and e values
# a = 0.5
# b = 0
# c = 0 #left/right (i.e. 5/-5)
# d = 0
# e = 0.5
# f = 0 #up/down (i.e. 5/-5)
# img = img.transform(img.size, Image.AFFINE, (a, b, c, d, e, f))
#img.save()
# img.show()


dir = "./test_images_ori"

for name in os.listdir(dir):
    print(name)
    path = os.path.join(dir, name)

    fol = path.split('/')[2]
    # print(fol)
    for filename in os.listdir(path):

        ori_img_path = path  +"/"+ filename
        print("ori_img_path : " + ori_img_path)
        ori_img= Image.open(ori_img_path)

        #create dir fol inside test_imgs_scale
        scale_im_p= "test_imgs_scale/" + fol
        scale_img_path = "test_imgs_scale/" + fol + "/" + filename
        if not os.path.exists(scale_im_p):
            os.makedirs(scale_im_p)

        #TODO discuss scale_factor(2/3) with supervisor
        #change a and e to change the scale
        scale_factor = random.randint(2, 3)
        #rot_img = ori_img.rotate(rot_angle)
        a = scale_factor
        b = 0
        c = 0  # left/right (i.e. 5/-5)
        d = 0
        e = scale_factor
        f = 0  # up/down (i.e. 5/-5)
        scale_img = ori_img.transform(ori_img.size, Image.AFFINE, (a, b, c, d, e, f))
        scale_img.save(scale_img_path)

        print("scale_img_path : "+scale_img_path)

