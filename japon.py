#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:13:58 2019

@author: abecassist
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg


rouge = np.array([188, 0, 75], dtype = np.uint8)

# Initialisation de l'image. On pourrait aussi creer les 3 plans R, V, B
# et les empiler ensuite avec la fonction stack.
japon = 255*np.ones((1000, 1500, 3), dtype = np.uint8)
#
# Creation des matrices d'indices lignes et colonnes (deja vu)
I, J = np.meshgrid(\
                    np.arange(1000, dtype=np.int64),\
                    np.arange(1500, dtype = np.int64),\
                    indexing = 'ij')
#
# Affectation des couleurs en respectant les conditions :

japon[ (500-I)**2+(750-J)**2<300**2] = rouge


#
# Voila le resultat :
plt.imshow(japon)
plt.show() # inutile en interactif
#
# ca merite une sauvegarde :
mpg.imsave('japon.png', japon)
