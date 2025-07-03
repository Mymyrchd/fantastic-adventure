def haunted_hospital(player):
    print("Tu entres dans l’hôpital abandonné. L’ambiance est pesante...")
    print("1. Explorer la salle d’opération")
    print("2. Aller à la morgue")
    choice = input("Ton choix (1/2) : ")

    if choice == "1":
        print("Du sang frais sur les murs... ta santé mentale baisse.")
        player.sanity -= 2
    else:
        print("Tu sens une présence derrière toi. Rien ne se passe, mais tu trembles.")
        player.sanity -= 1
