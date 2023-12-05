import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_VELOCITY = -8
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
GAP_HEIGHT = 100
FPS = 20

# Colors
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
BIRD_COLOR = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BIRD_COLOR, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = JUMP_VELOCITY

class Pipe(pygame.sprite.Sprite):
    def _init_(self, x, height):
        super()._init_()
        self.image = pygame.Surface((PIPE_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.image, WHITE, (0, 0, PIPE_WIDTH, height))
        pygame.draw.rect(self.image, WHITE, (0, height + GAP_HEIGHT, PIPE_WIDTH, SCREEN_HEIGHT - height - GAP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.height = height

    def update(self):
        self.rect.x -= 5

# Create groups for sprites
all_sprites = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()
bird = Bird()
all_sprites.add(bird)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    # Update game logic
    all_sprites.update()

    # Add pipes
    if random.randint(1, 100) < 2:
        pipe_height = random.randint(50, SCREEN_HEIGHT - GAP_HEIGHT - 50)
        new_pipe = Pipe(SCREEN_WIDTH, pipe_height)
        pipes_group.add(new_pipe)
        all_sprites.add(new_pipe)

    # Remove off-screen pipes
    for pipe in pipes_group:
        if pipe.rect.right < 0:
            pipes_group.remove(pipe)
            all_sprites.remove(pipe)

    # Check for collisions with pipes or screen boundaries
    if pygame.sprite.spritecollide(bird, pipes_group, False) or bird.rect.bottom > SCREEN_HEIGHT or bird.rect.top < 0:
        running = False

    # Draw everything on the screen
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()