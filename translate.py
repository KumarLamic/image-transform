from PIL import Image
import os
import random


ori_image='three.png'
scale_img_path=''
img = Image.open(ori_image)
#Apply translation by changing c and f values
a = 1
b = 0
c = 0 #left/right (i.e. 5/-5)
d = 0
e = 1
f = 0 #up/down (i.e. 5/-5)
img = img.transform(img.size, Image.AFFINE, (a, b, c, d, e, f))
# img.save()
img.show()


# dir = "./test_images_ori"
#
# for name in os.listdir(dir):
#     print(name)
#     path = os.path.join(dir, name)
#
#     fol = path.split('/')[2]
#     # print(fol)
#     for filename in os.listdir(path):
#
#         ori_img_path = path  +"/"+ filename
#         print("ori_img_path : " + ori_img_path)
#         ori_img= Image.open(ori_img_path)
#
#         #create dir fol inside test_imgs_scale
#         scale_im_p= "test_imgs_scale/" + fol
#         scale_img_path = "test_imgs_scale/" + fol + "/" + filename
#         if not os.path.exists(scale_im_p):
#             os.makedirs(scale_im_p)
#
#         # scale_factor = random.randint(2, 3)

#         a = 0
#         b = 0
#         c = 1  # left/right (i.e. 5/-5)
#         d = 0
#         e = 0
#         f = 1  # up/down (i.e. 5/-5)
#         scale_img = ori_img.transform(ori_img.size, Image.AFFINE, (a, b, c, d, e, f))
#         scale_img.save(scale_img_path)
#
#         print("scale_img_path : "+scale_img_path)

