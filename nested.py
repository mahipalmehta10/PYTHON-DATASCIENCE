from turtle import*
speed('fastest')
pencolor('red')
fillcolor('blue')
for i in range(6):
    fd(100)
    #write(i)   #prints the index
    for i in range(6):
        fd(50)
        begin_fill()
        for i in range(6):
            fd(25)
            lt(60)
        end_fill()
        lt(60)
    rt(60)

hideturtle()
mainloop()