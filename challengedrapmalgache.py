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

R =255* np.ones((100,150,3), dtype = np.uint8)

#R2 = 255* np.ones((50,150), dtype = np.uint8) 


R[:,:,:]=255
R[:,0:50,1:2]=255
R[50:100,50:150,:]=[0, 86, 27]
R[0:50,50:150,:]=[223, 109, 20]




plt.imshow(R)

plt.show()

mpg.imsave('R.png', R)
