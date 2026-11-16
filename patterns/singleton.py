class GameManager:
    # 1. CLASS-LEVEL VARIABLE: This belongs to the Blueprint, not the object.
    # It acts as the "vault" that holds the single instance in memory.
    _instance = None

    # 2. INTERCEPTING THE CONSTRUCTION CREW
    def __new__(cls):
        # Check the vault: Have we built the house yet?
        if cls._instance is None:
            # NO: Build the house (allocate memory) using Python's default builder
            cls._instance = super().__new__(cls)
            # Put a "Not Furnished Yet" sign on the door
            cls._instance._initialized = False
        # YES (or we just built it): Return the exact same memory address.
        # We NEVER create a new one.
        return cls._instance


     # 3. INTERCEPTING THE INTERIOR DESIGNER
    def __init__(self):
        # Prevent re-initialization if __init__ is called multiple times
        # Check the sign on the door!
        if self._initialized:
            # The house is already furnished. DO NOT TOUCH THE DATA.
            # Just exit immediately.
            return
        
        # If we reach here, it's the very first time. Furnish the house!    
        self.party: list = []
        self.turn_count: int = 0
        self.difficulty: str = "normal"
        # Take down the sign. Next time, the designer will be stopped.
        self._initialized = True


    def start_new_session(self, party: list) -> None:
        self.party = party
        self.turn_count = 0


    def next_turn(self) -> int:
        self.turn_count += 1
        return self.turn_count