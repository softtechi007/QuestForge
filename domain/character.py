class Character:
    """Placeholder — fleshed out in Level 1."""
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def describe(self):
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK."
    
    def attack(self, target: 'Character'):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
    def heal(self, amount: int):
        self.health += amount
        print(f"{self.name} heals for {amount} HP!")