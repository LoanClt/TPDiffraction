from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

tacheDiffraction = Image.open("disque1mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")
data = np.asarray(tacheDiffractionGris)
hauteur = data.shape[0]
longueur = data.shape[1]

tailleCache = 25

#plt.imshow(tacheDiffractionGris)

MAX = np.where(data == np.max(data))[0][0]

#Crééer un cache

cacheImage = data[MAX - tailleCache // 2 : MAX + tailleCache // 2 + 1, :]


valeurPixel = np.mean(cacheImage, axis=0)
listeNumero = np.linspace(0, longueur, longueur)

plt.plot(listeNumero, valeurPixel)
plt.title("Valeurs du niveau de gris des pixels")
plt.xlabel("Pixels n")
plt.ylabel("Niveau de gris")
plt.plot()
