from pygame import *
img_hero = 'racket.png'
img_back = 'galaxy.jpg'
img_ball = 'tenis_ball.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 660:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 10 :
            self.rect.y -= self.speed

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 660:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 10 :
            self.rect.y -= self.speed    


  
win_width = 1000
win_height = 800
display.set_caption("Пинпонг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 20, 380, 50, 140, 10)
ship1 = Player1(img_hero, 930, 350, 50, 140, 10)
ball = GameSprite(img_ball, 400, 100, 50, 50, 5)

finish = False
run = True
clock = time.Clock()
FPS = 60

check = 0
check1 = 0
speed_x = 5
speed_y = 5

font.init()
font = font.Font(None, 70)
win1 = font.render('Пебедил первый игрок', True, (255, 0, 0))
win2 = font.render('Пебедил второй игрок', True, (255, 0, 0))

count1 = font.render('Счёт:' + str(check), True, (0, 255, 0))
count2 = font.render('Счёт:' + str(check1), True, (0, 255, 0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background,(0,0))

        ship.update()
        ship.reset()
        ship1.update()
        ship1.reset()
        ball.reset()
        window.blit(count1, (10, 20))
        window.blit(count2, (830, 20))
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > win_width - 50 or ball.rect.x < 0:
            speed_x *= -1

        if sprite.collide_rect(ship, ball) or sprite.collide_rect(ship1, ball):
            speed_x *= -1

        if sprite.collide_rect(ship, ball):
            check += 1
            count1 = font.render('Счёт:' + str(check), True, (0, 255, 0))
        
        if sprite.collide_rect(ship1, ball):
            check1 += 1
            count2 = font.render('Счёт:' + str(check1), True, (0, 255, 0))

        if ball.rect.x > ship1.rect.x:
            finish = True
            window.blit(win1, (250, 300))

        if ball.rect.x < ship.rect.x:
            finish = True
            window.blit(win2, (250, 300))

    display.update()

    time.delay(15)

