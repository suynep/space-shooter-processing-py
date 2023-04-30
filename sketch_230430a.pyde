def setup():
    size(400, 400)
    x = loadImage('pngegg.png')
    imageMode(CENTER)


def draw():
    background(0)
    image(x, width/2, height/2, 50, 50)
