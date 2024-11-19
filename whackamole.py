import pygame
import random

# Constants
GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE

def draw_grid(screen):
    """Draws a 20x16 grid on the screen."""
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, "black", (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, "black", (0, y), (WINDOW_WIDTH, y))

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        # Load mole image
        mole_image = pygame.image.load("mole.png")
        mole_position = (0, 0)  # Initial position of the mole in the top-left corner

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(
                        mole_position[0], mole_position[1], GRID_SIZE, GRID_SIZE
                    )
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # Move mole to a new random position
                        mole_x = random.randrange(0, GRID_WIDTH) * GRID_SIZE
                        mole_y = random.randrange(0, GRID_HEIGHT) * GRID_SIZE
                        mole_position = (mole_x, mole_y)

            # Draw everything
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_position)
            pygame.display.flip()

            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()