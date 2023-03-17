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



\begin{figure}[!htb]
   \begin{minipage}{0.65\textwidth}
     \centering
     \includegraphics[width=.5\linewidth]{disque1mm}
     \caption{Disque à $a = 1$mm}\label{Fig:Data1}
   \end{minipage}\hfill
   \begin{minipage}{0.45\textwidth}
     \centering
     \includegraphics[width=0.7\linewidth]{disque2mm}
     \caption{Disque à $a = 2$mm}\label{Fig:Data2}
   \end{minipage}
\end{figure}

\begin{figure}[!htb]
   \begin{minipage}{0.65\textwidth}
     \centering
     \includegraphics[width=.5\linewidth]{disque3mm}
     \caption{Disque à $a = 3$mm}\label{Fig:Data1}
   \end{minipage}\hfill
   \begin{minipage}{0.45\textwidth}
     \centering
     \includegraphics[width=0.7\linewidth]{disque5mm}
     \caption{Disque à $a = 5$mm}\label{Fig:Data2}
   \end{minipage}
\end{figure}

\begin{figure}[!htb]
   \begin{minipage}{0.65\textwidth}
     \centering
     \includegraphics[width=.5\linewidth]{disque10mm}
     \caption{Disque à $a = 10$mm}\label{Fig:Data1}
   \end{minipage}\hfill
   \begin{minipage}{0.45\textwidth}
     \centering
     \includegraphics[width=0.8\linewidth]{disque20mm}
     \caption{Disque à $a = 20$mm}\label{Fig:Data2}
   \end{minipage}
\end{figure}

\begin{figure}[h]
    \centering
	\includegraphics[width=1\linewidth]{histo2mmDisque}
    \caption{Histogramme des nuances de gris pour la figure de diffraction associée au disque à  $a=2$mm }
\end{figure}
