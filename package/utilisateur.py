import mysql.connector
import tkinter as tk
from tkinter import messagebox

class Utilisateur:
    def __init__(self, id_utilisateur, email, nom, prenom, mdp, role_id):
        self.id_utilisateur=id_utilisateur
        self.email=email
        self.nom=nom
        self.prenom=prenom
        self.mdp=mdp
        self.role_id=role_id
        
    
    # methodes
    def login(email, mdp):
        # Établir la connexion à la base de données
        pass
    
    def ajouter_utilisateur():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    email = entry_email.get()
    mot_de_passe = entry_mot_de_passe.get()

    try:
        # Connexion à la base de données MySQL (ajustez les paramètres selon votre cas)
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port="8889",
            user="root",
            password="root",
            database="BlogBdd"
        )
        cursor = conn.cursor()

        # Exécution de la requête SQL pour ajouter un utilisateur
        cursor.execute("INSERT INTO Utilisateur (nom, prenom, email, mdp, id_role) VALUES (%s, %s, %s, %s, %s)",
                       (nom, prenom, email, mot_de_passe, 2))  # Supposons que le rôle "Utilisateur" a l'ID 2

        # Validation de la transaction et fermeture de la connexion
        conn.commit()
        conn.close()

        # Effacer les champs après l'ajout
        entry_nom.delete(0, tk.END)
        entry_prenom.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_mot_de_passe.delete(0, tk.END)

        messagebox.showinfo("Succès", "Utilisateur ajouté avec succès!")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'ajout de l'utilisateur : {str(e)}")
        
        
        
    # def write_comment():
    # def like():
    # def write_article():
    # def logout():

    
        
    
    
