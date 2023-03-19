import pygame

def inside(x, y):
    if (x <= 400 and y <= 400) and (x >= 0 and y >= 0):
        return True
    return False


pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My Game")
pygame.display.set_icon(pygame.image.load("gameicon.png"))

# initial position
pygame.draw.circle(screen, 'Red', (0, 50), 25)
x = 0
y = 50

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if inside(x, y - 20):
                    y -= 20
            if event.key == pygame.K_DOWN:
                if inside(x, y + 20):
                    y += 20
            if event.key == pygame.K_LEFT:
                if inside(x - 20, y):
                    x -= 20
            if event.key == pygame.K_RIGHT:
                if inside(x + 20, y):
                    x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()