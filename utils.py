# utils.py
import heapq
import pygame
from constants import WINDOW_SIZE, CELL_SIZE, WHITE

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal, snake_positions, grid_size):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    open_set = []

    heapq.heappush(open_set, (fscore[start], start))

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < grid_size:
                if 0 <= neighbor[1] < grid_size:
                    if neighbor in close_set:
                        continue
                    if neighbor in snake_positions:
                        continue

                    if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                        came_from[neighbor] = current
                        gscore[neighbor] = tentative_g_score
                        fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                        heapq.heappush(open_set, (fscore[neighbor], neighbor))

    return False

def draw_grid(surface):
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        for x in range(0, WINDOW_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, WHITE, rect, 1)

def draw_score(surface, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(text, (10, 10))
