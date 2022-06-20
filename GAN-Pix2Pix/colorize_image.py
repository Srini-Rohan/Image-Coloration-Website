import os
import time
from keras.layers import  Concatenate
from skimage.color import lab2rgb
from utils.save_image import save_image
from models.core_generator import CoreGenerator
import cv2
import tensorflow as tf
import numpy as np


core_generator = CoreGenerator()
core_generator.model.load_weights('./weights/core_generator.h5')
img=cv2.imread('./image.jpeg')
save_image(img,core_generator)
