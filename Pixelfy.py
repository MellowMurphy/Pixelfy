# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:16:28 2020

@author: chris
"""

import numpy as np
import skimage.io as io
from glob import glob
import os

def crop_img(img):
    min_i = 0; min_j = np.inf
    max_i = 0 ; max_j = -np.inf
    
    found_color_i = False
    for i in range(img.shape[0]):
        found_color_j = False
        for j in range(img.shape[1]):
            if found_color_j:
                if img[i][j][3] != 0:
                    if j > max_j:
                        max_j = j
                else:
                    break
            else:
                if img[i][j][3] != 0:
                    found_color_j = True
                    if j < min_j:
                        min_j = j              
        if not found_color_j:      
            if not found_color_i:
                if i > min_i:
                    min_i = i
        else:
            found_color_i = True
            if i > max_i:
                max_i = i
    return img[min_i:max_i,min_j:max_j]

inputs = glob("inputs/*.png")

try:
    for inp in inputs:
        name = inp.split("\\")[-1].replace(".png","")
        img = crop_img(io.imread(inp))
        
        io.imsave("cropped.png", img, quality = 100)
        
        ratio = img.shape[0]/img.shape[1]
        
        sizes = [16,32,64,128]
        
        os.mkdir("outputs\\" + name)
        
        for size in sizes:
            p_img = np.zeros((int(size*ratio),size,4))
            i_interval = (img.shape[0]//p_img.shape[0])+1
            j_interval = (img.shape[1]//p_img.shape[1])+1
            
            i = 0
            while i < p_img.shape[0]:
                j = 0
                while j < p_img.shape[1]:
                    if i*i_interval < img.shape[0] and j*j_interval < img.shape[1]:
                        p_img[i][j] = img[i*i_interval][j*j_interval]       
                    j += 1
                i += 1
            
            p_img = crop_img(p_img)/255
            io.imsave("outputs/{}/{}_{}.png".format(name,name,size), p_img, quality = 100)
            
except Exception as e: 
    print(e)
    