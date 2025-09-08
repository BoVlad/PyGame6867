import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu example")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

state = "menu"  # menu, playing, options
volume = 5

# прямокутники для кнопок
btn_start = pygame.Rect(WIDTH//2 - 120, 220, 240, 56)
btn_options = pygame.Rect(WIDTH//2 - 120, 300, 240, 56)
btn_quit = pygame.Rect(WIDTH//2 - 120, 380, 240, 56)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_start.collidepoint(event.pos):
                    state = "playing"
                elif btn_options.collidepoint(event.pos):
                    state = "options"
                elif btn_quit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()

        elif state == "options":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"
                elif event.key == pygame.K_LEFT:
                    volume = max(0, volume - 1)
                elif event.key == pygame.K_RIGHT:
                    volume = min(10, volume + 1)

        elif state == "playing":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "menu"

    # малювання
    if state == "menu":
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (70, 130, 180), btn_start)
        pygame.draw.rect(screen, (70, 130, 180), btn_options)
        pygame.draw.rect(screen, (70, 130, 180), btn_quit)
        screen.blit(font.render("Start", True, (255,255,255)), (btn_start.x+70, btn_start.y+10))
        screen.blit(font.render("Options", True, (255,255,255)), (btn_options.x+50, btn_options.y+10))
        screen.blit(font.render("Quit", True, (255,255,255)), (btn_quit.x+80, btn_quit.y+10))

    elif state == "options":
        screen.fill((20, 20, 40))
        txt = font.render(f"Options. Volume: {volume}", True, (255,255,255))
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2))
        backtxt = font.render("Esc = Back", True, (200,200,200))
        screen.blit(backtxt, (WIDTH//2 - backtxt.get_width()//2, HEIGHT//2+60))

    elif state == "playing":
        screen.fill((0, 120, 80))
        txt = font.render("Game running. Esc = back", True, (255,255,255))
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)