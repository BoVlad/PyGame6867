import pygame
import random


pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 450, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hot Air Balloon")

font = pygame.font.SysFont("Bahnschrift", 30)
font_end = pygame.font.SysFont("Bahnschrift", 70)

clock = pygame.time.Clock()

paused = False

lives_var = 10000
money_var = 0
shield_time = -10

speed = 2
speed_adding = 0.001


shield_timer = 0
shield_list = []
shield_min_distance = 700

heal_timer = 0
heal_list = []
heal_min_distance = 900

money_timer = 0
money_list = []
money_min_distance = 10

obstacle_timer = 0
obstacles = []
min_distance = 80


last_mouse_x = pygame.mouse.get_pos()
last_mouse_x = last_mouse_x[0]

bg = pygame.image.load("Images/BackGround.png")
bg = pygame.transform.scale(bg, (450, 700))
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

balloon = pygame.image.load("Images/Balloon.png").convert_alpha()
balloon = pygame.transform.scale(balloon, (70, 123))
balloon_rect = balloon.get_rect()
balloon_rect.topleft = (175, 450)

heal = pygame.image.load("Images/Heal.png")
heal = pygame.transform.scale(heal, (32, 30))
heal_rect = heal.get_rect()
heal_rect.topleft = (152, 450)

money = pygame.image.load("Images/Money.png")
money = pygame.transform.scale(money, (30, 30))
money_rect = balloon.get_rect()
money_rect.topleft = (152, 450)

shield = pygame.image.load("Images/Shield.png")
shield = pygame.transform.scale(shield, (28, 30))
shield_rect = shield.get_rect()
shield_rect.topleft = (152, 450)

spikes = pygame.image.load("Images/Spikes.png")
spikes = pygame.transform.scale(spikes, (33, 20))
spikes_rect = spikes.get_rect()
spikes_rect.topleft = (152, 450)


mus_playing = True

shield_sound = pygame.mixer.Sound("Sounds/crackling-dry-wood.wav")

live_lost_sound = pygame.mixer.Sound("Sounds/72d75b436239218.wav")

live_healing_sound = pygame.mixer.Sound("Sounds/healing-after-a-battle-in-a-computer-game.wav")

money_sound = pygame.mixer.Sound("Sounds/lost-money-on-the-game-account.wav")

game_over_sound = pygame.mixer.Sound("Sounds/a43faf51e2df0fc.wav")

pygame.mixer.music.load("Sounds/monplaisir-soundtrack.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
    if lives_var <= 0:
        end_text = font_end.render(f"Game over", True, (239, 62, 62))
        screen.blit(end_text, (60, 300))
        pygame.display.flip()
        continue
    if not paused:
        pygame.mixer.music.unpause()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 40 < mouse_x < 410:
            balloon_rect = balloon.get_rect()
            balloon_rect.x = mouse_x - 35
            balloon_rect.y = 450
            # if last_mouse_x >
            #
            # rotated = pygame.transform.rotate(balloon_img, angle)
            # balloon_rect = rotated.get_rect(center=balloon_rect.center)
            # balloon = rotated
            #
            # last_mouse_x = mouse_x - 35


        if obstacle_timer > min_distance:
            horizontal_spike_pos = random.randint(0, 420)
            vertical_spikes_pos = -(14 + random.randint(0, 200))
            spikes_number = random.randint(1, 3)
            for i in range(0, spikes_number):
                spike_in_list_rect = spikes.get_rect()
                spike_in_list_rect.x = horizontal_spike_pos + (i * 30)
                spike_in_list_rect.y = vertical_spikes_pos
                obstacles.append(spike_in_list_rect)
            obstacle_timer = 0
        if money_timer > money_min_distance:
            horizontal_money_pos = random.randint(0, 420)
            vertical_money_pos = -(14 + random.randint(0, 100))
            money_in_list_rect = money.get_rect()
            money_in_list_rect.x = horizontal_money_pos
            money_in_list_rect.y = vertical_money_pos
            money_list.append(money_in_list_rect)
            money_timer = 0
        if heal_timer > heal_min_distance:
            horizontal_heal_pos = random.randint(0, 420)
            vertical_heal_pos = -(14 + random.randint(0, 100))
            heal_in_list_rect = heal.get_rect()
            heal_in_list_rect.x = horizontal_heal_pos
            heal_in_list_rect.y = vertical_heal_pos
            heal_list.append(heal_in_list_rect)
            heal_timer = 0
        if shield_timer > shield_min_distance:
            horizontal_shield_pos = random.randint(0, 420)
            vertical_shield_pos = -(14 + random.randint(0, 100))
            shield_in_list_rect = shield.get_rect()
            shield_in_list_rect.x = horizontal_shield_pos
            shield_in_list_rect.y = vertical_shield_pos
            shield_list.append(shield_in_list_rect)
            shield_timer = 0



        for i in obstacles:
            i.y = i.y + speed
            if balloon_rect.colliderect(i):
                if (pygame.time.get_ticks() // 1000) - 10 >= shield_time:
                    shield_time = pygame.time.get_ticks() // 1000
                    balloon.set_alpha(128)
                    lives_var = lives_var - 1
                    obstacles.remove(i)
                    if lives_var <= 0:
                        pygame.mixer.music.fadeout(2000)
                        game_over_sound.set_volume(0.5)
                        game_over_sound.play()
                        continue
                    live_lost_sound.set_volume(0.1)
                    live_lost_sound.play()
            if i.y >= 790:
                obstacles.remove(i)
        for i in money_list:
            i.y = i.y + speed
            if balloon_rect.colliderect(i):
                money_var = money_var + 1
                money_list.remove(i)
                money_sound.set_volume(0.1)
                money_sound.play()
            if i.y >= 790:
                money_list.remove(i)
        for i in heal_list[:]:
            i.y = i.y + speed
            if balloon_rect.colliderect(i):
                heal_list.remove(i)
                lives_var = lives_var + 1
                live_healing_sound.set_volume(0.1)
                live_healing_sound.play()
            if i.y >= 790:
                heal_list.remove(i)
        for i in shield_list:
            i.y = i.y + speed
            if balloon_rect.colliderect(i):
                shield_list.remove(i)
                shield_sound.set_volume(0.1)
                shield_sound.play()
                shield_time = pygame.time.get_ticks() // 1000
                balloon.set_alpha(128)
            if i.y >= 790:
                shield_list.remove(i)
        screen.blit(bg, bg_rect)

        for i in obstacles:
            screen.blit(spikes, i)
        for i in money_list:
            screen.blit(money, i)
        for i in heal_list:
            screen.blit(heal, i)
        for i in shield_list:
            screen.blit(shield, i)
        screen.blit(balloon, balloon_rect)

        if (pygame.time.get_ticks() / 1000) - 7 >= shield_time:
            balloon.set_alpha(255)
        if (pygame.time.get_ticks() / 1000) - 7.5 >= shield_time:
            balloon.set_alpha(128)
        if (pygame.time.get_ticks() / 1000) - 8 >= shield_time:
            balloon.set_alpha(255)
        if (pygame.time.get_ticks() / 1000) - 8.5 >= shield_time:
            balloon.set_alpha(128)
        if (pygame.time.get_ticks() / 1000) - 9 >= shield_time:
            balloon.set_alpha(255)
        if (pygame.time.get_ticks() / 1000) - 9.5 >= shield_time:
            balloon.set_alpha(128)
        if (pygame.time.get_ticks() / 1000) - 10 >= shield_time:
            balloon.set_alpha(255)

        lives_text = font.render(f"Lives: {lives_var}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 10))

        money_text = font.render(f"Score: {money_var}", True, (255, 255, 255))
        screen.blit(money_text, (10, 40))

        info_text = font.render("P - Pause", True, (0, 0, 0))
        screen.blit(info_text, (10, 70))




        speed = speed + speed_adding
        obstacle_timer = obstacle_timer + 1
        money_timer = money_timer + 1
        heal_timer = heal_timer + 1
        shield_timer = shield_timer + 1
    else:
        pygame.mixer.music.pause()
        pause_text = font_end.render("PAUSE", True, (0, 0, 0))
        screen.blit(pause_text, (120, 300))

    pygame.display.flip()
    clock.tick(60)




