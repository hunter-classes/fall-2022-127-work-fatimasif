import turtle 


def square(t,x,y,w,color,sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw a square
    for i in range (4):
        t.forward(sidelen)
        t.right(90)
        
def triangle (t,x,y,w,color,sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw a triangle
    for i in range (3):
        t.forward(sidelen)
        t.right(120)
    
def ngon(t,x,y,w,color,sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw an octogon
    for i in range (8):
        t.forward(sidelen)
        t.right(45)
        
def hexagon(t,x,y,w,color,sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    #draw an octogon
    for i in range (6):
        t.forward(sidelen)
        t.right(300)


wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush, -50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)

triangle(crush,50,50,1,"purple",50)

ngon(crush,-90,70,2,"pink",80)

hexagon(crush,-20,20,2,"orange",80)


#squirt.penup()
#squirt.goto(100,100)
#squirt.pendown()
#squirt.color("red")
#squirt.width(5)
#square(squirt)


wn.exitonclick()
wn.mainloop()