from pygame import *
from random import *
img_hero = 'rocket.png'
img_back = 'galaxy.jpg'
img_ball = 'ufo.png'

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
        if keys[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 10 :
            self.rect.y -= self.speed

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y <700:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 10 :
            self.rect.y -= self.speed    

font.init()
font1 = font.SysFont('Arial', 36)
lost = False

class Ball(GameSprite):
    lost = False
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.x > 800:
            self.rect.x -= self.speed
        if self.rect.x < 0:
            self.speed = 5
        if self.rect.y < 600:
            self.speed = -5
        if self.rect.y > 0:
            self.speed = 5

        


win_width = 1000
win_height = 800
display.set_caption("Пинпонг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 20, win_height - 100, 80, 100, 10)
ship1 = Player1(img_hero, 900, 400, 80, 100, 10)
ball = Ball(img_ball, 400, 100, 50, 50, 10 )

finish = False
run = True


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
        ball.update()
        ball.reset()
        if lost == True:
            run = False

        #collides = sprite.groupcollide(monsters, bulls, True, True)
        #if collides:
        #    moster = Enemy('ufo.png', randint(80, 620), -50, 80, 50, randint(1, 3))
        #    monsters.add(moster)
        #    score+=1
        #    if top <= score:
        #        top+=1
        


    display.update()

    time.delay(15)
