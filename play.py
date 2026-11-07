from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round,total_party_damage

if __name__ == "__main__":
    
    # Create two characters
    # hero = Character(name="Aria", health=100, attack_power=15)
    # villain = Character(name="Goblin", health=30, attack_power=5)
    # warrior = Character(name="Thorin", health=120, attack_power=18)
    # mage = Character(name="Eldrin", health=80, attack_power=10)
    # rogue = Character(name="Shadow", health=90, attack_power=12)
    party = [Warrior("Thorin"), Mage("Eldrin"), Rouge("Shadow"), Cleric("Liora")]
    dummy_enemy = Warrior("Training dummy")
    
    # for member in party:
    #     print("*" * 100)
    #     print("=" * 100)
    #     print("Attackers Information:")
    #     print(member.describe())
    #     print("=" * 100)
    #     print("Defenders Information:")
    #     print(dummy_enemy.describe())
    #     print("=" * 100)
    #     run_special_round(member, dummy_enemy)
    #     print(f"Dummy HP: {dummy_enemy.health}\n")
    
    total_party_damage(party, dummy_enemy)
    print(f"Dummy HP after all attacks: {dummy_enemy.health}\n")