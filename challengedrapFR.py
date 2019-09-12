#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:03:02 2019

@author: robinets
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

# Blanc = np.zeros((50, 50, 3), dtype=np.uint8) #zeros #eyes

R =0* np.ones((100,150), dtype = np.uint8)
V =0* np.ones((100,150), dtype = np.uint8)
B =0* np.ones((100,150), dtype = np.uint8)


R[0:100,0:50]=255
V[0:100,0:50]=255
B[0:100,0:50]=255

carres = np.stack((R, V, B), axis =2)

plt.imshow(carres)

plt.show()

mpg.imsave('carres.png', carres)
