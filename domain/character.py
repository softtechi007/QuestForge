class Character:
    """Placeholder — fleshed out in Level 1."""
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.__max_health = health  # Private attribute for maximum health
        self.attack_power = attack_power

    @property
    def health(self)-> int:
        return self._health
    
    @property
    def is_alive(self)-> bool:
        return self._health > 0
    
    def describe(self)-> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK."
    
    def take_damage(self, amount: int)-> None:
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
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
        
    