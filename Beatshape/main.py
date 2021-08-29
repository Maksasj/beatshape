import pygame, sys , random

from pygame.key import set_repeat
from sprites import Player , Wall , Point

#Constants
player_color_r = 250
player_color_g = 120
player_color_b = 60
gameplay = False

WIDTH, HEIGHT = 640, 640

TITLE = "Beatshape"

pygame.init()
hit_sound = pygame.mixer.Sound("data/sounds/hit.wav")
main_music = pygame.mixer.music.load("data/sounds/main_theme.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)


logo = pygame.image.load("data/images/logo.png")
pygame.display.set_icon(logo)

text_font = pygame.font.Font('data/fonts/Minecraft.ttf',75)
score_font = pygame.font.Font('data/fonts/Minecraft.ttf',180)
highest_score_font = pygame.font.Font('data/fonts/Minecraft.ttf',35)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

player = Player(WIDTH/2, HEIGHT/2)
point = Point(random.randint(40, 600) , random.randint(40, 600))

walls = pygame.sprite.Group()

def name_text():
    text_name = text_font.render("Beatshape",True,(50,65,75))
    screen.blit(text_name, (WIDTH/2-195, HEIGHT/2-60))

def press_space_text(y_arc):
    press_space_text = highest_score_font.render("Press SPACE to start ",True,(50,65,75))
    text_rect = press_space_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.y += 270 + y_arc[0]
    screen.blit(press_space_text,  text_rect)

level_speed = 1
tick = 0
score = 0
point_particle = {}
point_particle[0] = 90
point_particle[1] = 1
y_arc = {}
y_arc[0] = 0
y_arc[1] = 0.10

highest_score_file = open("data/highest_score.txt", "r")
highest_score = highest_score_file.read()
highest_score_file.close()


def highest_score_text():
    highest_score_file = open("data/highest_score.txt", "r")
    highest_score = highest_score_file.read()
    highest_score_file.close()

    score_text = highest_score_font.render("Highest score: "+str(highest_score),True,(50,65,75))
    text_rect = score_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.y += 40
    screen.blit(score_text,  text_rect)

def score_text():
    score_text = score_font.render(str(score),True,(50,65,75))
    text_rect = score_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    screen.blit(score_text,  text_rect)
highest_score_text()
press_space_text(y_arc)

#Main Loop
while True:
    if gameplay == True:
        
        tick += 1
        if tick > 100-level_speed*2:     
            wall = Wall(random.randint(0, 640) , -20)
            walls.add(wall)
            tick = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.left_pressed = True
                if event.key == pygame.K_d:
                    player.right_pressed = True
                if event.key == pygame.K_w:
                    player.up_pressed = True
                if event.key == pygame.K_s:
                    player.down_pressed = True
                if event.key==pygame.K_ESCAPE: 
                    hit_sound.play()
                    gameplay = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.left_pressed = False
                if event.key == pygame.K_d:
                    player.right_pressed = False
                if event.key == pygame.K_w:
                    player.up_pressed = False
                if event.key == pygame.K_s:
                    player.down_pressed = False
            
        screen.fill((12, 24, 36)) 
        score_text()
        
        for x in walls:
            x.rect.y += level_speed
            x.draw(screen)
            if x.col(player):
                if score > int(highest_score):
                    highest_score_file = open("data/highest_score.txt", "w")
                    highest_score_file.write(str(score))
                    highest_score_file.close()

                hit_sound.play()
                gameplay = False
                score = 0
                level_speed = 1

                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False

                player.x = WIDTH/2
                player.y = HEIGHT/2
                for y in walls:
                    y.kill()

            if x.rect.y >= 650:
                x.kill()
       


        player.draw(screen,player_color_r,player_color_g,player_color_b)
        #point.draw(screen)
        
        s = pygame.Surface((32,32), pygame.SRCALPHA)   
        s.fill((66, 235, 90,point_particle[0]))                        
        screen.blit(s, (point.rect.x-8,point.rect.y-8))

        point_particle[0] += point_particle[1]
        if point_particle[0] > 100:
            point_particle[1] *= -1

        if point_particle[0] < 20:
            point_particle[1] *= -1 

        pygame.draw.rect(screen,  point.color,  point.rect)
       

        if point.col(player) == True:
            score += 1
            level_speed += 1
            point.rect.x = random.randint(40, 600)
            point.rect.y = random.randint(40, 600)


        if player.x >= 639:
            player.x = 2
        if player.x <= 1:
            player.x = 638

        if player.y >= 639:
            player.y = 2
        if player.y <= 1:
            player.y = 638

        if player_color_r > 50: player_color_r -= 5
        if player_color_r < 50: player_color_r = 255

        if player_color_g > 50: player_color_g -= 4
        if player_color_g < 50: player_color_g = 255

        if player_color_b > 50: player_color_b -= 3
        if player_color_b < 50: player_color_b = 255

    

        player.update()
    else:
        screen.fill((12, 24, 36)) 
        name_text()
        highest_score_text()

        press_space_text(y_arc)
        y_arc[0] += y_arc[1]
        if y_arc[0] > 7:
            y_arc[1] *= -1
        if y_arc[0] < 0:
            y_arc[1] *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE: 
                    hit_sound.play()
                    gameplay = True
                if event.key==pygame.K_ESCAPE: 
                    sys.exit()
    pygame.display.flip()
    clock.tick(120)