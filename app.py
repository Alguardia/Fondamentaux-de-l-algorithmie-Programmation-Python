import os, time
def show_menu():
    global answer
    print("|############################################################|")
    print("|                          Produit                           | ")
    print("|############################################################|")
    print("")
    print("")
    print("1) Lire la liste")
    print("2) Ajouter un produit")
    print("3) Supprimer un produit")
    print("4) Rechercher")
    print("5) Trier")
    
    answer = int(input("Choisir une option : "))
    os.system("cls")
    return answer

def lire_liste():
    with open('produit.txt', 'r',encoding='utf-8') as fichier:
            f = fichier.readlines()
            for ligne in f:
                a = ligne.split(",")
                print('NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])


def ajouter_produit():
    inputuser=input("Ajouter un produit :")
    with open('produit.txt', 'a',encoding='utf-8') as fichier:
        fichier.write('\n')
        fichier.write(inputuser)


def rechercher_produit():
    input_recherche=str(input("produit a rechercher : "))
    with open('produit.txt', 'r',encoding='utf-8') as fichier:
        f = fichier.readlines()
        for ligne in f:
            a = ligne.split(",")
            if input_recherche.lower()==a[0].lower():
                print('NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])


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

def tri_produit():
    print('1) triée par prix')
    print('2) triée par quantité')
    answer = int(input("Choisir une option : "))
    if answer==1:

        with open('produit.txt', 'r',encoding='utf-8') as fichier:
            f = fichier.readlines()
            for ligne in f:
                a = ligne.split(",")
                print('NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])





while True:
    show_menu()

    if answer==1:
        lire_liste()
        input ("")
        os.system("cls")

                
    elif answer==2:
        ajouter_produit()
        input ("")
        os.system("cls")    

    elif answer==3:
        supprimer_produit()
        input ("")
        os.system("cls")       


    elif answer==4:
        rechercher_produit()
        input ("")
        os.system("cls")        


    elif answer==5:
        ajouter_produit()
        input ("")
        os.system("cls")
