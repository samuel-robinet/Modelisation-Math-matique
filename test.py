import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

# definition des couleurs utilisees, codees en R, V, B
blanc = np.array([255, 255, 255], dtype = np.uint8)
bleu = np.array([0, 0, 255], dtype = np.uint8)
rouge = np.array([255, 0, 0], dtype = np.uint8)

# Initialisation de l'image. On pourrait aussi creer les 3 plans R, V, B
# et les empiler ensuite avec la fonction stack.
tcheque = np.zeros((100, 150, 3), dtype = np.uint8)
#
# Creation des matrices d'indices lignes et colonnes (deja vu)
I, J = np.meshgrid(\
                    np.arange(100, dtype=np.int64),\
                    np.arange(150, dtype = np.int64),\
                    indexing = 'ij')
#
# Affectation des couleurs en respectant les conditions :
tcheque[0:50,:,:]=255
tcheque[50:100,:,:]=[255,0,0]
tcheque[np.logical_and(J<=I, I <= 100 - J)] = bleu


#
# Voila le resultat :
plt.imshow(tcheque)
plt.show() # inutile en interactif
#
# ca merite une sauvegarde :
mpg.imsave('tcheque.png', tcheque)