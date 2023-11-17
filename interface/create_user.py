import tkinter as tk
from tkinter import messagebox
import mysql.connector

from package.utilisateur import ajouter_utilisateur

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
