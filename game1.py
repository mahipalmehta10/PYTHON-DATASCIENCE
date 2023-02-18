#variable used in function is called local variable and those written outside is called gloabal variable

import pgzrun

music.play('bcg') #adding music

b=Rect((50,50),(100,50))
# vx = 2  #velocity in x axis ,global variable
# vy=1
vx,vy=4,1

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b,'blue')

def update():
    global vx,vy #to tell that vx is global
    b.x += vx
    b.y += vy
    if b.right >800 or b.left <0: #width of screen is 800 and left corner is zero
       vx= -vx
       sounds.s1.play()
    if b.bottom >600 or b.top<0:
        vy = -vy 
        sounds.s1.play()

#outside of all functions
pgzrun.go()