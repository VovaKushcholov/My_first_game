#Створи власний Шутер!
from random import randint
from pygame import *
from time import time as t
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire = mixer.Sound('fire.ogg')
bullets = sprite.Group(

)

clock = time.Clock()
FPS = 60
clock.tick(FPS)
lost = 0
kills = 0

window = display.set_mode((700,500))
display.set_caption("Ienth")
background =transform.scale(
    image.load("galaxy.jpg"),
        (700,500)
    )
window.blit(background,(0,0))



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_height,player_width,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    
class Player(GameSprite):
    def update (self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',15,20,self.rect.centerx,self.rect.top,5)
        bullets.add(bullet)

class Enemy(GameSprite):
    direction = 'down'
    
    def update(self):
        global lost , text_lose
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(0,600)
            self.rect.y = 0
            lost += 1
            text_lose = font1.render(
                'Пропущено ' + str(lost), 1 , (255,255,255)
                )
class Asteroids(GameSprite):
    direction = 'down'
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(0,600)
            self.rect.y = 0
player = Player("rocket.png",80,50,0,420,2)

Ufo1 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,0,1)
Ufo2 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,25,1)
Ufo3 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,50,1)
Ufo4 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,75,1)
Ufo5 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,100,1)
Ufo6 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,75,1)
Ufo7 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,50,1)
Ufo8 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,25,1)
Ufo9 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,0,1)
Ufo10 = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,10,1)

asteroid1 =Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-10,1)
asteroid2 =Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-20,1)
asteroid3 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-30,1)
asteroid4 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-40,1)
asteroid5 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-50,1)
asteroid6 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-60,1)
asteroid7 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-70,1)
asteroid8 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-80,1)
asteroid9 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-90,1)
asteroid10 = Asteroids('asteroid.png',randint(50,100),randint(50,100),randint(0,600) ,-100,1)


asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
asteroids.add(asteroid4)
asteroids.add(asteroid5)
asteroids.add(asteroid6)
asteroids.add(asteroid7)
asteroids.add(asteroid8)
asteroids.add(asteroid9)
asteroids.add(asteroid10)

monsters = sprite.Group()
monsters.add(Ufo1)
monsters.add(Ufo2)
monsters.add(Ufo3)
monsters.add(Ufo4)
monsters.add(Ufo5)
monsters.add(Ufo6)
monsters.add(Ufo7)
monsters.add(Ufo8)
monsters.add(Ufo9)
monsters.add(Ufo10)

font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',100)

win = font2.render(
    'VICTORY', 1 , (0,255,0)
)
lose = font2.render(
    'GAME OVER', 1 , (255,0,0)
)

bullets_in_roket = 10
kills = 0
finish = False
game = True
num_fire = 0 
reload_t = False
player_lives = 3 
while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 10 and reload_t != True:
                    player.fire()
                    bullets_in_roket -= 1
                    num_fire += 1

                if num_fire >= 10 and reload_t != True:
                        reload_t = True
                        start = t()

                        

          

    text_lose = font1.render(
        'Пропущено ' + str(lost), 1 , (255,255,255)
    )    
    text_kills = font1.render(
        'Знищено ' + str(kills), 1 , (255,255,255)
    )  
    text_bullets = font1.render(
        'Патронів ' + str(bullets_in_roket), 1 , (255,255,255)
    )      

    live = font2.render(
        str(player_lives), 1 , (178, 34, 34)
    )

    if finish != True:
        
        window.blit(background,(0,0))
        player.reset()
        player.update()
        
        monsters.draw(window)
        monsters.update()

        asteroids.draw(window)
        asteroids.update()

        bullets.draw(window)
        bullets.update()

        text_lose = font1.render(
            'Пропущено ' + str(lost), 1 , (255,255,255)
        )
        


        sprite_list = sprite.groupcollide(
            monsters, bullets, True, True
        )
        
        ship = sprite.spritecollide(
            player , monsters, True
        )
        
        for lives in ship:
            player_lives -= 1
            Ufo = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,0,1)
        
        if player_lives == 3: 
            live = font2.render(
                str(player_lives), 1 , (124, 252, 0)
            )   
        if player_lives == 2:
            live = font2.render(
                str(player_lives), 1 , (255, 215, 0)
            )   
        if player_lives == 1:
            live = font2.render(
                str(player_lives), 1 , (178, 34, 34)
            )
        if player_lives == 0:
            live = font2.render(
                str(player_lives), 1 , (178, 34, 34)
            )
            monsters.add(Ufo)
        for moster in sprite_list:
            kills += 1 
            Ufo = Enemy('ufo.png',randint(50,100),randint(50,100),randint(0,600) ,0,1)
            monsters.add(Ufo)
        window.blit(text_lose,(0,0))
        window.blit(text_kills,(0,40))
        window.blit(text_bullets,(560,0))
        window.blit(live,( 300, 0))
        if reload_t == True:
            end = t()
            reload_num = end - start
            text_reload = font1.render(
                'Wait for reload ' + str(reload_num), 1 , (255,0,0)
                )  
            window.blit(text_reload,(200,400))
            
            if reload_num >= 2:
                num_fire = 0
                bullets_in_roket = 10
                reload_t = False 


        if lost == 15 or player_lives <= 0:
            window.blit(lose,(150,200))  
            finish = True
        if kills == 25:
            window.blit(win,(150,200) )
            finish = True
        
    display.update()
    clock.tick(60) 
