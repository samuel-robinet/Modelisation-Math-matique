#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:03:02 2019

@author: robinets
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

# Blanc = np.zeros((50, 50, 3), dtype=np.uint8) #zeros

R =255* np.ones((100,150,3), dtype = np.uint8)


R[0:100,50:150,:]=255
R[0:100,0:50,:]=[0, 0, 255]
R[0:100,100:150,:]=[255,0,0]

plt.imshow(R)

plt.show()

mpg.imsave('fr.png', R)
