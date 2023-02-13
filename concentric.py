from turtle import*

#code to create concentric square
speed('fastest')
pencolor ('red')
for i in range(100):
    fd(i*3+5)
    lt(90)
    
hideturtle
mainloop()