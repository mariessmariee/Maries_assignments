import pygame
import random
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blue Cats")
clock = pygame.time.Clock()

original_img = pygame.image.load("blue_cat.png").convert_alpha()

class BlueCat:
    def __init__(self):
        self.size = random.randint(40, 100)
        self.image = pygame.transform.scale(original_img, (self.size, self.size))
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT - self.size)
        self.speed_x = random.uniform(1, 4)
        self.speed_y = random.uniform(-1, 1)
        self.angle = random.uniform(0, 2 * math.pi)
        self.radius = random.randint(20, 80)
        self.center_x = self.x
        self.center_y = self.y
        self.rotation = random.choice([True, False])
        self.rotation_speed = random.uniform(1, 3)

    def update(self):
        if self.rotation:
            self.angle += 0.03
            x = self.center_x + math.cos(self.angle) * self.radius
            y = self.center_y + math.sin(self.angle) * self.radius
            rotated_img = pygame.transform.rotate(self.image, self.angle * self.rotation_speed * 10)
            rect = rotated_img.get_rect(center=(x, y))
            screen.blit(rotated_img, rect)
        else:
            self.x += self.speed_x
            self.y += self.speed_y
            if self.x > SCREEN_WIDTH:
                self.x = -self.size
            if self.y < 0 or self.y > SCREEN_HEIGHT - self.size:
                self.speed_y *= -1
            screen.blit(self.image, (self.x, self.y))

cats = [BlueCat() for _ in range(7)]

flag = True
while flag:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.fill(BACKGROUND_COLOR)
    for cat in cats:
        cat.update()
    pygame.display.flip()

pygame.quit()
