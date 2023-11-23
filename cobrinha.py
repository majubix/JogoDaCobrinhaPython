import pygame
import sys
import random

pygame.init()

PURPLE = (128, 0, 128)
PINK = (255, 182, 193)

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, PURPLE, segment)

def draw_food(food):
    pygame.draw.rect(screen, PINK, food)

def main():
    clock = pygame.time.Clock()

    
    snake = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]

    
    food = pygame.Rect(random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                       random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
                       CELL_SIZE, CELL_SIZE)

    
    direction = pygame.K_RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    direction = event.key

        
        if direction == pygame.K_UP:
            snake[0].y -= CELL_SIZE
        elif direction == pygame.K_DOWN:
            snake[0].y += CELL_SIZE
        elif direction == pygame.K_LEFT:
            snake[0].x -= CELL_SIZE
        elif direction == pygame.K_RIGHT:
            snake[0].x += CELL_SIZE

        
        if snake[0].x < 0 or snake[0].x >= WIDTH or snake[0].y < 0 or snake[0].y >= HEIGHT:
            pygame.quit()
            sys.exit()

        
        for segment in snake[1:]:
            if snake[0].colliderect(segment):
                pygame.quit()
                sys.exit()

        
        if snake[0].colliderect(food):
            snake.append(pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE))
            food.x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
            food.y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE

        
        screen.fill((255, 255, 255))
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()

        
        clock.tick(FPS)

if __name__ == "__main__":
    main()
