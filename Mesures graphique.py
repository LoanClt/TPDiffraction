from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

tacheDiffraction = Image.open("disque3mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")
data = np.asarray(tacheDiffractionGris)
hauteur = data.shape[0]
longueur = data.shape[1]

taillePixel = 5.3*10**(-6)
D = 107*10**(-2)
a = 1*10**(-3) #diamètre de la pupille ET PAS LE RAYON, VERIFIER DANS CR
LAMBDA = 632.8*10**(-9)
ALPHA =((np.pi * a)/(LAMBDA*D)) #cf commentaire d'après pour l'explication sur ce alpha

tailleCache = 25

#plt.imshow(tacheDiffractionGris)

maxHauteur = np.where(data == np.max(data))[0][0]
maxLongueur = np.where(data == np.max(data))[1][0]

#Crééer un cache

cacheImage = data[maxHauteur - tailleCache // 2 : maxHauteur + tailleCache // 2 + 1, :]


valeurPixel = np.mean(cacheImage, axis=0)
listeNumero = np.linspace(0, longueur, longueur)
listeY = np.array(list(map(lambda x: x*taillePixel, listeNumero))) #on veut l'abcisse y sur l'axe, je tranforme en micromètre
listeYCentree = np.array(list(map(lambda x: x - maxLongueur*taillePixel, listeY))) #bessel a un max en 0, je centre le max de ma tache en 0


minima = argrelextrema(valeurPixel, np.less)
print(len(minima))


plt.plot(listeYCentree, valeurPixel)
plt.title("Valeurs du niveau de gris des pixels")
plt.xlabel("Position sur l'écran")
plt.ylabel("Niveau de gris")
minima = plt.ginput(2)
plt.show()
phiDisque2 = np.abs((minima[0][0]-minima[1][0])*10**(-6)/2)
aPratique = 1.22*D*LAMBDA/phiDisque2
print(aPratique*10**(-3))
