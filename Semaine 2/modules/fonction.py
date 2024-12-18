import os
from tabulate import tabulate
import csv
import pandas as pd

def lire_liste(chemin_fichier):
    produit=[]
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        data = csv.reader(fichier)
   
        for liste in data:
            produit.append(liste)        

    print(tabulate(produit, tablefmt="grid"))


def ajouter_produit(chemin_fichier):
    print("Ajouter un produit :")
    inputusernom=input("Nom du produit :")
    inputuserprix=input("Prix du produit :")
    inputuserquantite=input("Quantité du produit :")

    with open(chemin_fichier, 'a',encoding='utf-8') as fichier:
        if not  inputusernom or not inputuserprix or not  inputuserquantite:
            print("Erreur, le champ est vide")
            inputusernom=input("Nom du produit :")
            inputuserprix=input("Prix du produit :")
            inputuserquantite=input("Quantité du produit :")
            
        else:
            fichier.write('\n')
            fichier.write(inputusernom +','+ inputuserprix + ',' +  inputuserquantite)


def supprimer_produit(chemin_fichier):
    input_recherche = input("Entrez le nom du produit à supprimer : ")
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    nouvelles_lignes = []
    produit_supprime = False

    for ligne in lignes:
        a = ligne.split(",")
        if input_recherche.lower() == a[0].lower():
            produit_supprime = True 
            print(f"Produit supprimé : {a[0]} , PRIX : {a[1]} , QUANTITE : {a[2]}")
        else:
            nouvelles_lignes.append(ligne.strip())

    if produit_supprime:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            for i, ligne in enumerate(nouvelles_lignes):
                if i < len(nouvelles_lignes) - 1:
                    fichier.write(ligne + "\n")
                else:
                    fichier.write(ligne)
            
        print("Le produit a été supprimé avec succès.")
    else:
        print("Aucun produit trouvé avec ce nom.")





def rechercher_produit(chemin_fichier):
    i=0
    print("1) Recherche séquentielle")
    print("2) Recherhce dichotomique")
    answer = int(input("Choisir une option : "))



    if answer==1:
        verif=False
        os.system("cls")
        print("1) Recherche séquentielle : ")
        input_recherche=str(input("produit a rechercher : "))
        df = pd.read_csv(chemin_fichier)
        filtered_df = df.loc[df['NOM'].str.contains(input_recherche)]
        if filtered_df.empty: 
            print(f"Le produit '{input_recherche}' n'a pas été trouvé.")
            return False
        else: 
            print("Éléments trouvés :") 
            print(filtered_df)
            return True

        

    elif answer == 2:
        os.system("cls")
        print("2) Recherhce dichotomique : ")
        liste = []
        input_recherche = str(input("Produit à rechercher : "))
        
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()
            
            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = a[1].strip()
                produit_quantite = a[2].strip()
                liste.append((produit_nom, produit_prix, produit_quantite))
        liste.sort()
        indice = -1
        min = 0
        max = len(liste) - 1
        while min <= max and indice == -1:
            moy = (min + max) // 2
            if liste[moy][0] < input_recherche:
                min = moy + 1
            elif liste[moy][0] > input_recherche:
                max = moy - 1
            else:
                indice = moy


        if indice != -1:
            print('ID :',indice+1,', NOM :',input_recherche,', PRIX :',liste[indice][1],', QUANTITE :',liste[indice][2])
        else:
            print(f"Le produit '{input_recherche}' n'a pas été trouvé.")






def trier_produit(chemin_fichier):
    i=0
    print("1) Tri par sélection par nom")
    print("2) Tri à bulles par prix ")
    print("3) Tri rapide par quantité")
    answer = int(input("Choisir une option : "))

    if answer == 1:
        os.system("cls")
        print("1) Tri par nom : ")
    
        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="NOM")
        print(df_sorted)
	




         


    if answer == 2:
        os.system("cls")
        print("2) Tri par prix : ")
    

        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="PRIX")
        print(df_sorted)
	

    if answer == 3:
        os.system("cls")
        print("3) Tri par quantité :")
        liste = []

        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="QUANTITE")
        print(df_sorted)
	