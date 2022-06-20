import numpy as np
from skimage.color import rgb2lab, lab2rgb, rgb2gray, gray2rgb
import cv2




def save_image(img,core_generator):

    size=img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)
    img=img/255
    img=np.reshape(img,(1,256,256,1))
    img_lab=core_generator.model.predict(img)
    img=np.reshape(img,(256,256,1))
    img_lab=np.reshape(img_lab,(256,256,2))
    img_color = np.zeros((256, 256, 3))
    img_color[:,:,0] = img[:,:,0] *100
    img_color[:,:,1:] = img_lab * 128
    img_color=lab2rgb(img_color)
    img_color=(img_color*255).astype(np.uint8)
    img_color=cv2.cvtColor(img_color,cv2.COLOR_RGB2BGR)
    img_color = cv2.resize(img_color,(size[1],size[0]))
    cv2.imwrite('./color.jpeg',img_color)
