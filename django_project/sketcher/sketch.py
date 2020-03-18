import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy import ndimage

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)



def img2sketch(img):
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_gray_inv = 255 - img_gray
  img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
                              sigmaX=0, sigmaY=0)

  img_blur = ndimage.filters.gaussian_filter(img_gray_inv,sigma=20)

  # cv2.imshow('hi', img_gray)
  img_blend = dodgeV2(img_gray, img_blur)
  # img_burn = burnV2(img_gray, img_blur)

  edges = cv2.Canny(img,100,200)
  inv_edges = 255-edges
#   f = edges
  f = img_blend + edges
#   f = 255 - (inv_edges - img_blend)
  return f