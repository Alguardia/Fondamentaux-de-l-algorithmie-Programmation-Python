import os
import csv

def register():
    username=input("mettre votre nom :")
    password=input("mettre votre mdp :")
    nom_fichier = f"{username}.csv" 
    chemin_fichier = os.path.join('liste_produit', nom_fichier)

    with open('user.csv', 'a', encoding='utf-8') as fichier: 
        fichier.write(f"\n{username},{password}")
        print(f"Utilisateur {username} enregistré avec succès !")

    with open(chemin_fichier, 'w', newline='', encoding='utf-8') as fichier_csv: 
        writer = csv.writer(fichier_csv) 
        writer.writerow(['nom', 'prix', 'quantite']) 
       

    input("")


def verifier_utilisateur(username, password):
    with open('user.csv', 'r', encoding='utf-8') as fichier:
        utilisateurs = fichier.readlines()
        
        for utilisateur in utilisateurs:
            nom, mot_de_passe = utilisateur.strip().split(',')
            if nom == username and mot_de_passe == password:
                return True
    return False


def login(username,password):
    
    if verifier_utilisateur(username, password):
        print("Connexion réussie !")
        return True
        
        
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")
        input('')
        return False


def supprimer_user():
    global mot_de_passe
    username = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")
    nouvelles_lignes = []
    produit_supprime = False
    with open('user.csv', 'r', encoding='utf-8') as fichier:
        utilisateurs = fichier.readlines()

        for utilisateur in utilisateurs:
            nom, mot_de_passe = utilisateur.strip().split(',')
            if nom == username and mot_de_passe == password:
                produit_supprime = True 
                
            else:
                nouvelles_lignes.append(utilisateur)

        if produit_supprime:
            with open('user.csv', 'w', encoding='utf-8') as fichier:
                fichier.writelines(nouvelles_lignes)
            print("L'utilisateur a été supprimé avec succès.")
            input("")
            return mot_de_passe
        else:
            print("Aucun utilisateur trouvé avec ce nom.")
            input("")

