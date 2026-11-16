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

### Level 7: Custom Exceptions & Error Handling ✅
- Created `domain/exceptions.py` with a base `QuestForgeError` class and specific domain subtypes (`DeadCharacterError`, `InsufficientManaError`, `InvalidActionError`, `InventoryEmptyError`)
- Replaced generic errors and silent failures in `character.py` and `classes.py` with domain-specific exceptions
- Implemented Exception Translation in `inventory.py`: catching Python's generic `IndexError` and raising the domain-specific `InventoryEmptyError`
- Established a strict error-handling contract so the UI/CLI (Level 17) can catch specific game rules and display friendly messages without crashing the engine
- Demonstrated how custom exceptions turn errors into part of the project's domain vocabulary, allowing calling code to react precisely to different failure states

### Level 8: SOLID Principles Refactor ✅
- Audited Levels 1–7 against the five SOLID principles; this was a pure refactor level with no new features, focused on hardening the foundation before adding design patterns in Levels 9–14
- **Single Responsibility Principle (SRP):** Removed all `print()` calls from `domain/character.py` and `domain/classes.py`; combat methods (`attack`, `take_damage`, `heal`, `add_defense`, `special_ability`) now return descriptive strings instead of writing to the console
- Separated game logic from presentation: `Character` now only manages state and math; `play.py` (the UI layer) is responsible for displaying returned strings — enabling future swap from CLI to Web UI without touching domain code
- **Interface Segregation Principle (ISP):** Split the monolithic `Item` interface from Level 5 into two focused abstractions in `domain/item.py`: `Usable` (with `apply()`) for consumables and `Equippable` (with `equip()`) for gear
- Updated `domain/items.py`: `HealthPotion` now implements only `Usable`; `Weapon` now implements only `Equippable` — no class is forced to stub out methods it doesn't use
- **Open/Closed Principle (OCP):** Verified that the polymorphic `take_turn()` loop from Level 4 already satisfies OCP — new character types (e.g., Necromancer) can be added as new subclasses without editing the battle engine
- **Liskov Substitution Principle (LSP):** Confirmed all subclasses honor the parent contract — `special_ability()` now consistently returns `str` across Warrior, Mage, Rogue, and Cleric, with no inconsistent return types or silent `None` returns
- **Dependency Inversion Principle (DIP):** Documented the architectural intent that high-level modules (Battle Engine, UI) depend on abstractions (`Character` ABC, `Usable`/`Equippable` interfaces) rather than concrete classes — foundation for future save/load adapters and mock-based testing
- Authored `REFACTOR_NOTES.md` capturing before/after snippets for each SOLID letter, forming the basis of the final architecture write-up
- Established that most design patterns in Levels 9–14 are simply named recipes for satisfying SOLID; a SOLID-clean base makes pattern insertion trivial rather than invasive
- Previewed the Observer pattern (Level 14): returning strings from combat methods is the first step toward a decoupled event system where multiple listeners (CLI, Web UI, log file) can subscribe to combat events

### Level 9: Creational Patterns I — Factory & Builder ✅
- Separated object creation logic from the code that uses it, decoupling the game engine from concrete classes
- Implemented the **Factory Method Pattern** via `CharacterFactory` in `patterns/creational.py`
  - Uses a `@staticmethod` to instantiate playable characters (`Warrior`, `Mage`, `Rogue`, `Cleric`) based on string input
  - Callers depend only on the factory, respecting the Dependency Inversion Principle (DIP)
  - Adding new character classes now only requires updating the factory, not the UI or game loop
- Implemented the **Builder Pattern** via `EnemyBuilder` to construct complex enemies (e.g., Bosses)
  - Replaced the "Telescoping Constructor" anti-pattern with a fluent, step-by-step configuration API (`.with_health()`, `.with_loot()`)
  - Used method chaining (returning `self`) to make object construction readable and maintainable
  - Demonstrated when to use instance methods (Builder needs state/memory) vs. static methods (Factory is a pure utility)
- Updated `play.py` to spawn the player via the Factory and a custom Dragon boss via the Builder

### Level 10: Creational Patterns II — Singleton ✅
- Implemented the **Singleton Pattern** via `GameManager` in `patterns/singleton.py` to manage global session state
- Guaranteed exactly one instance of `GameManager` exists in memory by overriding `__new__` and using an `_initialized` guard in `__init__` to prevent state reset
- Centralized session-wide coordination: tracks the current player party, turn counter, and difficulty settings
- Provided a single global access point for the game engine, UI, and battle loop without passing the manager through every function signature
- Demonstrated the deliberate, sparing use of Singletons for infrastructure coordinators rather than domain entities, avoiding the pitfalls of hidden global state and test pollution
- Updated `play.py` to prove that multiple calls to `GameManager()` return the exact same memory address and share state across different scopes

### Level 11: Structural Patterns I — Decorator ✅
- Solved the **Open/Closed Principle violation** that would occur from adding boolean flags (`is_raging`, `is_poisoned`) to the `Character` class for every new status effect
- Avoided **class explosion** from inheritance: no need for `RagingWarrior`, `PoisonedWarrior`, `RagingPoisonedWarrior` combinations
- Implemented the **Decorator Pattern** in `patterns/decorators.py` to add behavior to individual objects at runtime through composition
- Created `CharacterBuff` base decorator class that wraps a `Character` and delegates all unhandled attributes/methods via Python's `__getattr__` magic method
- Demonstrated the **"Russian Doll" composition model**: each decorator wraps the previous one, forming a chain where the outermost wrapper is the only one the client sees
- Implemented `RageBuff` decorator that multiplies `attack_power` by 1.5, overriding the property to add behavior around the wrapped object's value
- Implemented `PoisonDebuff` decorator with custom `tick()` method that applies damage-over-time, demonstrating decorators can add entirely new methods not present in the base interface
- Implemented `ShieldBuff` decorator that adds defense charges, proving decorators can wrap state as well as behavior
- Showed **runtime stacking**: `PoisonDebuff(RageBuff(Warrior("Bram")))` creates a character with both rage and poison effects, with each decorator handling its specific concern
- Maintained **polymorphism**: the battle engine interacts with decorated characters through the same `Character` interface, unaware of how many wrappers exist
- Preserved **encapsulation boundaries**: decorators interact with wrapped objects only through public interfaces (`self._wrapped.defense`), never reaching into private state (`self._wrapped._defense`), ensuring the composition chain stays intact when stacking
- Documented the **"internal self-call" limitation**: decorators cannot intercept the wrapped object's internal `self` method calls (the same limitation as Spring's proxy-based `@Transactional`), so we decorate the method that consumes state rather than the state itself
- Updated `play.py` to demonstrate wrapping a `Warrior` in multiple decorators and verifying that the original `Warrior` instance remains unmodified (decorators add behavior without mutating the core)
- Established foundation for Level 17 where buffs and debuffs will be applied and expire dynamically during the main battle loop