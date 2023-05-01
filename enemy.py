

class Enemy():
    rot_fac = PI/2
    a_sp = 5
    def __init__(self, p_img, a_img, posx, posy, ammo):
        self.p_img = p_img
        self.a_img = a_img
        self.position = PVector(posx, posy)
        self.ammo = ammo
        self.ammopos = PVector(self.position.x, self.position.y)
        
    def draw_(self):
        pushMatrix()
        imageMode(CENTER)
        translate(self.position.x, self.position.y)
        rotate(Enemy.rot_fac)
        image(self.p_img, 0, 0)
        popMatrix()
        
    def draw_ammo(self):
        pushMatrix()
        imageMode(CENTER)
        translate(self.ammopos.x, self.ammopos.y)
        rotate(Enemy.rot_fac)
        image(self.a_img, 0, 0)
        popMatrix()

        self.ammopos.x -= Enemy.a_sp
    
    
