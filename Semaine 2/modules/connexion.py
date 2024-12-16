import os
import csv
from tabulate import tabulate

def register():
    username=input("mettre votre nom :")
    password=input("mettre votre mdp :")
    nom_fichier = f"{username}.csv" 
    chemin_fichier = os.path.join('data', nom_fichier)

    with open('data/user.csv', 'a', encoding='utf-8') as fichier: 
        fichier.write(f"\n{username},{password}")
        print(f"Utilisateur {username} enregistré avec succès !")


    with open(chemin_fichier, 'w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(['NOM', 'PRIX', 'QUANTITE'])

    input("")




def verifier_utilisateur(username, password):
    with open('data/user.csv', 'r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False






def login(username, password):
    if verifier_utilisateur(username, password):
        print("Connexion réussie !")
        return True
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")
        input('')
        return False




def supprimer_user():
    global mot_de_passe
    username = input("Entrez votre nom d'utilisateur : ").strip()
    password = input("Entrez votre mot de passe : ").strip()
    nouvelles_lignes = []
    utilisateur_supprime = False

    with open('data/user.csv', 'r', encoding='utf-8') as fichier:
        utilisateurs = fichier.readlines()

        for utilisateur in utilisateurs:
            
            nom, mot_de_passe = utilisateur.strip().split(',')
            nom = nom.strip()  
            mot_de_passe = mot_de_passe.strip()  
           

      
            if nom == username and mot_de_passe == password:
                utilisateur_supprime = True 
                print(f"Utilisateur supprimé : {nom}")
               
            else:
                nouvelles_lignes.append(utilisateur.strip())  

    if utilisateur_supprime:
        with open('data/user.csv', 'w', encoding='utf-8') as fichier:
            for i, utilisateur in enumerate(nouvelles_lignes):
                if i < len(nouvelles_lignes) - 1:
                    fichier.write(utilisateur + "\n")
                else:
                    fichier.write(utilisateur)
        
        
        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
            print(f"Le fichier CSV '{nom_fichier}' a été supprimé.")
        
        print("L'utilisateur a été supprimé avec succès.")
        input("Appuyez sur une touche pour continuer...")
    else:
        print("Aucun utilisateur trouvé avec ce nom.")
        input("Appuyez sur une touche pour continuer...")


def liste_commercants():
    commercants=[]
    with open('data/user.csv', 'r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier)
        next(reader)
        for row in reader:
            commercants.append(row[0])


    print("Liste des commerçants :") 
    for commercant in commercants: 
        print(f"- {commercant}")
    input("Appuyez sur une touche pour continuer...")