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
    username = input("Entrez votre nom d'utilisateur : ").strip()  # Supprimer les espaces autour de l'entrée
    password = input("Entrez votre mot de passe : ").strip()  # Supprimer les espaces autour de l'entrée
    nouvelles_lignes = []
    utilisateur_supprime = False

    with open('user.csv', 'r', encoding='utf-8') as fichier:
        utilisateurs = fichier.readlines()

        for utilisateur in utilisateurs:
            # Assurez-vous que chaque ligne est bien formatée
            nom, mot_de_passe = utilisateur.strip().split(',')
            nom = nom.strip()  # Supprimer les espaces autour du nom d'utilisateur
            mot_de_passe = mot_de_passe.strip()  # Supprimer les espaces autour du mot de passe
           

            # Comparer sans espaces
            if nom == username and mot_de_passe == password:
                utilisateur_supprime = True 
                print(f"Utilisateur supprimé : {nom}")
                # Ne pas ajouter cet utilisateur à nouvelles_lignes
            else:
                nouvelles_lignes.append(utilisateur.strip())  # Ajouter la ligne sans espaces

    if utilisateur_supprime:
        with open('user.csv', 'w', encoding='utf-8') as fichier:
            fichier.writelines(nouvelles_lignes)  # Écrire uniquement les utilisateurs restants
        
        # Supprimer le fichier CSV associé à l'utilisateur
        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('liste_produit', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
            print(f"Le fichier CSV '{nom_fichier}' a été supprimé.")
        
        print("L'utilisateur a été supprimé avec succès.")
        input("Appuyez sur une touche pour continuer...")
    else:
        print("Aucun utilisateur trouvé avec ce nom.")
        input("Appuyez sur une touche pour continuer...")