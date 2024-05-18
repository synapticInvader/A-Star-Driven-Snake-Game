# snake.py
import random
from constants import GRID_SIZE, UP, DOWN, LEFT, RIGHT


class Snake:
    def __init__(self):
        self.positions = [(GRID_SIZE // 2, GRID_SIZE // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        delta_x, delta_y = self.direction
        new_head = ((head_x + delta_x) % GRID_SIZE, (head_y + delta_y) % GRID_SIZE)

        if new_head in self.positions:
            return False

        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False

        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def grow_snake(self):
        self.grow = True
