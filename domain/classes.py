from domain.character import Character

class Warrior(Character):
    """A Warrior character with enhanced attack power."""
    def __init__(self, name: str):
        super().__init__(name, health=120, attack_power=18)
        
    def special_ability(self, target: Character) -> None:
        """Warrior's special ability: Power Strike."""
        bonus = int(self.attack_power * 1.5)
        target.take_damage(bonus)  
        print(f"{self.name} uses  Cleave! {bonus} damage to {target.name}")

class Mage(Character):
    """A Mage character with enhanced attack power."""
    def __init__(self, name: str):
        super().__init__(name, health=80, attack_power=10)
        self.mana = 100  # Mages have mana for special abilities
        
    def special_ability(self, target: Character) -> None:
        """Mage's special ability: Fireball."""
        cost = 20  # Mana cost for Fireball
        if self.mana < cost:  # Check if the mage has enough mana
            print(f"{self.name} doesn't have enough mana to cast Fireball.")
            return
        self.mana -= cost  # Deduct mana cost
        damage = self.attack_power * 3  # Fireball deals triple attack power
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}. Mana left: {self.mana}")

class Rouge(Character):
    """A Rogue character with enhanced attack power."""
    def __init__(self, name: str):
        super().__init__(name, health=90, attack_power=14)
        
    def special_ability(self, target: Character) -> None:
        """Rogue's special ability: Backstab."""
        crit = int(self.attack_power * 2)  # Backstab deals double attack power
        target.take_damage(crit)
        print(f"{self.name} uses Backstab! {crit} critical damage to {target.name}.")

class Cleric(Character):
    """A Cleric character with healing abilities."""
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=8)
        
    def special_ability(self, target: Character) -> None:
        """Cleric's special ability: Heal."""
        heal_amount = 30  # Amount of health restored
        target.heal(heal_amount)
        print(f"{self.name} casts Heal! {target.name} recovers {heal_amount} HP.")
        print(f"{target.name}'s health after healing: {target.health}")