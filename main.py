# main.py
import pygame
from settings import *
from game_controller import GameController

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
game_controller = GameController()

direction_map = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

running = True
while running:
    screen.fill(BG_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in direction_map:
                game_controller.snake.change_direction(direction_map[event.key])

    # Update game state
    game_controller.update()
    if game_controller.check_boundaries():
        running = False  # Game over if snake hits boundary

    # Draw the snake
    current = game_controller.snake.head
    while current:
        pygame.draw.rect(screen, SNAKE_COLOR, (*current.position, GRID_SIZE, GRID_SIZE))
        current = current.next

    # Draw the food
    pygame.draw.rect(screen, FOOD_COLOR, (*game_controller.grid.food_position, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control game speed

pygame.quit()
