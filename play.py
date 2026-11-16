from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.battle import run_special_round,total_party_damage
from domain.items import Armor, HealthPotion, Weapon
from domain.exceptions import QuestForgeError
from patterns.creational import CharacterFactory, EnemyBuilder
from patterns.singleton import GameManager

# Let's create a completely separate function far away from our main code
def simulate_battle_round():
    # Inside this function, we just call GameManager(). 
    # We don't need to pass it as an argument! It finds itself.
    local_manager = GameManager() 
    
    print(f"  -> [Inside Battle] Turn count before: {local_manager.turn_count}")
    local_manager.next_turn()
    print(f"  -> [Inside Battle] Turn count after: {local_manager.turn_count}")

if __name__ == "__main__":
    print("=== 1. FIRST CREATION (Main Menu) ===")
    # The Construction Crew builds the house. The Designer furnishes it.
    manager1 = GameManager()
    manager1.difficulty = "hard"
    manager1.party = ["Aria (Mage)", "Thorin (Warrior)"]
    
    print(f"Manager 1 Memory ID: {id(manager1)}")
    print(f"Manager 1 Difficulty: {manager1.difficulty}")
    print(f"Manager 1 Party: {manager1.party}")
    
    print("\n=== 2. SECOND CREATION (Settings Menu) ===")
    # The Construction Crew sees the house exists and returns the same address.
    # The Designer sees the "Furnished" sign and walks away.
    manager2 = GameManager()
    
    print(f"Manager 2 Memory ID: {id(manager2)}")
    print(f"Are they the EXACT same object in memory? {manager1 is manager2}")
    print(f"Manager 2 Difficulty: {manager2.difficulty}") # Should still be "hard"!
    
    print("\n=== 3. THIRD CREATION (Inside a totally different function) ===")
    simulate_battle_round()
    
    print("\n=== 4. VERIFYING STATE BACK IN MAIN ===")
    # Because the battle function modified the SINGLETON, 
    # manager1 sees the changes instantly!
    print(f"Manager 1 Turn Count: {manager1.turn_count}") 
        
    