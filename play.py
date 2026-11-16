from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.battle import run_special_round,total_party_damage
from domain.items import Armor, HealthPotion, Weapon
from domain.exceptions import QuestForgeError
from patterns.creational import CharacterFactory, EnemyBuilder
from patterns.singleton import GameManager
from patterns.decorators import RageBuff, PoisonDebuff, ShieldBuff


if __name__ == "__main__":
    
    hero = Warrior("Bram")
    print(f"Base attack: {hero.attack_power}")


    # Wrap the hero in a RageBuff
    raging_hero = RageBuff(hero)
    print(f"Raging attack: {raging_hero.attack_power}")


    # Wrap the raging hero in a PoisonDebuff (Stacking!)
    poisoned_raging_hero = PoisonDebuff(raging_hero)
    print(f"Still raging attack: {poisoned_raging_hero.attack_power}")
    
    shielded_hero = ShieldBuff(hero)
    print(f"Shielded hero defense: {shielded_hero.defense}")

    # Trigger the poison
    print(poisoned_raging_hero.tick())
    print(f"HP after poison: {poisoned_raging_hero.health}")
    
    print(f"hero is attack power: {hero.attack_power}")
    

    