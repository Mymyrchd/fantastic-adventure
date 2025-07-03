import json

SAVE_FILE = "savegame.json"

def save_game(player):
    data = {
        "name": player.name,
        "gender": player.gender,
        "trait": player.trait,
        "sanity": player.sanity,
        "relationships": player.relationships
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("\n✅ Jeu sauvegardé avec succès.")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            from game.avatar import Avatar
            player = Avatar(
                name=data["name"],
                gender=data["gender"],
                trait=data["trait"]
            )
            player.sanity = data["sanity"]
            player.relationships = data["relationships"]
            print("\n🔁 Partie chargée avec succès.")
            return player
    except FileNotFoundError:
        print("\nAucune sauvegarde trouvée.")
        return None
