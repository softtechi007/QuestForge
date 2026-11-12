from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round,total_party_damage
from domain.items import Armor, HealthPotion, Weapon
from domain.exceptions import QuestForgeError


if __name__ == "__main__":
    
    # Create two characters
    # hero = Character(name="Aria", health=100, attack_power=15)
    # villain = Character(name="Goblin", health=30, attack_power=5)
    # warrior = Character(name="Thorin", health=120, attack_power=18)
    # mage = Character(name="Eldrin", health=80, attack_power=10)
    # rogue = Character(name="Shadow", health=90, attack_power=12)
    

    mage = Mage("Sylla")
    warrior = Warrior("Bram")


    try:
        # Sylla starts with 50 mana. 3 fireballs (20 cost each) will fail.
        mage.special_ability(warrior)
        mage.special_ability(warrior)
        mage.special_ability(warrior) 
    except QuestForgeError as e:
        print(f"Action failed: {e}")
    
# 1. Setup: Create a character with an empty inventory
    hero = Warrior("Arthur")

    # 2. The Bouncer: Try to use an item that doesn't exist
    try:
        print("Attempting to use item at index 0...")
        hero.inventory.use(0, hero)
        
    except QuestForgeError as e:
        # 3. The Polite Rejection: Catch the domain error and print friendly text
        print(f"Game UI: {e}") 

    print("Game continues smoothly...")

    
    