import os
from fonction import *
from connexion import *
import pwnedpasswords
password=""
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

while True:
    os.system("cls") 

    print("1) Login")
    print("2) Register")
    print("3) Delete")
    answer=int(input("Choisir une option : "))

    if answer==1:
        username = input("Entrez votre nom d'utilisateur : ")
        password = input("Entrez votre mot de passe : ")
        if login(username,password):

            os.system("cls")
            
            print("Votre mot de passe a été compromis !\nNombre de fois compromis : ", pwnedpasswords.check(password) )
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
                trier_produit()
                input ("")
                os.system("cls")


    if answer==2:
        register()

    if answer==3:
        supprimer_user()
        
