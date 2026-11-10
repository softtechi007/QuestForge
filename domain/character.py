from abc import ABC, abstractmethod
from domain.inventory import Inventory

class Character(ABC):
    """Placeholder — fleshed out in Level 1."""
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.__max_health = health  # Private attribute for maximum health
        self.attack_power = attack_power
        self.inventory = Inventory()
        self._defense = 0  # Default defense value

    @property
    def health(self)-> int:
        return self._health
    
    @property
    def is_alive(self)-> bool:
        return self._health > 0
    
    @property
    def defense(self) -> int:
        return self._defense
    
    def describe(self)-> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK."
    
    def take_damage(self, amount: int)-> None:
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        
        # ← NEW LOGIC: Check if we have shield charges
        if self._defense > 0:
            # Block the attack completely!
            self._defense -= 1
            print(f"{self.name}'s shield blocks the attack! ({self._defense} charges left)")
            return  # Exit early, no damage taken
        
        self._health = max(0, self._health - amount)
        
    def heal(self, amount: int)-> None:
            if amount < 0:
                raise ValueError("Healing amount cannot be negative.")
            if not self.is_alive:
                print(f"{self.name} is dead and cannot be healed.")
                return
            self._health = min(self._health + amount, self.__max_health)
            print(f"{self.name} heals for {amount} HP!")
    
    def attack(self, target: 'Character')-> None:
        if not self.is_alive:
            print(f"{self.name} is dead and cannot attack.")
            return
        if not target.is_alive:
            print(f"{target.name} is already dead.")
            return
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
    
    def add_defense(self, amount: int) -> None:
        """Add shield charges (called by Armor items)"""
        if amount < 0:
            raise ValueError("Defense amount cannot be negative.")
        self._defense += amount
        print(f"{self.name} gains {amount} shield charges! (Total: {self._defense})")
    
    @abstractmethod
    def special_ability(self, target: 'Character')-> None:
        """Every concrete Character MUST define its own special move."""
        raise NotImplementedError
        
    