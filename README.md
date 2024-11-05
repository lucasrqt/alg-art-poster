# Algorithmic Art Poster Contest

This repository contains my work for the [contest of algorithmic art](https://www.bdepalme.fr/2024/09/22/poster.html) of the **[Palme association](https://www.bdepalme.fr)** (association of Computer Science students of ISTIC, University of Rennes).

## Résumé (en FR)

### Créateur·ice

**Esther Pytlak**

### Démarche (en 61 mots)

Ma volonté principale pour ce concours était de créer un poster "psychédélique" (style que j'affectionne énormément). Plutôt que de générer des formes, j'ai trouvé plus intéressant de combiner cela avec des images. En combinant des formes et couleurs pyschédéliques et une image en fond, cela crée une perspective très intéressante, laissant libre cours à l'imagination de l'observateur·ice vis-à-vis de la représentation.

### Explication du code

#### Manipulation d'images
Les données des images sont manipulées avec la librairie OpenCV2, qui permet d'obtenir la matrice de l'image comportant chaque pixel, de jouer avec les modes de couleur, etc.

Ces données nous servent à avoir la taille de l'image et donc de soit pouvoir :
- manipuler les pixels et créer des effets dessus
- soit obtenir la taille de l'image afin de générer un masque psychédélique

#### Génération de l'effet
L'effet psychédélique est généré à l'aide du *Perlin Noise*, permettant de créer des zones qui ont l'air d'être aléatoires. Selon les différentes zones, nous pouvons leur donner une couleur unique et donc génrer un effet psychédélique avec énormément de couleurs et de formes. Nous pouvons jouer avec beaucoup de paramètres afin d'avoir différents rendu.

#### Exportation du résultat
Après la modification, l'image modifiée est ensuite ouverte avec la librairie PIL pour faire une interpollation (augmenter la résolution de l'image), afin qu'elle soit en 300 DPI pour être imprimée.

### Structure du projet

#### Arborescence du projet
```
.
├── README.md
├── ascii_art.html
├── data
│   ├── me.jpg
│   ├── me2.jpg
│   ├── me_darkened_background.jpg
│   ├── psychedelic_cherry_tree_1.jpg
│   ├── psychedelic_cherry_tree_1.pdf
├── notebook.ipynb
└── requirements.txt
```

#### Explication
- `README.md` : ce fichier avec les explications
- `acii_art.html`: test d'un ASCII art à partir d'une image
- `requirements.txt` : modules pythons utilisés pour ce projet
- `notebook.ipynb` : notebook python contenant le code source du projet
- `data/` : répoertoire contenant les images sources et les résultats produits par le notebook
- **`psychedelic_cherry_tree_1.{jpg, pdf}` : RENDU FINAL DU POSTER** (en pdf et jpg)

## Installation

1. Create the virtual env. (see python doc, depends on the os)
2. Activate the virtual env.
3. Install the requierements :
```bash
pip install -r requirements.txt
```

## Play with the notebook

Everything is in the notebook `notebook.ipynb`.

### Steps

The goal is to get an image modified to get a psychedelic effect on it.

To do so I manipulate the images with the library opencv and I apply effects on it with numpy functions and the packages noise that provides useful functions to apply generative effects.
