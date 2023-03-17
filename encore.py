from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy.special as sp

tacheDiffraction = Image.open("disque1mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")
data = np.asarray(tacheDiffractionGris)
hauteur = data.shape[0]
longueur = data.shape[1]
DimensionFente =  1*10**(-3)

tailleCache = 25

#plt.imshow(tacheDiffractionGris)

MAX = np.where(data == np.max(data))[0][0]

#Crééer un cache

cacheImage = data[MAX - tailleCache // 2 : MAX + tailleCache // 2 + 1, :]


valeurPixel = np.mean(cacheImage, axis=0)
listeNumero = np.linspace(0, longueur, longueur)
L = []
EPSILON = []

for elt in listeNumero:
    L.append(DimensionFente*5.3*10**(-6)/(632.8*10**(-9)*80*10**(-2)))

J1=sp.jn(1,L)

for i in range(len(J1)):
    EPSILON.append((J1[i]/(L[i]*m.pi)**2))



#plt.plot(L, valeurPixel)
plt.plot(L, J1, label="Bessel")
plt.legend()
plt.title("Valeurs du niveau de gris des pixels")
plt.xlabel("Pixels n")
plt.ylabel("Niveau de gris")
plt.show()
