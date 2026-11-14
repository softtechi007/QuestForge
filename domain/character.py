from abc import ABC, abstractmethod
from domain.inventory import Inventory
from domain.exceptions import DeadCharacterError

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
    
    def take_damage(self, amount: int)-> str:
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        
        # ← NEW LOGIC: Check if we have shield charges
        if self._defense > 0:
            # Block the attack completely!
            self._defense -= 1
            return f"{self.name}'s shield blocks the attack! ({self._defense} charges left)" # Exit early, no damage taken
        
        self._health = max(0, self._health - amount)
        return f"{self.name} takes {amount} damage! (HP: {self._health})"

    def heal(self, amount: int)-> str:
            if amount < 0:
                raise ValueError("Healing amount cannot be negative.")
            if not self.is_alive:
                return f"{self.name} is dead and cannot be healed."
            self._health = min(self._health + amount, self.__max_health)
            return f"{self.name} heals for {amount} HP! (HP: {self._health})"
    
    def attack(self, target: 'Character')-> str:
        if not self.is_alive:
            raise DeadCharacterError(f"{self.name} is dead and cannot act")
        if not target.is_alive:
            return f"{target.name} is already dead."
        target.take_damage(self.attack_power)
        return f"{self.name} attacks {target.name} for {self.attack_power} damage!"
    
    def add_defense(self, amount: int) -> str:
        """Add shield charges (called by Armor items)"""
        if amount < 0:
            raise ValueError("Defense amount cannot be negative.")
        self._defense += amount
        return f"{self.name} gains {amount} shield charges! (Total: {self._defense})"
    
    @abstractmethod
    def special_ability(self, target: 'Character')-> str:
        """Every concrete Character MUST define its own special move."""
        raise NotImplementedError
        
    