from domain.character import Character

def run_special_round(attacker: Character, defender: Character) -> None:
    """Works for ANY Character subclass — this is polymorphism in action."""
    attacker.special_ability(defender)

def total_party_damage(attackers: list[Character], target: Character) -> None:
    """list of mixed characters and have them all attack a target, without checking their types"""
    for member in attackers:
        member.attack(target)
        print(f"{member.name} attacks {target.name} for {member.attack_power} damage! {target.name}'s health is now {target.health}.")