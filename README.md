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