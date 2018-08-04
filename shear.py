from PIL import Image
import os
import random


# ori_image='one.png'
# share_img_path=''
# img = Image.open(ori_image)
# #Apply shearing by changing b(horizontal shear) and d(vertical shear) values
# a = 1
#
# b = random.uniform(0,0.9)
# c = 0
# d = random.uniform(0,0.9)
# if(b == 0):
#     d = random.uniform(0.1,0.9)
# if(d==0):
#     b=random.uniform(0.1,0.9)
# e = 1
# f = 0
# img = img.transform(img.size, Image.AFFINE, (a, b, c, d, e, f))
# # img.save()
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

        #create dir fol inside test_imgs_shear
        shear_im_p= "test_imgs_shear/" + fol
        shear_img_path = "test_imgs_shear/" + fol + "/" + filename
        if not os.path.exists(shear_im_p):
            os.makedirs(shear_im_p)

        a = 1
        b = random.uniform(0, 0.9)
        c = 0
        d = random.uniform(0, 0.9)
        if (b == 0):
            d = random.uniform(0.1, 0.9)
        if (d == 0):
            b = random.uniform(0.1, 0.9)
        e = 1
        f = 0
        shear_img = ori_img.transform(ori_img.size, Image.AFFINE, (a, b, c, d, e, f))
        shear_img.save(shear_img_path)

        print("shear_img_path : "+shear_img_path)

