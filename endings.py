def determine_ending(player):
    love = player.relationships.get("Alex", 0)

    if player.sanity <= 0:
        return "Fin tragique : tu perds la tête, piégé dans l’horreur."
    elif love >= 3:
        return "Fin romantique : tu sauves Alex, et vous fuyez ensemble."
    elif player.sanity < 5:
        return "Fin neutre : ton coéquipier est perdu, mais tu t’en sors."
    else:
        return "Fin héroïque : tu surmontes les ténèbres et retrouves ton partenaire."
