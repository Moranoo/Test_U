from calculs import additionner;

from calculs import lire_csv;

import io; # io est pour les entrées/sorties de données provenant de fichiers ici le fichier csv

from unittest import mock;# il simule les entrées/sorties de données provenant de fichiers ici le fichier csv

def test_lire_csv():
    donnees_moquees = io.StringIO("nom,age\nAlice,30\nBob,25\n")# ici on crée un fichier csv avec des données qui devront representées les données du fichier csv
    
    with mock.patch('builtins.open', return_value=donnees_moquees):# ici on simule l'ouverture du fichier csv avec les données moquées
        resultat = lire_csv("faux_fichier.csv")#ici on appelle la fonction lire_csv avec le fichier csv moqué 
        assert resultat == [
            {'nom': 'Alice', 'age': '30'},
            {'nom': 'Bob', 'age': '25'}
        ]


def test_additionner():
    assert additionner(2,2) == 4