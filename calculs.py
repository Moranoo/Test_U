import csv

def lire_csv(fichier):
    with open(fichier, mode='r') as f:
        reader = csv.DictReader(f)
        return [ligne for ligne in reader]
    



def additionner(a, b):
    return a + b
