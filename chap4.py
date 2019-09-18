import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

R = 255*np.ones((80,80,3), dtype=np.uint8)
i, j = np.meshgrid(\
                    np.arange(80, dtype=np.int64),\
                    np.arange(80, dtype = np.int64),\
                    indexing = 'ij')
indB=np.logical_and(i%20<10, j%20<10)
indJ=np.logical_and(i%20>9, j%20>9)
R[indJ, :]=[0,0,0]
R[indB, :]=[0,0,0]
#print([carres]*carres)

# visualisation avec imshow
plt.imshow(R)
#plt.show() # inutile en interactif
#
# Sauvegarde avec imsave

