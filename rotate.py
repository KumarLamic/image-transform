# rotate an image counter-clockwise using the PIL image library
# free from:  http://www.pythonware.com/products/pil/index.htm
# make sure to install PIL after your regular python package is installed
from PIL import Image
import os
import random


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

        #TODO create dir fol inside test_imgs_rot
        rot_im_p= "test_imgs_rot10/" + fol
        rot_img_path = "test_imgs_rot10/" + fol + "/" + filename
        if not os.path.exists(rot_im_p):
            os.makedirs(rot_im_p)
        rot_angle = 10
        rot_img = ori_img.rotate(rot_angle)
        rot_img.save(rot_img_path)

        print("rot_img_path : "+rot_img_path)


