from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.battle import run_special_round,total_party_damage
from domain.items import Armor, HealthPotion, Weapon
from domain.exceptions import QuestForgeError
from patterns.creational import CharacterFactory, EnemyBuilder

if __name__ == "__main__":
    
    # Create two characters
    # hero = Character(name="Aria", health=100, attack_power=15)
    # villain = Character(name="Goblin", health=30, attack_power=5)
    # warrior = Character(name="Thorin", health=120, attack_power=18)
    # mage = Character(name="Eldrin", health=80, attack_power=10)
    # rogue = Character(name="Shadow", health=90, attack_power=12)
    

    # Using Factory
    player = CharacterFactory.create("mage", "Sylla")
    player2 = CharacterFactory.create("cleric", "Liora")


    # Using Builder
    boss = (EnemyBuilder("Dragon")
            .with_health(500)
            .with_attack(50)
            .with_loot(HealthPotion())
            .build())


    print(f"Created {player.name} (HP: {player.health})")
    print(f"Created {player2.name} (HP: {player2.health})")
    print(f"Created {boss.name} (HP: {boss.health})")
        
    