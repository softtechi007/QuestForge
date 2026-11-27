# from domain.character import Character
# from domain.classes import Warrior, Mage, Rogue, Cleric
# from domain.battle import run_special_round,total_party_damage
# from domain.items import Armor, HealthPotion, Weapon
# from domain.exceptions import QuestForgeError
# from patterns.creational import CharacterFactory, EnemyBuilder
# from patterns.singleton import GameManager
# from patterns.decorators import RageBuff, PoisonDebuff, ShieldBuff


# if __name__ == "__main__":
    
#     hero = Warrior("Bram")
#     print(f"Base attack: {hero.attack_power}")


#     # Wrap the hero in a RageBuff
#     raging_hero = RageBuff(hero)
#     print(f"Raging attack: {raging_hero.attack_power}")


#     # Wrap the raging hero in a PoisonDebuff (Stacking!)
#     poisoned_raging_hero = PoisonDebuff(raging_hero)
#     print(f"Still raging attack: {poisoned_raging_hero.attack_power}")
    
#     shielded_hero = ShieldBuff(hero)
#     print(f"Shielded hero defense: {shielded_hero.defense}")

#     # Trigger the poison
#     print(poisoned_raging_hero.tick())
#     print(f"HP after poison: {poisoned_raging_hero.health}")
    
#     print(f"hero is attack power: {hero.attack_power}")
    

# ==========================================
# LEVEL 12: FACADE & ADAPTER TESTING
# ==========================================
from patterns.facade import QuestForgeAPI
from infra.save_adapter import JsonFileAdapter, InMemoryAdapter
from patterns.state import BattleState, BattleStateMachine

print("\n--- Testing Facade with JsonFileAdapter (Hard Drive) ---")
# 1. Create the Facade. We inject the JSON adapter via the constructor.
json_api = QuestForgeAPI(save_adapter=JsonFileAdapter("my_save.json"))

# 2. Start a new game. Notice we ONLY pass simple strings! 
# The UI doesn't need to import Warrior or Mage anymore!
json_api.new_game([
    ("Warrior", "Bram"),
    ("Mage", "Elara")
])

# 3. Save the game. The Facade translates the objects to a dict, 
# and the Adapter writes it to the disk.
json_api.save()
print("Game saved to disk! Check your folder for 'my_save.json'.")


print("\n--- Testing Facade with InMemoryAdapter (RAM) ---")
# 1. Create a SECOND Facade, but inject the RAM adapter instead.
ram_api = QuestForgeAPI(save_adapter=InMemoryAdapter())

# 2. Start a new game with different heroes.
ram_api.new_game([
    ("Rogue", "Shadow"),
    ("Cleric", "Light")
])

# 3. Save to RAM (No files are touched!)
ram_api.save()

# 4. Load from RAM to prove it worked.
loaded_ram_data = ram_api.save_adapter.load()
print(f"Loaded from RAM: {loaded_ram_data}")

# ==========================================
# LEVEL 13: STRATEGY & STATE TESTING
# ==========================================


print("\n--- Testing BattleStateMachine ---")

# 1. Initialize the machine (starts in IDLE)
machine = BattleStateMachine()
print(f"1. Initial state: {machine.state.name}")

# 2. Attempt an ILLEGAL transition: IDLE -> VICTORY
print("2. Attempting illegal transition: IDLE -> VICTORY...")
try:
    machine.transition(BattleState.VICTORY)
    print("   ❌ FAIL: The machine allowed an illegal transition!")
except ValueError as e:
    print(f"   ✅ SUCCESS: Caught expected error -> {e}")

# 3. Attempt a LEGAL transition: IDLE -> PLAYER_TURN
print("3. Attempting legal transition: IDLE -> PLAYER_TURN...")
try:
    machine.transition(BattleState.PLAYER_TURN)
    print(f"   ✅ SUCCESS: State is now {machine.state.name}")
except ValueError as e:
    print(f"   ❌ FAIL: Unexpected error -> {e}")