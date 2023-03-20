from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

tacheDiffraction = Image.open("disque1mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")
data = np.asarray(tacheDiffractionGris)
hauteur = data.shape[0]
longueur = data.shape[1]

taillePixel = 5.3*10**(-6)
D = 80*10**(-2)
a = 1*10**(-3) #diamètre de la pupille ET PAS LE RAYON, VERIFIER DANS CR
LAMBDA = 632.8*10**(-9)
ALPHA =((np.pi * a)/(LAMBDA*D)) #cf commentaire d'après pour l'explication sur ce alpha

tailleCache = 25

maxHauteur = np.where(data == np.max(data))[0][0]
maxLongueur = np.where(data == np.max(data))[1][0]

#Crééer un cache
cacheImage = data[maxHauteur - tailleCache // 2 : maxHauteur + tailleCache // 2 + 1, :]
# Moyenne sur un certain nombre de lignes
valeurPixel = np.mean(cacheImage, axis=0) #/np.max(np.mean(cacheImage, axis=0)) #courbe moyennée
valeurPixel = valeurPixel - min(valeurPixel)

listeNumero = np.linspace(0, longueur, longueur) #[0, 1, 2, ..., n]
listeY = np.array(list(map(lambda x: x*taillePixel, listeNumero))) #on veut l'abcisse y sur l'axe, je tranforme en micromètre
listeYCentree = np.array(list(map(lambda x: x - maxLongueur*taillePixel, listeY))) #bessel a un max en 0, je centre le max de ma tache en 0
listeYA = np.array(list(map(lambda x: ((x*taillePixel) - maxLongueur*taillePixel)*ALPHA, listeNumero)))

EPSILON = []
J1 = sp.j1(listeYA)
EPSILON = np.abs(2*J1/(listeYA))**2

max_value = np.max(valeurPixel)

plt.figure()
plt.plot(listeYCentree, valeurPixel, label="Courbe centrée")
plt.plot(listeYCentree, max_value*EPSILON, label="|J1(pi*x)/pi*x|²")
plt.legend()
plt.title("Valeurs du niveau de gris des pixels normalisée à l'unitée")
plt.xlabel("Position (micromètre)")
plt.ylabel("Niveau de gris")
plt.show()
