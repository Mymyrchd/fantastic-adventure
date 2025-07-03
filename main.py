from game.avatar import create_avatar
from game.story import start_story
from game.state import save_game, load_game

if __name__ == "__main__":
    print("=== SAUVETAGE OBSCUR ===")
    print("1. Nouvelle Partie")
    print("2. Charger la partie")
    choix = input("Choisis une option (1/2): ")

    if choix == "2":
        player = load_game()
        if not player:
            print("\nCréation d'une nouvelle partie...")
            player = create_avatar()
    else:
        player = create_avatar()

    start_story(player)
    save_game(player)
)=