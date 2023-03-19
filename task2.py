import pygame, os

pygame.init()

path = '.'
sounds = []
current = 0

for x in os.listdir(path):
    if '.mp3' in x:
        sounds.append(x)

print(*sounds)

screen = pygame.display.set_mode((1000, 200))
font = pygame.font.Font('TiltNeon-Regular-VariableFont_XROT,YROT.ttf', 25)
commands = font.render('Press UP to START, Press DOWN to STOP, Press LEFT to RETURN, Press RIGHT to MOVE ON', True, (255, 255, 255))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.load(sounds[current])
                pygame.mixer.music.play(-1) # start

            if event.key == pygame.K_DOWN:
                pygame.mixer.music.stop() # stop

            if event.key == pygame.K_RIGHT:
                current = (current + 1) % (len(sounds))
                pygame.mixer.music.load(sounds[current])
                pygame.mixer.music.play(-1) # next

            if event.key == pygame.K_LEFT:
                current = (current - 1) % (len(sounds))
                pygame.mixer.music.load(sounds[current])
                pygame.mixer.music.play(-1) # prev

    screen.blit(commands, (10, 10))
    pygame.display.update()
    pygame.display.flip()
