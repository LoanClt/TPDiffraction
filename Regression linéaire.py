from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

taillePixel = 5.3*10**(-6)
D = 107*10**(-2)
a = 1*10**(-3) #diamètre de la pupille ET PAS LE RAYON, VERIFIER DANS CR
LAMBDA = 632.8*10**(-9)
ALPHA =((np.pi * a)/(LAMBDA*D)) #cf commentaire d'après pour l'explication sur ce alpha

a = [1,
     2,
     3,
     5,
     10,
     20]

phi = [0.0018202576451612892,
       0.0008822576612903227,
       0.0005823981935483873,
       0.0003637919999999999,
       0.00016129032258064505,
       0.00013064516129032266]

phiInverse = list(map(lambda elt: 1 / elt, phi))

fit = np.polyfit(a, phiInverse, 1)

x = np.linspace(1, 20, 1000)
def droite(x, fit):
    return fit[0]*x + fit[1]

plt.scatter(a, phiInverse)
plt.plot(x, droite(x, fit), label = "Régréssion linéaire")
plt.xlabel(r"$a$ en mm")
plt.ylabel(r"1/phi")
plt.legend()
plt.show()
