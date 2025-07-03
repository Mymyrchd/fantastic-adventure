class Avatar:
    def __init__(self, name, gender, trait):
        self.name = name
        self.gender = gender
        self.trait = trait
        self.sanity = 10
        self.relationships = {}

def create_avatar():
    print("--- Création de ton avatar ---")
    name = input("Nom du personnage : ")
    gender = input("Genre (H/F/Autre) : ")
    print("Traits disponibles : courageux, observateur, romantique")
    trait = input("Choisis un trait : ")
    return Avatar(name, gender, trait)
