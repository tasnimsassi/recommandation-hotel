import tkinter as tk

base_regles = {
    "emplacement": {
        "Paris": ["Hotel A", "Hotel C"],
        "Londres": ["Hotel B", "Hotel D"]
    },
    "prix": {
        100: ["Hotel B", "Hotel D"],
        150: ["Hotel A", "Hotel C"],
        200: ["Hotel A", "Hotel D"],
        250: ["Hotel B", "Hotel C"]
    },
    "activites": {
        "Piscine": ["Hotel A", "Hotel B"],
        "Spa": ["Hotel C"],
        "Centre de remise en forme": ["Hotel B", "Hotel D"],
        "Salle de jeux": ["Hotel A", "Hotel C"],
        "Randonnée": ["Hotel B", "Hotel D"]
    },
    "plats": {
        "Cuisine française": ["Hotel A"],
        "Végétarien": ["Hotel A"],
        "Cuisine anglaise": ["Hotel B"],
        "Cuisine italienne": ["Hotel C"],
        "Cuisine asiatique": ["Hotel D"]
    },
    "nature_voyage": {
        "Vacances en famille": ["Hotel A"],
        "Voyage d'affaires": ["Hotel B"],
        "Lune de miel": ["Hotel C"],
        "Aventure extrême": ["Hotel D"]
    },
    "avis": {
        4.5: ["Hotel A"],
        3.8: ["Hotel B"],
        4.0: ["Hotel C"],
        4.2: ["Hotel D"]
    },
    "sejour_passe": {
        True: ["Hotel A", "Hotel C"],
        False: ["Hotel B", "Hotel D"]
    },
    "critere_qualite": {
        "Excellent": ["Hotel A", "Hotel C"],
        "Bon": ["Hotel B", "Hotel D"],
        "Très bon": ["Hotel B"],
        "Moyen": ["Hotel D"]
    }
}

class SystemeExpert:
    def recommander_hotel(self, criteres):
        recommandations = []
        for critere, valeur in criteres.items():
            if critere in base_regles and valeur in base_regles[critere]:
                recommandations.extend(base_regles[critere][valeur])
        return list(set(recommandations))

def soumettre_formulaire():
    # Récupérer les valeurs des champs
    criteres_utilisateur = {}
    for critere, valeur in critere_vars.items():
        criteres_utilisateur[critere] = valeur.get()

    # Appel de la fonction de recommandation en utilisant les choix de l'utilisateur
    resultats = expert.recommander_hotel(criteres_utilisateur)

    # Affichage des recommandations avec les critères correspondants
    if resultats:
        message = "Hôtels recommandés pour vos critères :\n"
        for hotel in resultats:
            message += f"{hotel} - Critères : "
            for critere, valeurs in base_regles.items():
                for valeur, hotels in valeurs.items():
                    if hotel in hotels:
                        message += f"{critere}: {valeur}, "
            message = message[:-2] + "\n"  # Supprimer la dernière virgule et ajouter un retour à la ligne
        resultat_label.config(text=message)
    else:
        resultat_label.config(text="Aucun hôtel ne correspond à vos critères.")

def clear_champs():
    for critere in critere_vars.values():
        critere.set('Choisir une option')
# Initialisation du système expert
expert = SystemeExpert()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Système de recommandation d'hôtel")



# Chargement de l'image et redimensionnement
bg_image = tk.PhotoImage(file='hotel.png')  # Assurez-vous que le nom de l'image est correct
resized_bg_image = bg_image.subsample(2, 2)  # Redimensionner l'image

# Création d'un label pour afficher l'image redimensionnée
image_label = tk.Label(root, image=resized_bg_image)
image_label.pack(side="right")

# Création des menus déroulants pour les critères de la base de règles
critere_vars = {}
for critere, valeurs in base_regles.items():
    tk.Label(root, text=f"{critere.capitalize()} : ").pack()
    critere_vars[critere] = tk.StringVar(root)
    critere_vars[critere].set('Choisir une option')  # Valeur initiale nulle

    # Récupérer les clés au lieu des valeurs associées dans le dictionnaire
    menu_options = list(valeurs.keys())
    menu_options.sort()
    
    critere_menus = tk.OptionMenu(root, critere_vars[critere], *menu_options)
    critere_menus.pack()

# Modifier la taille des boutons
button_width = 20  # Largeur des boutons

# Bouton pour soumettre le formulaire
submit_button = tk.Button(root, text="Recommander hôtel", command=soumettre_formulaire, width=button_width)
submit_button.pack()

# Bouton pour effacer les champs
clear_button = tk.Button(root, text="Effacer les champs", command=clear_champs, width=button_width)
clear_button.pack()


# Label pour afficher le résultat
resultat_label = tk.Label(root, text="")
resultat_label.pack()

# Lancement de la boucle principale de l'interface
root.mainloop()