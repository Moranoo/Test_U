from calculs import additionner;
import numpy as np;
import geopandas as gpd

from calculs import lire_csv, charger_donnees, charger_shapefile;

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


# Moquer des fichiers .npy
def test_charger_donnees():
     # Simuler un tableau NumPy
    donnees_moquees = np.array([[1, 2, 3], [4, 5, 6]])

    # Moquer np.load pour qu'il retourne le tableau simulé
    with mock.patch('numpy.load', return_value=donnees_moquees):
        resultat = charger_donnees("fichier_fictif.npy")

# Moquer des fichdef test_charger_shapefile():
    # Simuler un GeoDataFrame
    donnees_moquees = gpd.GeoDataFrame({
        'nom': ['PointA', 'PointB'],
        'geometry': [None, None]  # Normalement, il y aurait de la géométrie ici
    })

    # Moquer gpd.read_file pour qu'il retourne le GeoDataFrame simulé
    with mock.patch('geopandas.read_file', return_value=donnees_moquees):
        resultat = charger_shapefile("fichier_fictif.shp")
        assert resultat.equals(donnees_moquees)
