from game.horror import haunted_hospital
from game.romance import talk_to_pnj
from game.endings import determine_ending

def start_story(player):
    print(f"\nBienvenue {player.name}. Ton coéquipier a disparu dans un hôpital abandonné...")

    haunted_hospital(player)

    print("\nTu rencontres Alex, un agent survivant.")
    talk_to_pnj(player, "Alex")

    print("\nTu explores les sous-sols...")
    player.sanity -= 3

    print("\nFin de l’aventure...")
    ending = determine_ending(player)
    print(ending)
