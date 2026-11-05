from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric

if __name__ == "__main__":
    
    # Create two characters
    # hero = Character(name="Aria", health=100, attack_power=15)
    # villain = Character(name="Goblin", health=30, attack_power=5)
    # warrior = Character(name="Thorin", health=120, attack_power=18)
    # mage = Character(name="Eldrin", health=80, attack_power=10)
    # rogue = Character(name="Shadow", health=90, attack_power=12)
    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric("Liora")
    
    warrior.attack(mage)  # Warrior attacks Mage Resuing parent Character class method
    mage.special_ability(warrior)  # Mage uses special ability on Warrior
    print(f"Bram's health after attack: {warrior.health},\nSylla's health after special ability: {mage.health}")
    cleric.special_ability(warrior)  # Cleric uses special ability on Warrior
    print(f"Liora's health after healing: {cleric.health},\nBram's health after special ability: {warrior.health}")

    # Describe the characters
    # print(hero.describe())
    # print(villain.describe())
    # print(warrior.describe())
    # print(mage.describe())
        
    # for i in range(1,4):
    #     print(f"\n--- Round {i} ---")
    #     # Goblin attacks Hero
    #     villain.attack(hero)
    #     # villain.heal(10)  # Goblin heals after attacking
    #     # Warrior attacks Goblin
    #     warrior.attack(villain)
    #     # warrior.heal(10)  # Warrior heals after attacking
    #     # Mage attacks Warrior
    #     mage.attack(warrior)
    #     # mage.heal(10)  # Mage heals after attacking

    #     # Print the status of all characters after each round
    #     print(hero.describe())
    #     print(villain.describe())
    #     print(warrior.describe())
    #     print(mage.describe())


    ### test cases for level 2
    # hero.health = -90  # Directly modifying health for testing purposes
    
    # hero.take_damage(80)
    # print(hero.health)
    # hero.heal(500)  # Heal the hero by 50 HP
    # print(hero.health)