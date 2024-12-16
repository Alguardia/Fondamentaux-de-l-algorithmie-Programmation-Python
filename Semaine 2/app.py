import os
from modules.fonction import *
from modules.connexion import *
import pwnedpasswords

password = ""
is_logged_in = False

def show_menu():
    global answer
    print("|############################################################|")
    print("|                          Produit                           | ")
    print("|############################################################|")
    print("")
    print("1) Lire la liste")
    print("2) Ajouter un produit")
    print("3) Supprimer un produit")
    print("4) Rechercher")
    print("5) Trier")
    print("6) Déconnexion")
    answer = int(input("Choisir une option : "))
    os.system("cls")
    return answer

while True:
    os.system("cls") 

    if not is_logged_in:
        print("1) Login")
        print("2) Register")
        print("3) Delete")
        answer = int(input("Choisir une option : "))

        if answer == 1:
            username = input("Entrez votre nom d'utilisateur : ")
            password = input("Entrez votre mot de passe : ")
            if login(username, password):
                os.system("cls")
                is_logged_in = True
            else:
                print("Échec de la connexion. Veuillez réessayer.")
                input("Appuyez sur une touche pour continuer...")

        elif answer == 2:
            register()

        elif answer == 3:
            supprimer_user()

    else:
        print("Votre mot de passe a été compromis !\nNombre de fois compromis : ", pwnedpasswords.check(password))
        answer = show_menu()

        
        if answer == 1:
            lire_liste()
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")

        elif answer == 2:
            ajouter_produit()
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")    

        elif answer == 3:
            supprimer_produit()
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")       

        elif answer == 4:
            rechercher_produit()
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")        

        elif answer == 5:
            trier_produit()
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")

        elif answer == 6: 
            is_logged_in = False 
            print("Vous êtes déconnecté.")
            input("Appuyez sur une touche pour continuer...")