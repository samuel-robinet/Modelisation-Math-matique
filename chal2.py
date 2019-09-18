import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg
import os

# On prepare les trois matrices a empiler
R =255* np.ones((50,50,3), dtype=np.uint8)
i, j = np.meshgrid(\
                    np.arange(50, dtype=np.int64),\
                    np.arange(50, dtype = np.int64),\
                    indexing = 'ij')
indB=(i==j)
R[indB, :]=[0,0,0]
# Pour l'instant, la superposition donnerait du blanc.# On mets a 0 les 100 premieres lignes de chacune des matrices

print(R)
# On empile les trois matrice
#carres = np.stack((R[0], R[1], R[2]), axis =2)


os.chdir("../")

# visualisation avec imshow
plt.imshow(R)
plt.show() # inutile en interactif

# Sauvegarde avec imsave
#mpg.imsave('carres2.png', carres)