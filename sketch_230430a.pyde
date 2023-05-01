from player import Player
from enemy import Enemy
import random

vel = 20
e = []
e_count = 5
e_name = [i for i in range(e_count)]

def check_ammo_collision(p, a):
    if dist(p.position.x - p.p_img.height/2, p.position.y, a.ammopos.x + a.a_img.height/2, a.ammopos.y) < (p.p_img.height/2 + a.a_img.height/2 - 50):
        return True
    
        
    
        
def setup():
    size(1500, 800)
    global bg 
    bg = loadImage('spacebg.png')
    player_full = loadImage('level2player.png')
    p_img = player_full.get(0, 0, player_full.width/2, player_full.height)
    p_a_img = player_full.get(player_full.width/2, 0, player_full.width/2, player_full.height)
    enemy2_full = loadImage('enemy2.png')
    e2_img = enemy2_full.get(0, 0, enemy2_full.width/2, enemy2_full.height)
    e2_a_img = enemy2_full.get(enemy2_full.width/2, 0, enemy2_full.width/2, enemy2_full.height)
    enemy1_full = loadImage('enemy.png')
    e1_img = enemy1_full.get(0, 0, enemy1_full.width/2, enemy1_full.height)
    e1_a_img = enemy1_full.get(enemy1_full.width/2, 0, enemy1_full.width/2, enemy1_full.height)
    
    ## PLAYER/ENEMY INIT
    global player
    starty = height / 2
    startx = p_img.width / 2 + 30
    
    p_img.resize(0, 100)
    p_a_img.resize(0, 100)
    e1_img.resize(0, 100)
    e1_a_img.resize(0, 100)
    
    player = Player(p_img, p_a_img, startx, starty, 100)
    
    for i in range(e_count):
        enemy = Enemy(e1_img, e1_a_img, 1400, starty + random.randint(-200, 200), 100)
        e.append((i, enemy))
        
    global enemies
    enemies = dict(e)
    
    print(p_img.width, p_img.height)
    
    
    
def draw():
    background(bg)
    
    player.draw_()
    player.draw_ammo()
    

    
    for i in e_name:
        enemies[i].draw_()
        enemies[i].draw_ammo()
        if check_ammo_collision(enemies[i], player):
            del enemies[i]
            e_name.remove(i)
    

    
    
    

        
def keyPressed():
    if keyCode == UP:
        player.position.y -= vel
    if keyCode == DOWN:
        player.position.y += vel
    if keyCode == RIGHT:
        player.position.x += vel
    if keyCode == LEFT:
        player.position.x -= vel
