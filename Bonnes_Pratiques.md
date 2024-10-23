## 1. Problèmes d'import lors des tests (Chemins relatifs vs absolus)

Problème : Lors de l'exécution de tests unitaires, les imports dans les fichiers de test échouent.
Cause : Tu utilises des chemins relatifs ou absolus incorrects pour importer des modules depuis d'autres parties du projet.
Solution : Utilise des imports basés sur la structure du package en te basant sur le dossier racine du projet. Si ton projet est bien structuré en packages avec __init__.py, assure-toi d'importer correctement avec des chemins relatifs ou absolus selon le cas.


````Python
# Mauvais import
from module1 import fonction1  # Cela peut échouer si tu l'exécutes depuis un autre dossier.

# Bon import (en supposant que module1.py est dans le dossier src)
from src.module1 import fonction1
````

## Astuce :
Tu peux ajouter ton dossier racine au PYTHONPATH pour t'assurer que Python sait où chercher les modules :

````bash

export PYTHONPATH="${PYTHONPATH}:/chemin/vers/projet"
````


## 2. Problèmes avec les dépendances dans les tests (Mocking nécessaire)
Problème : Ton test échoue parce qu'il essaie d'accéder à des fichiers ou à une base de données externes.
Cause : Les tests unitaires doivent être isolés, et s'ils dépendent de ressources externes comme des bases de données ou des fichiers, cela peut causer des erreurs.
Solution : Utilise des outils comme unittest.mock pour "moquer" les dépendances externes dans les tests unitaires.

Exemple :

````python
# Moquer un fichier ouvert par une fonction
from unittest import mock

def test_lire_fichier():
    with mock.patch('builtins.open', mock.mock_open(read_data="données fictives")):
        result = fonction_qui_lit_un_fichier("chemin_fictif.txt")
        assert result == "données fictives"

```
