# game_controller.py
import pygame
from snake import Snake
from grid import GameGrid
from settings import *

class GameController:
    def __init__(self):
        self.snake = Snake((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.grid = GameGrid()
        self.score = 0

    def update(self):
        # Move the snake
        self.snake.move()

        # Check for food collision
        if self.grid.check_collision_with_food(self.snake.head.position):
            self.snake.grow_snake()  # Call grow_snake instead of grow directly
            self.grid.food_position = self.grid.generate_food()
            self.score += 1

    def check_boundaries(self):
        head_x, head_y = self.snake.head.position
        return not (0 <= head_x < SCREEN_WIDTH and 0 <= head_y < SCREEN_HEIGHT)
