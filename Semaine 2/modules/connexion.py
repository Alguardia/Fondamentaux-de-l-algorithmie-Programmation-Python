import os
import csv
from tabulate import tabulate
import pandas as pd


def register():
    username = input("Mettre votre nom : ")
    password = input("Mettre votre mot de passe : ")
    nom_fichier = f"{username}.csv"
    chemin_fichier = os.path.join('data', nom_fichier)

    user_data = [[username, password]]



    df = pd.read_csv('data/user.csv')
    df_new = pd.DataFrame(user_data, columns=['username', 'password'])
    df_combined = pd.concat([df, df_new], ignore_index=True)
    df_combined.to_csv('data/user.csv', index=False)

    print(f"Utilisateur {username} enregistré avec succès !")

    df_produit = pd.DataFrame(columns=['NOM', 'PRIX', 'QUANTITE'])
    df_produit.to_csv(chemin_fichier, index=False)

    input("Appuyez sur une touche pour continuer...")



def verifier_utilisateur(username, password):
    df = pd.read_csv('data/user.csv')
    filtered_df = df.loc[(df['username'] == username) & (df['password'] == password)]
    if filtered_df.empty: 
        print("Aucun élément trouvé.") 
        return False
    else: 
        print("Éléments trouvés :") 
        print(filtered_df)
        return True

def login(username, password):
    if verifier_utilisateur(username, password):
        print("Connexion réussie !")
        return True
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")
        input('')
        return False




def supprimer_user():
    username = input("Entrez votre nom d'utilisateur : ").strip()
    password = input("Entrez votre mot de passe : ").strip()


    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)

    filtered_df = df.loc[~((df['username'] == username) & (df['password'] == password))]


    if len(filtered_df) < len(df):
     
        filtered_df.to_csv(user_csv_path, index=False)
        print(f"Utilisateur {username} supprimé avec succès.")

        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
            print(f"Le fichier CSV '{nom_fichier}' a été supprimé.")
    else:
        print("Aucun utilisateur trouvé avec ce nom et ce mot de passe.")

    input("Appuyez sur une touche pour continuer...")



def liste_commercants():

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    commercants = df['username'].tolist()
    print("Liste des commerçants :")
    for commercant in commercants:
        print(f"- {commercant}")

    input("Appuyez sur une touche pour continuer...")
