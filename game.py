# game.py
import pygame
import sys
from snake import Snake
from food import Food
from constants import BLACK, GREEN, RED, GRID_SIZE, WINDOW_SIZE, CELL_SIZE, WHITE
from utils import a_star_search, draw_grid, draw_score


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Snake Game with A* Algorithm")
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            path = a_star_search(self.snake.positions[0], self.food.position, self.snake.positions, GRID_SIZE)
            if path:
                next_move = path[-1]
                move_dir = (next_move[0] - self.snake.positions[0][0], next_move[1] - self.snake.positions[0][1])
                self.snake.change_direction(move_dir)

            if not self.snake.move():
                self.running = False

            if self.snake.positions[0] == self.food.position:
                self.snake.grow_snake()
                self.food.spawn(self.snake.positions)
                self.score += 1

            self.surface.fill(BLACK)
            draw_grid(self.surface)
            draw_score(self.surface, self.score)

            for pos in self.snake.positions:
                rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.surface, GREEN, rect)

            rect = pygame.Rect(self.food.position[0] * CELL_SIZE, self.food.position[1] * CELL_SIZE, CELL_SIZE,
                               CELL_SIZE)
            pygame.draw.rect(self.surface, RED, rect)

            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()
            self.clock.tick(10)

        self.show_game_over()

    def show_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        self.surface.blit(text, text_rect)

        font_small = pygame.font.Font(None, 36)
        score_text = font_small.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2 + 50))
        self.surface.blit(score_text, score_rect)

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

