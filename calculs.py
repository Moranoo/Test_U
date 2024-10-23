import csv
import numpy as np
import geopandas as gpd


def lire_csv(fichier):
    with open(fichier, mode='r') as f:
        reader = csv.DictReader(f)
        return [ligne for ligne in reader]

def charger_donnees(fichier):
    return np.load(fichier)

def additionner(a, b):
    return a + b

def charger_shapefile(fichier):
    return gpd.read_file(fichier)
