#Imports
import pygame
import random
# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 5
OBSTACLE_GAP = 200
FONT_SIZE = 32
FONT_COLOR = (255, 255, 255)
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Initialize Pygame
pygame.init()
pygame.display.set_caption("The Cosmic Vortex - Press Space to Start")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)
# Create player
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2
# Create obstacles
obstacles = []
obstacle_x = WINDOW_WIDTH
obstacle_y = random.randint(0, WINDOW_HEIGHT - OBSTACLE_HEIGHT)
# Game loop
running = True
space_pressed = False
text_surface = font.render("The Cosmic Vortex", True, WHITE)
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed = True
    if space_pressed:
        pygame.quit()
        break
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Cosmic Vortex - by zPointless")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update player position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - PLAYER_HEIGHT:
        player_y += 5
    # Update obstacle position
    obstacle_x -= OBSTACLE_SPEED
    if obstacle_x < -OBSTACLE_WIDTH:
        obstacle_x = WINDOW_WIDTH
        obstacle_y = random.randint(0, WINDOW_HEIGHT - OBSTACLE_HEIGHT)
    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    if player_rect.colliderect(obstacle_rect):
        running = False
    # Render
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(window, WHITE, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    pygame.display.update()
    clock.tick(FPS)
#font
text_surface = font.render("You Lost", True, FONT_COLOR)
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
# Draw text on the screen
window.blit(text_surface, text_rect)
pygame.display.update()
#wait time
running = True
space_pressed = False  # Flag to track if spacebar is pressed
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed = True
    if space_pressed:
        pygame.quit()
#100 Lines! - Wow! Coding really takes up a lot of code & time! I'm glad this is still on the simple side...#
