# Projet de Pipeline de Traitement d'Images

Ce projet implémente une pipeline simple en Python pour traiter un ensemble d'images en les redimensionnant et en ajoutant un remplissage (padding) pour obtenir un format carré. Chaque exécution de la pipeline sauvegarde les images traitées dans un dossier horodaté unique sous `datasets/`.

## Fonctionnalités

- **Redimensionnement** : Chaque image est redimensionnée en gardant son ratio d'origine.
- **Remplissage (Padding)** : Si l'image n'est pas carrée, un remplissage est ajouté pour obtenir une taille carrée.
- **Dossier de sortie horodaté** : Les images traitées sont stockées dans un sous-dossier horodaté unique dans `datasets/`, ce qui permet de conserver les résultats de chaque exécution.

## Prérequis

- Python 3.x
- Bibliothèques Python : `Pillow , numpy , precommit , black`

Pour installer les dépendances, utilisez :

```bash
pip install -r requirements.txt
```

Utilisation
Placez vos images brutes dans le dossier input_images et lancer le script 


