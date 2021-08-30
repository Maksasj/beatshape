import pygame, sys , random

#from pygame.key import set_repeat
from sprites import Player , Wall , Point , Coin , Shield_Button

#Constants
player_color_r = 250
player_color_g = 120
player_color_b = 60
gameplay = False

WIDTH, HEIGHT = 640, 640

TITLE = "Beatshape"

pygame.init()
hit_sound = pygame.mixer.Sound("data/sounds/hit.wav")
coin_sound = pygame.mixer.Sound("data/sounds/coin.wav")
shield_sound = pygame.mixer.Sound("data/sounds/shield.wav")
main_music = pygame.mixer.music.load("data/sounds/main_theme.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)


logo = pygame.image.load("data/images/logo.png")
pygame.display.set_icon(logo)

text_font = pygame.font.Font('data/fonts/Minecraft.ttf',75)
score_font = pygame.font.Font('data/fonts/Minecraft.ttf',180)
highest_score_font = pygame.font.Font('data/fonts/Minecraft.ttf',35)
coin_font = pygame.font.Font('data/fonts/Minecraft.ttf',35)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

player = Player(WIDTH/2, HEIGHT/2)
point = Point(random.randint(40, 600) , random.randint(40, 600))
coin_sprite = Coin(-40 , -40)
shield_button = Shield_Button(-40 , -40)

walls = pygame.sprite.Group()

def name_text():
    text_name = text_font.render("Beatshape",True,(50,65,75))
    screen.blit(text_name, (WIDTH/2-195, HEIGHT/2-60))

def press_space_text(y_arc):
    press_space_text = highest_score_font.render("Press SPACE to start ",True,(50,65,75))
    text_rect = press_space_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.y += 270 + y_arc[0]
    screen.blit(press_space_text,  text_rect)

def coin_text():
    coin_text = coin_font.render("Coins: "+str(coin),True,(236, 245, 66))
    text_rect = coin_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.y += 295
    text_rect.x -= 240
    screen.blit(coin_text,  text_rect)
def level_text():
    level_text = coin_font.render("Level: "+str(level),True,(50,65,75))
    text_rect = level_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.y += 295
    text_rect.x += 240
    screen.blit(level_text,  text_rect)

level_speed = 1
level = 0
tick = 0
score = 0
coin = 0
players_shield = False

level_color = {}
level_color[0] = (12, 24, 36)

level_color[1] = (12, 24, 36) #Gray
level_color[2] = (18, 51, 32) #Green
level_color[3] = (224, 178, 92) #Orange
level_color[4] = (224, 92, 92) #Red
level_color[5] = (92, 136, 224) #Blue
level_color[6] = (147, 92, 224) #Purple
level_color[7] = (224, 92, 169) #Pink
level_color[0] = level_color[random.randint(1, 7)]

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


def dynamic_text(x , y , text , color ,font_size):
    dynamic_text_font = pygame.font.Font('data/fonts/Minecraft.ttf',font_size)
    dynamic_text = dynamic_text_font.render(str(text),True,color)
    text_rect = dynamic_text.get_rect(center = pygame.display.get_surface().get_rect().center)
    text_rect.x += x
    text_rect.y += y
    screen.blit(dynamic_text,  text_rect)

highest_score_text()
press_space_text(y_arc)

#Main Loop
while True:
    if gameplay == True:
        
        

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
                    
                    score = 0
                    coin = 0
                    level_speed = 1
                    level = 0

                    player.left_pressed = False
                    player.right_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False

                    player.x = WIDTH/2
                    player.y = HEIGHT/2
                    
                    level_color[0] = level_color[random.randint(1, 7)]
                    coin_sprite.x = -40
                    coin_sprite.y = -40
                    for y in walls:
                        y.kill()

                if event.key==pygame.K_SPACE: 
                    if coin > 0:
                        hit_sound.play()
                        mause = pygame.mouse.get_pos()
                        player.x = mause[0]-16
                        player.y = mause[1]-16
                        coin -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.left_pressed = False
                if event.key == pygame.K_d:
                    player.right_pressed = False
                if event.key == pygame.K_w:
                    player.up_pressed = False
                if event.key == pygame.K_s:
                    player.down_pressed = False

            if event.type == pygame.MOUSEBUTTONDOWN:           
                if shield_button.rect.collidepoint(pygame.mouse.get_pos()):
                    if (coin >= 3) and (players_shield == False):
                        coin -= 3
                        players_shield = True


            
        screen.fill(level_color[0]) 
        score_text()
        coin_text()
        level_text()

        if (coin >= 3) and (players_shield == False):
            shield_button.rect.x = 540
            shield_button.rect.y = 0

            shield_button.draw(screen , (50,65,75))

            point_s = pygame.Surface((48,48), pygame.SRCALPHA)   
            point_s.fill((0, 34, 255,point_particle[0]))                        
            screen.blit(point_s, (shield_button.rect.x+16,shield_button.rect.y+12))
            dynamic_text(260 , -282 , "Shield" , (92, 136, 224) ,15)
            dynamic_text(260 , -245 , "3 coins" , (236, 245, 66) ,16)
        else:
            shield_button.rect.x = -40
            shield_button.rect.y = -40

        tick += 1
        if tick > 100 - level_speed*2:     
            wall = Wall(random.randint(0, 620) , -20)
            walls.add(wall)
            tick = 0

        for x in walls:
            x.rect.y += level_speed - level*10
            x.draw(screen)
            if x.col(player):
                if players_shield == True:
                    shield_sound.play()
                    players_shield = False
                    x.kill()
                else:
                    if score > int(highest_score):
                        highest_score_file = open("data/highest_score.txt", "w")
                        highest_score_file.write(str(score))
                        highest_score_file.close()

                    hit_sound.play()
                    gameplay = False
                    score = 0
                    coin = 0
                    level_speed = 1
                    level = 0
                    players_shield = False

                    player.left_pressed = False
                    player.right_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False

                    player.x = WIDTH/2
                    player.y = HEIGHT/2
                    
                    level_color[0] = level_color[random.randint(1, 7)]
                    coin_sprite.x = -40
                    coin_sprite.y = -40

                    shield_button.x = -40
                    shield_button.y = -40
                    for y in walls:
                        y.kill()

            if x.rect.y >= 650:
                x.kill()
       

        if score != 0:
            if (score % 3 == 0) and (coin_sprite.rect.x < 0):
                coin_sprite.rect.x = random.randint(40, 600)
                coin_sprite.rect.y = random.randint(40, 600)

        if players_shield == True:
            point_s = pygame.Surface((48,48), pygame.SRCALPHA)   
            point_s.fill((0, 34, 255,point_particle[0]))                        
            screen.blit(point_s, (player.x-8,player.y-8))

        player.draw(screen,player_color_r,player_color_g,player_color_b)

        if score != 0:
            if score % 10 == 0:
                level_color[0] = level_color[random.randint(1, 7)]
                level_speed += 1
                level += 1  
                score += 1  

                for y in walls:
                    y.kill()

        

        point_s = pygame.Surface((32,32), pygame.SRCALPHA)   
        point_s.fill((66, 235, 90,point_particle[0]))                        
        screen.blit(point_s, (point.rect.x-8,point.rect.y-8))

        coin_particle = pygame.Surface((32,32), pygame.SRCALPHA)   
        coin_particle.fill((236, 245, 66,point_particle[0]))                        
        screen.blit(coin_particle, (coin_sprite.rect.x-8,coin_sprite.rect.y-8))

        point_particle[0] += point_particle[1]
        if point_particle[0] > 100:
            point_particle[1] *= -1

        if point_particle[0] < 20:
            point_particle[1] *= -1 

        pygame.draw.rect(screen,  point.color,  point.rect)
        pygame.draw.rect(screen,  coin_sprite.color,  coin_sprite.rect)

        if point.col(player) == True:
            score += 1
            level_speed += 1
            point.rect.x = random.randint(40, 600)
            point.rect.y = random.randint(40, 600)

        if coin_sprite.col(player) == True:
            coin_sound.play()
            coin += 1
            coin_sprite.rect.x = -40
            coin_sprite.rect.y = -40
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
        screen.fill(level_color[0]) 
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