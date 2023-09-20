import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Taille de l'écran
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 30

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Block Game")

# Joueur
player_x = WIDTH // 2
player_y = HEIGHT - BLOCK_SIZE

# Blocs
blocks = []

# Ajouter des blocs au hasard
for _ in range(10):
    x = random.randint(0, WIDTH - BLOCK_SIZE)
    y = random.randint(0, HEIGHT - BLOCK_SIZE)
    blocks.append(pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block)

def main():
    global player_x

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 5
        if keys[pygame.K_UP]:
            player_y -= 5
        if keys[pygame.K_RIGHT]:
            player_x += 5

        # Dessiner l'arrière-plan
        screen.fill(WHITE)

        # Dessiner les blocs
        draw_blocks()

        # Dessiner le joueur
        pygame.draw.rect(screen, BLACK, (player_x, player_y, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
