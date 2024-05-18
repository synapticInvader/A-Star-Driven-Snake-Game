# food.py
import random
from constants import GRID_SIZE

class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    def spawn(self, snake_positions):
        while True:
            self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if self.position not in snake_positions:
                break
