import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg
import os

# On prepare les trois matrices a empiler
R =255* np.ones((50,100,3), dtype=np.uint8) #im=255*ones((100,10,3), dtype=np.uint8)
i, j = np.meshgrid(\
                    np.arange(50, dtype=np.int64),\
                    np.arange(100, dtype = np.int64),\
                    indexing = 'ij')
indB=i%10 > 4
R[indB, :]=[0,0,0]


# Pour l'instant, la superposition donnerait du blanc.# On mets a 0 les 100 premieres lignes de chacune des matrices

print(R)

os.chdir("../")

# visualisation avec imshow
plt.imshow(R)
plt.show() # inutile en interactif

# Sauvegarde avec imsave
#mpg.imsave('carres.png', carres)

R=np.rot90(R)

os.chdir("../")

# visualisation avec imshow
plt.imshow(R)
plt.show() # inutile en interactif
#mpg.imsave('carres1B.png', carres)