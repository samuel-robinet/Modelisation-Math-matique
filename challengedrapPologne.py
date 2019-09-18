#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:19:27 2019

@author: abecassist
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

# Blanc = np.zeros((50, 50, 3), dtype=np.uint8) #zeros

R =255* np.ones((100,160,3), dtype = np.uint8)


R[0:100,50:150,:]=255
R[50:100,0:160,:]=[212,33,51]

plt.imshow(R)

plt.show()

mpg.imsave('pologne.png', R)
