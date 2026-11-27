from abc import ABC, abstractmethod
import random


class AIStrategy(ABC):
    @abstractmethod
    def choose_target(self, allies: list, enemies: list):
        ...


class AggressiveAI(AIStrategy):
    def choose_target(self, allies: list, enemies: list):
        # Returns the character with the lowest health
        return min(enemies, key=lambda c: c.health)


class RandomAI(AIStrategy):
    def choose_target(self, allies: list, enemies: list):
        # Returns a random character
        return random.choice(enemies)

class DefensiveAI(AIStrategy):
    def choose_target(self, allies: list, enemies: list):
        # Returns the character with the highest health
        # 1. Find allies below 30% health
        critical_allies = [ally for ally in allies if ally.health < ally.max_health * 0.3]
        
        # 2. If there are critical allies, heal the one with the LOWEST health
        if critical_allies:
            return min(critical_allies, key=lambda c: c.health)
        
        # 3. Otherwise, fall back to attacking the enemy with the lowest health
        return min(enemies, key=lambda c: c.health)