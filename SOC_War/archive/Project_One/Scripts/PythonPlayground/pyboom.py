import pygame
import random
import sys

# Initialize
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PyBOOM - Vanth Style")
clock = pygame.time.Clock()

# Load basic sound
# boom = pygame.mixer.Sound("boom.wav")  # Only if you have a sound file

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Random colors & rectangles
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        rect = pygame.Rect(random.randint(0, 600), random.randint(0, 440), 40, 40)
        pygame.draw.rect(screen, color, rect)

        pygame.display.flip()
        clock.tick(15)

except KeyboardInterrupt:
    pygame.quit()
    print("Vanth out.")

