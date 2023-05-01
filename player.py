class Player():
    rot_fac = 3 * PI / 2

    a_sp = 10

    def __init__(self, p_img, a_img, posx, posy, ammo):
        self.p_img = p_img
        self.a_img = a_img
        self.position = PVector(posx, posy)
        self.ammo = ammo
        self.ammopos = PVector(self.position.x, self.position.y)
        
    def draw_(self):
        pushMatrix()
        imageMode(CENTER)
        rectMode(CENTER)
        noFill()
        strokeWeight(3)
        stroke(255)
        translate(self.position.x, self.position.y)
        rotate(Player.rot_fac)
        rect(0, 0, self.p_img.width, self.p_img.height)
        image(self.p_img, 0, 0)
        
        popMatrix()
    
    def draw_ammo(self):
        if self.ammo > 0:
            pushMatrix()
            # stroke(255)
            imageMode(CENTER)
            translate(self.ammopos.x, self.ammopos.y)
            rotate(Player.rot_fac)
            # rect(0, 0, self.a_img.width, self.a_img.height)
            image(self.a_img, 0, 0)
            popMatrix()
            self.ammopos.x += Player.a_sp
    

        
    
