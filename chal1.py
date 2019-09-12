import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg
import os

# On prepare les trois matrices a empiler
R =255* np.ones((10,100), dtype=np.uint8) #im=255*ones((100,10,3), dtype=np.uint8)
V =255* np.ones((10,100), dtype=np.uint8)
B =255* np.ones((10,100), dtype=np.uint8)

R[5:10,0:100]=0
V[5:10,0:100]=0
B[5:10,0:100]=0

R = np.vstack((R,R,R,R,R))
V = np.vstack((V,V,V,V,V))
B = np.vstack((B,B,B,B,B))
# Pour l'instant, la superposition donnerait du blanc.# On mets a 0 les 100 premieres lignes de chacune des matrices

print(R)
# On empile les trois matrice
carres = np.stack((R, V, B), axis =2)


os.chdir("../")

# visualisation avec imshow
plt.imshow(carres)
plt.show() # inutile en interactif

# Sauvegarde avec imsave
mpg.imsave('carres.png', carres)

R=np.rot90(R)
V=np.rot90(V)
B=np.rot90(B) #transposition à faire 

carres2 = np.stack((R, V, B), axis =2)


os.chdir("../")

# visualisation avec imshow
plt.imshow(carres2)
plt.show() # inutile en interactif
mpg.imsave('carres1B.png', carres)