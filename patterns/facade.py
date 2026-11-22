from patterns.singleton import GameManager
from patterns.creational import CharacterFactory
from domain.exceptions import QuestForgeError


class QuestForgeAPI:
    def __init__(self, save_adapter):
        self.manager = GameManager()
        self.save_adapter = save_adapter


    def new_game(self, class_names_and_names: list[tuple[str, str]]) -> None:
        # Hides the complexity of using the Factory and updating the Manager
        party = [CharacterFactory.create(cls, name) for cls, name in class_names_and_names]
        self.manager.start_new_session(party)


    def save(self) -> None:
        # Hides the format of the save data and the adapter being used
        data = {
            "turn_count": self.manager.turn_count,
            "party": [c.name for c in self.manager.party]
        }
        self.save_adapter.save(data)