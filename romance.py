def talk_to_pnj(player, pnj_name):
    affection = player.relationships.get(pnj_name, 0)
    print(f"\n{pnj_name} te regarde fixement.")
    print("1. Lui sourire")
    print("2. Rester distant")
    choice = input("Ton choix : ")

    if choice == "1":
        affection += 2
        print(f"{pnj_name} te rend ton sourire, un lien se crée...")
    else:
        affection -= 1
        print(f"{pnj_name} détourne le regard.")

    player.relationships[pnj_name] = affection
