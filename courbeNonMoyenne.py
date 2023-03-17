from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

tacheDiffraction = Image.open("disque1mm.png")

tacheDiffractionGris = tacheDiffraction.convert("L")
data = np.asarray(tacheDiffractionGris)
hauteur = data.shape[0]
longueur = data.shape[1]

#plt.imshow(tacheDiffractionGris)

MAX = np.where(data == np.max(data))[0][0]

#On récupère les pixels de la ligne L
valeurPixel = data[MAX]
listeNumero = np.linspace(0, longueur, longueur)

plt.plot(listeNumero, valeurPixel)
plt.title("Valeurs du niveau de gris des pixels")
plt.xlabel("Pixels n")
plt.ylabel("Niveau de gris")
plt.plot()
