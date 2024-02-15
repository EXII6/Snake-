import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Définition de la taille de la fenêtre
WIDTH, HEIGHT = 600, 400

# Définition de la taille des blocs et de la vitesse de déplacement
BLOCK_SIZE = 20
FPS = 10

# Chargement de l'image du serpent
snake_image = pygame.image.load('snake.png')
snake_image = pygame.transform.scale(snake_image, (BLOCK_SIZE, BLOCK_SIZE))  # Redimensionner l'image

# Initialisation de l'affichage
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("jeu du serpent")

# Fonction principale du jeu
def game_loop():
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += x_change
        y += y_change

        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Ajouter la tête du serpent à la liste des positions
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        # Garder la longueur du serpent égale à snake_length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Dessiner le serpent en parcourant la liste des positions
        for block in snake_list:
            window.blit(snake_image, (block[0], block[1]))

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(FPS)

    window.fill(BLACK)
    message("Game Over!", RED)
    pygame.display.update()
    time.sleep(2)
    game_loop()

# Fonction pour afficher un message à l'écran
def message(msg, color):
    font = pygame.font.SysFont(None, 25)
    text = font.render(msg, True, color)
    window.blit(text, [WIDTH / 2 - 75, HEIGHT / 2])

game_loop()