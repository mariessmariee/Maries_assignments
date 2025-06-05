import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Heart Painter ❤️")
clock = pygame.time.Clock()

try:
    heart_img = pygame.image.load("red_heart.png").convert_alpha()
    heart_img = pygame.transform.scale(heart_img, (40, 40))
except pygame.error as e:
    print("Fehler beim Laden von red_heart.png:", e)
    pygame.quit()
    sys.exit()

class Brush:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_position(self):
        return (self._x, self._y)

    def set_position(self, x, y):
        self._x = x
        self._y = y

class EmojiBrush(Brush):
    def __init__(self, x, y, image):
        super().__init__(x, y)
        self.__image = image

    def draw(self, surface):
        surface.blit(self.__image, self.get_position())

def show_start_screen():
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 28)
    title = font.render("Heart Painter", True, (0, 0, 0))
    instructions = [
        "Klicke mit der Maus, um Herzen zu malen.",
        "Drücke 'C', um den Bildschirm zu leeren.",
        "Drücke eine Taste, um zu starten."
    ]
    screen.blit(title, (250, 100))
    for i, line in enumerate(instructions):
        text = small_font.render(line, True, (0, 0, 0))
        screen.blit(text, (160, 200 + i * 40))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def main():
    show_start_screen()
    painting = []
    while True:
        mouse_pressed = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    painting = []
        if mouse_pressed:
            x, y = pygame.mouse.get_pos()
            brush = EmojiBrush(x - 20, y - 20, heart_img)
            painting.append(brush)
        screen.fill((255, 255, 255))
        for brush in painting:
            brush.draw(screen)
        pygame.display.flip()
        clock.tick(60)

main()
