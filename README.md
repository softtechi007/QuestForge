# QuestForge

A turn-based RPG battle engine built step-by-step to master Object-Oriented Programming and Design Patterns.

## What is QuestForge?

QuestForge is an educational project where each "level" introduces a new OOP concept or design pattern. By the end, all the pieces combine into a complete, playable RPG battle system demonstrating 15+ professional software engineering concepts.

## Current Progress

### Level 0: Project Skeleton ✅
- Set up clean folder structure separating domain logic from infrastructure
- Established foundation for clean architecture

### Level 1: Classes & Objects ✅
- Created `Character` class with attributes (name, health, attack_power)
- Implemented methods: `describe()`, `attack()`, `heal()`
- Demonstrated object instantiation and state management

### Level 2: Encapsulation ✅
- Protected `Character` internal state using `_health` and `__max_health` fields
- Added `@property` decorator for read-only `health` access
- Implemented `take_damage()` with validation (rejects negative damage, clamps HP to 0)
- Updated `heal()` to cap at max HP and reject negative amounts
- Added `is_alive` property to check character status
- Prevented invalid states: no negative HP, no overhealing, no direct field tampering

### Level 3: Inheritance ✅
- Created `domain/classes.py` with four Character subclasses
- **Warrior**: High HP (120) and attack (18), Cleave ability deals 1.5x damage
- **Mage**: Lower HP (80), mana resource (50), Fireball deals 3x damage but costs 20 mana
- **Rogue**: Balanced stats (90 HP, 14 attack), Backstab deals 2x critical damage
- **Cleric**: Moderate stats (100 HP, 8 attack), Heal ability restores 30 HP to ally
- All subclasses inherit Character's encapsulated state via `super().__init__()`
- Demonstrated "is-a" relationship: all subclasses are Characters
- Kept inheritance shallow (one level) to avoid fragile base class problem

### Level 4: Polymorphism & Abstraction ✅
- Introduced an abstract base class (or interface) to enforce a unified contract for all characters
- Implemented the `take_turn(target)` method across all subclasses (Warrior, Mage, Rogue, Cleric)
- **Warrior**: `take_turn()` executes a physical strike
- **Mage**: `take_turn()` checks mana and casts a spell
- **Rogue**: `take_turn()` calculates critical hit chances
- **Cleric**: `take_turn()` evaluates ally health and heals if necessary
- Updated the Battle Engine to iterate through a generic list of `Character` objects, calling `take_turn()` without needing `if/else` type-checking
- Demonstrated the **Liskov Substitution Principle** (any subclass can seamlessly replace the base class without breaking the engine)
- Eliminated tight coupling between the Battle Engine and specific character classes, making the combat loop open for extension but closed for modification


### Level 5: Abstraction ✅
- Refactored `Character` into an Abstract Base Class (ABC) using Python's `abc` module
- Added `@abstractmethod` decorator to `special_ability()` method, enforcing a contract that all subclasses must implement
- Prevented direct instantiation of `Character` class — attempting to create `Character()` now raises `TypeError`, catching incomplete implementations at creation time rather than runtime
- Created `domain/item.py` with an `Item` abstract interface defining `apply()` method contract
- Prepared foundation for Level 6 (Composition) where `Item` will be implemented by `Potion`, `Weapon`, and `Armor` classes
- Demonstrated the distinction between abstraction (enforcing behavior contracts) and encapsulation (protecting internal state)
- Ensured future character classes (e.g., Necromancer, Archer) are mathematically forced to implement their unique abilities, preventing silent bugs


### Level 6: Composition Over Inheritance ✅
- Introduced the **Inventory** system using composition ("has-a" relationship)
- `Character` now **has-an** `Inventory` instead of inheriting item behaviors
- Created `domain/items.py` with concrete `Item` implementations:
  - **HealthPotion**: Restores HP when applied to a character
  - **Weapon**: Increases attack power when equipped
  - **Armor**: Grants shield charges that completely block incoming attacks
- Implemented shield charge mechanic: Armor provides N charges, each charge blocks one attack completely, then depletes
- Demonstrated the difference between inheritance ("is-a") and composition ("has-a")
- Solved the combinatorial explosion problem: no need for `WarriorWithFireSword` classes
- Items interact with characters through public APIs only (respecting encapsulation boundaries)
- `Inventory` is decoupled from specific item types via polymorphism—can hold any `Item` implementation
- Showed how composition enables flexible, reusable object relationships
- Prepared foundation for Level 7 (Custom Exceptions) and future levels (Decorators for buffs, Serialization for save/load)