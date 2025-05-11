from pygame import *
from random import randint

back = (255, 255, 255)
# score = 0 #сбито
# lost = 0 #пропущено
# max_lost = 100
# goal = 30
# life = 5

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

win_width = 600
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
window.fill(back)
player = Player('platform.png', 30, 200, 50, 150, 7)
player2 = Player('platform.png', 620, 200, 50, 150, 7)
ball = GameSprite('ball.png', 330, 250, 50, 50, 4)

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')

font.init()
font = font.SysFont('Arial', 70)
lose1 = font.render('PLAYER 1 LOSE', True, (255, 215, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (255, 215, 0))


clock = time.Clock()
FPS = 60

speed = 10

speed_x = 3
speed_y = 3

start_x = 5
start_y = 5
c = 9

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
              
    if finish != True:
        window.fill(back)
        player.update_l()
        player2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1  

   
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        player.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
    # if ball.rect.y > (350 + 20):
    #   time_text = Label(150, 150, 50, 50, blue)
    #   time_text.set_text('YOU LOSE', 60, (255,0,0))
    #   time_text.draw(10, 10)
    #   game_over = True
#         for c in collides:
#             score = score + 1
#             monster = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1, 5))
#             monsters.add(monster)
#             asteroid = Enemy('asteroid.png', randint(80, 620), -40, 80, 50, randint(1, 5))
#             asteroids.add(asteroid)

        # if sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
        #     sprite.spritecollide(player, monsters, True)
        #     sprite.spritecollide(player, asteroids, True)
        #     life = life - 1

#         if life == 0 or lost >= max_lost:
#             finish = True
#             window.blit(lose, (200, 200))

#         if score >= goal:
#             finish = True
#             window.blit(win, (200, 200))

#         text = font2.render('Счёт: ' + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))
#         text_lose = font2.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))
#         text_life = font2.render(str(life), 1, (255, 255, 255))
#         window.blit(text_life, (630, 50))
#         monsters.draw(window)
#         monsters.update()
#         bullets.draw(window)
#         bullets.update()
#         asteroids.draw(window)
#         asteroids.update()

    

#     if finish == True:
#         finish = False
#         score = 0
#         lost = 0
#         # num_fire = 0
#         life = 3
#         for b in bullets :
#             b.kill()
#         for m in monsters:
#             m.kill()
#         for a in asteroids:
#             a.kill()

#         time.delay(3000)
#         monsters = sprite.Group()
#         for i in range(1, 6):
#             monster = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1, 5))
#             monsters.add(monster)
#         asteroids = sprite.Group()
#         for i in range(1, 3):
#             asteroid = Enemy('asteroid.png', randint(80, 620), -40, 80, 50, randint(1, 5))
#             asteroids.add(asteroid)

    # time.delay(10)
    
    
    