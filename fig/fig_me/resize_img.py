from PIL import Image
from glob import glob
import numpy as np, os

max_h = 200
try:
    os.system('rm *_small*')
except:
    pass

arr_img = glob('*.jpg')

for img_name in arr_img:
    img = Image.open(img_name)
    h, w, c = np.shape(img)
    
    max_w = int(max_h*w/h)

    print(img_name+'\n', h, w, '\t-->\t', max_h, max_w)

    img_small = img.resize((max_w, max_h))

    new_img_name = img_name[:img_name.rfind('.jpg')]+'_small.jpg'
    img_small.save(new_img_name)
print('done')
