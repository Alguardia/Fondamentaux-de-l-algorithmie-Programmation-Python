import pandas as pd


def register():
    username=input("mettre votre nom :")
    passwd=input("mettre votre mdp :")

    with open('user.csv', 'a', encoding='utf-8') as fichier: 
        fichier.write(f"\n{username},{passwd}")
        print(f"Utilisateur {username} enregistré avec succès !")

    input("")


def verifier_utilisateur(username, password):
    with open('user.csv', 'r', encoding='utf-8') as fichier:
        utilisateurs = fichier.readlines()
        
        for utilisateur in utilisateurs:
            nom, mot_de_passe = utilisateur.strip().split(',')
            if nom == username and mot_de_passe == password:
                return True
    return False


def login():

    username = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")

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

