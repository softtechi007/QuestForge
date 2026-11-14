from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric
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


    print("--- Testing Mage Special Ability (Mana) ---")
    try:
        # 1. Capture the returned string in a variable
        result1 = mage.special_ability(warrior)
        print(result1) # 2. The UI prints it
        
        result2 = mage.special_ability(warrior)
        print(result2)
        
        result3 = mage.special_ability(warrior) 
        print(result3)
        
    except QuestForgeError as e:
        print(f"Action failed: {e}")
    
    print("\n--- Testing Empty Inventory ---")
    hero = Warrior("Arthur")
    try:
        hero.inventory.use(0, hero)
    except QuestForgeError as e:
        print(f"Game UI: {e}") 

    print("\n--- Testing Basic Attack & Shield ---")
    # Let's give Arthur some defense to test the shield string
    print(hero.add_defense(2)) 
    
    # Now attack him
    print(mage.attack(hero)) 
    print(mage.attack(hero)) # This one should trigger the shield block string!
    print(hero.health)
    print(mage.attack(hero)) 
    print(hero.health)  # This should show the remaining health after the shield is gone

    
    