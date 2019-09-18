import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg


R = 255 * np.ones((60, 256, 3), dtype = np.uint8)
i, j = np.meshgrid(\
                    np.arange(60, dtype=np.int64),\
                    np.arange(256, dtype = np.int64),\
                    indexing = 'ij')

#test=np.linspace(1,256,60*256,dtype=np.uint8)
#print(test)
#test1=test.reshape((256,60))
#test1=np.rot90(test,-1)
#print(test1)

# visualisation avec imshow
plt.imshow(R)
#plt.show() # inutile en interactif
#
# Sauvegarde avec imsave
#mpg.imsave('carres3.png', carres)
