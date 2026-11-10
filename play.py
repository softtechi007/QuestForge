from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round,total_party_damage
from domain.items import Armor, HealthPotion, Weapon

if __name__ == "__main__":
    
    # Create two characters
    # hero = Character(name="Aria", health=100, attack_power=15)
    # villain = Character(name="Goblin", health=30, attack_power=5)
    # warrior = Character(name="Thorin", health=120, attack_power=18)
    # mage = Character(name="Eldrin", health=80, attack_power=10)
    # rogue = Character(name="Shadow", health=90, attack_power=12)
    
    # # 1. Create Character (Character HAS-A Inventory)
    
    hero = Warrior("Arthur")
    enemy = Mage("Evil Wizard")
    print(hero.describe())
    
    hero.inventory.add(HealthPotion(25))
    hero.inventory.use(0, hero)
    print(hero.describe())
    
    enemy.attack(hero)
    print(hero.describe())
    
    hero.inventory.add(Armor("Iron Shield", 1))
    hero.inventory.use(0, hero)
    print(hero.describe())
    
    enemy.attack(hero)
    print(hero.describe())
    
    hero.inventory.add(HealthPotion(25))
    hero.inventory.use(0, hero)
    print(hero.describe())
    
    enemy.attack(hero)
    print(hero.describe())


    
    