Ce projet implémente une pipeline simple en Python pour traiter un ensemble d'images en les redimensionnant et en ajoutant un remplissage (padding) pour obtenir un format carré. Chaque exécution de la pipeline sauvegarde les images traitées dans un dossier horodaté unique sous datasets/.

Structure du Projet
graphql
Copier le code
project_root/
│
├── input_images/         # Dossier contenant les images brutes à traiter
├── datasets/             # Dossier de sortie contenant un sous-dossier horodaté pour chaque exécution
│   └── <horodatage>/     # Sous-dossier avec les images traitées de chaque exécution
│
├── src/
│   ├── main.py           # Point d'entrée du script
│   └── image_processor.py # Contient la classe ImageProcessor pour le traitement d'images
│
└── README.md             # Documentation du projet
Fonctionnalités
Redimensionnement : Chaque image est redimensionnée en gardant son ratio d'origine.
Remplissage (Padding) : Si l'image n'est pas carrée, un remplissage est ajouté pour obtenir une taille carrée. La couleur de remplissage par défaut est (114, 114, 144).
Dossier de sortie horodaté : Les images traitées sont stockées dans un sous-dossier horodaté unique dans datasets/, ce qui permet de conserver les résultats de chaque exécution.
Prérequis
Python 3.x
Bibliothèques Python : Pillow
Pour installer les dépendances, utilisez :

bash
Copier le code
pip install -r requirements.txt
Utilisation
Placez vos images brutes dans le dossier input_images/.
Lancez le script principal :
bash
Copier le code
python src/main.py
Les images traitées seront sauvegardées dans datasets/<horodatage>/.
Personnalisation
Dans main.py, vous pouvez :

Modifier la taille de sortie des images en ajustant le paramètre target_size (par défaut : 640).
Spécifier un autre dossier de sortie en changeant le paramètre output_root.
