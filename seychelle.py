#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:34:34 2019

@author: abecassist
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

bleu= np.array([0, 63, 135], dtype = np.uint8)
jaune= np.array([255, 216, 86], dtype = np.uint8)
vert= np.array([0, 122, 61], dtype = np.uint8)
rouge = np.array([214, 40, 40], dtype = np.uint8)

# Initialisation de l'image. On pourrait aussi creer les 3 plans R, V, B
# et les empiler ensuite avec la fonction stack.
seychelle = 255*np.ones((1000, 2000, 3), dtype = np.uint8)
#
# Creation des matrices d'indices lignes et colonnes (deja vu)
I, J = np.meshgrid(\
                    np.arange(1000, dtype=np.int64),\
                    np.arange(2000, dtype = np.int64),\
                    indexing = 'ij')
#
# Affectation des couleurs en respectant les conditions :
seychelle[:,:,:]=vert
seychelle[1000-(J/5)>=I] = np.array([255, 255, 255], dtype = np.uint8)
seychelle[1000-(J/5)*2>=I] = rouge
seychelle[1000-(J/5)*4>=I] = jaune
seychelle[1000-(J/5)*8>=I] = bleu




#
# Voila le resultat :
plt.imshow(seychelle)
plt.show() # inutile en interactif
#
# ca merite une sauvegarde :
mpg.imsave('seychelle.png', seychelle)