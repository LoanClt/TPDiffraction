from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

tacheDiffraction = Image.open("disque2mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")

plt.imshow(tacheDiffractionGris)
plt.show()
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
#1,22a/lambda = phi/2D

plt.plot(listeYCentree, valeurPixel)
plt.title("Valeurs du niveau de gris des pixels")
plt.xlabel("Position sur l'écran")
plt.ylabel("Niveau de gris")
plt.xlim([-0.0005, 0.0005])
minima = plt.ginput(2)
plt.show()
phiDisque = np.abs((minima[0][0]-minima[1][0])*10**(-6))
print(phiDisque*10**(6))


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

print(phiInverse)

fit = np.polyfit(a, phiInverse, 1)
fit_reel = [1/(LAMBDA/(2.44*D))*10**(-4), fit[1]]

print(1/(LAMBDA/(2.44*D))*10**(-4))
print(fit)

#1,22lambda/a = phi/2D
#a = lambda*phi/2,44*D
#phi = 2,44*D/lambda

x = np.linspace(1, 20, 1000)
def droite(x, fit):
    return fit[0]*x + fit[1]

def droite_reel(x, fit_reel):
    return fit_reel[0]*x + fit_reel[1]

plt.scatter(a, phiInverse)
plt.plot(x, droite(x, fit), label = "Régréssion linéaire")
plt.plot(x, droite_reel(x, fit_reel), label = "Polynôme réel")
plt.xlabel(r"$a$ en mm")
plt.ylabel(r"1/phi")
plt.legend()
#plt.show()
