import os, time


def lire_liste():
    with open('produit.txt', 'r',encoding='utf-8') as fichier:
            f = fichier.readlines()
            for ligne in f:
                a = ligne.split(",")
                print('NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])


def ajouter_produit():
    inputuser=input("Ajouter un produit :")
    with open('produit.txt', 'a',encoding='utf-8') as fichier:
        if not inputuser:
            print("Erreur, le champ est vide")
            inputuser=input("Ajouter un produit :")
        else:
            fichier.write('\n')
            fichier.write(inputuser)


def supprimer_produit():
    input_recherche = input("Entrez le nom du produit à supprimer : ")
    with open('produit.txt', 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    nouvelles_lignes = []
    produit_supprime = False

    for ligne in lignes:
        a = ligne.split(",")
        if input_recherche.lower() == a[0].lower():
            produit_supprime = True 
            print(f"Produit supprimé : {a[0]} , PRIX : {a[1]} , QUANTITE : {a[2]}")
        else:
            nouvelles_lignes.append(ligne)

    if produit_supprime:
        with open('produit.txt', 'w', encoding='utf-8') as fichier:
            fichier.writelines(nouvelles_lignes)
        print("Le produit a été supprimé avec succès.")
    else:
        print("Aucun produit trouvé avec ce nom.")





def rechercher_produit():
    i=0
    print("1) Recherche séquentielle")
    print("2) Recherhce dichotomique")
    answer = int(input("Choisir une option : "))

    if answer==1:

        input_recherche=str(input("produit a rechercher : "))
        with open('produit.txt', 'r',encoding='utf-8') as fichier:
            f = fichier.readlines()
            for ligne in f:
                i=i+1
                a = ligne.split(",")
                if input_recherche.lower()==a[0].lower():
                    print('ID :',i,', NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])


    elif answer == 2:
        liste = []
        input_recherche = str(input("Produit à rechercher : "))
        
        with open('produit.txt', 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()
            
            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = a[1].strip()
                produit_quantite = a[2].strip()
                liste.append((produit_nom, produit_prix, produit_quantite))
        liste.sort()
        r = -1
        g = 0
        d = len(liste) - 1
        while g <= d and r == -1:
            c = (g + d) // 2
            if liste[c][0] < input_recherche:
                g = c + 1
            elif liste[c][0] > input_recherche:
                d = c - 1
            else:
                r = c


        if r != -1:
            print('ID :',r+1,', NOM :',input_recherche,', PRIX :',liste[r][1],', QUANTITE :',liste[r][2])
        else:
            print(f"Le produit '{input_recherche}' n'a pas été trouvé.")


