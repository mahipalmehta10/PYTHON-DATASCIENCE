from turtle import*
speed ('fastest')

#create a hexagon
size=50
side=10

for i in range(side):
     fd(size) #forward can be written as fd
     left(360/side)
     write (i)     # and this can be written as lt
hideturtle()  # hide turtle
mainloop()    # keep the window open
