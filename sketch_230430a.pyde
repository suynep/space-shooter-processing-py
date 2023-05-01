from player import Player
from enemy import Enemy


vel = 20


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
    global player, enemy
    starty = height / 2
    startx = p_img.width / 2 + 30
    player = Player(p_img, p_a_img, startx, starty, 100)
    enemy = Enemy(e1_img, e1_a_img, 700, starty, 100)

    
def draw():
    background(bg)
    player.draw_()
    enemy.draw_()
    enemy.draw_ammo()
    
    
    
def keyPressed():
    if keyCode == UP:
        player.position.y -= vel
    if keyCode == DOWN:
        player.position.y += vel
    if keyCode == RIGHT:
        player.position.x += vel
    if keyCode == LEFT:
        player.position.x -= vel
    
