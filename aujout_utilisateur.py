import tkinter as tk
from tkinter import messagebox
import mysql.connector

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

# Créer la fenêtre principale
root = tk.Tk()
root.title("Ajouter un utilisateur")

# Créer les widgets
label_nom = tk.Label(root, text="Nom:")
label_prenom = tk.Label(root, text="Prénom:")
label_email = tk.Label(root, text="Email:")
label_mot_de_passe = tk.Label(root, text="Mot de passe:")

entry_nom = tk.Entry(root)
entry_prenom = tk.Entry(root)
entry_email = tk.Entry(root)
entry_mot_de_passe = tk.Entry(root, show="*")

button_ajouter = tk.Button(root, text="Ajouter Utilisateur", command=ajouter_utilisateur)

# Placer les widgets dans la fenêtre
label_nom.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_prenom.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_mot_de_passe.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_nom.grid(row=0, column=1, padx=10, pady=5)
entry_prenom.grid(row=1, column=1, padx=10, pady=5)
entry_email.grid(row=2, column=1, padx=10, pady=5)
entry_mot_de_passe.grid(row=3, column=1, padx=10, pady=5)

button_ajouter.grid(row=4, column=0, columnspan=2, pady=10)

# Lancer la boucle principale
root.mainloop()
