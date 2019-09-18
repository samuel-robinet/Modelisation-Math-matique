#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:23:34 2019

@author: abecassist
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

bleu = np.array([0,45,98], dtype = np.uint8)
rouge = np.array([206,17,38], dtype = np.uint8)

# Initialisation de l'image. On pourrait aussi creer les 3 plans R, V, B
# et les empiler ensuite avec la fonction stack.
dominicain = 255*np.ones((100, 150, 3), dtype = np.uint8)
#
# Creation des matrices d'indices lignes et colonnes (deja vu)
I, J = np.meshgrid(\
                    np.arange(100, dtype=np.int64),\
                    np.arange(150, dtype = np.int64),\
                    indexing = 'ij')
#
# Affectation des couleurs en respectant les conditions :
dominicain[0:40,0:65:,:]=bleu
dominicain[60:100,85:150:,:]=bleu
dominicain[60:100,0:65:,:]=rouge
dominicain[0:40,85:150,:]=rouge




#
# Voila le resultat :
plt.imshow(dominicain)
plt.show() # inutile en interactif
#
# ca merite une sauvegarde :
mpg.imsave('dominicain.png', dominicain)