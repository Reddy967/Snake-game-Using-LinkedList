# grid.py
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

class GameGrid:
    def __init__(self):
        self.food_position = self.generate_food()

    def generate_food(self):
        x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return x, y
    
    def check_collision_with_food(self, snake_head_pos):
        return snake_head_pos == self.food_position
