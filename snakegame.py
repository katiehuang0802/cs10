
import turtle
import random
import time
"""
Running Program:
Type in terminal python MichelleCheung_ChuyingHuang_Snake.py to run the game.
You should use the arrow keys on your keyboard to play the game.
"""
#screen set up
screen = turtle.Screen()
screen.title("Snake")
screen.setup(width=650, height=650)
screen.tracer(0)

# Score
print_score = turtle.Turtle()
print_score.speed(0)
print_score.shape("square")
print_score.color("black")
print_score.penup()
print_score.hideturtle()
print_score.setposition(0, 300)
print_score.write("Score: 0", align= "center", font=("Times New Roman", 20))

#Grid
board_width = 600
board_height = 600
rows = 30
cols = 30

draw = turtle.Turtle()
draw.hideturtle()
draw.speed(speed = 0)
draw.penup()
draw.setposition(-290,290) #left corner
draw.pendown()

"""
Draw the border
"""

for i in range(0,2):
    draw.forward(board_width)
    draw.right(90)
    draw.forward(board_height)
    draw.right(90)

rowsteps = board_width/cols
colsteps = board_height/rows
"""
Draw Vertical Lines
"""
for i in range(0, int(rows/2)):
    draw.forward(rowsteps)
    draw.right(90)
    draw.forward(board_height)
    draw.left(90)
    draw.forward(rowsteps)
    draw.left(90)
    draw.forward(board_height)
    draw.right(90)
"""
Draw Hortizontal Lines
"""
for i in range(0, int(cols/2)):
    draw.right(90)
    draw.forward(colsteps)
    draw.right(90)
    draw.forward(board_width)
    draw.left(90)
    draw.forward(colsteps)
    draw.left(90)
    draw.forward(board_width)


# Front of the Snake
front = turtle.Turtle()
front.penup()
front.color("#8b008b")
front.shape("square")
front.speed(0)
front.setposition(0,0)
front.setheading(-0.01) #when game is set up the snake is stopped

#Apple
"""
creates first apple object on the screen. all following apples will
be "new_apple" objects.
"""
apple = turtle.Turtle()
apple.penup()
apple.color("#DC143C")
apple.speed(0)
apple.shape("circle")
apple.setposition(-20,20)

#Keyboard Functions
"""
90 = north = up
270 = south = down
180 = west = left
0 = east = right

These 4 functions below set the heading direction of the snake.
"""

def moveup(): #sets the heading to up
    if front.heading() != 270: #this prevents snake from running into itself
        front.seth(90)

def movedown(): #sets heading to down
    if front.heading() != 90:
        front.seth(270)

def moveleft(): #sets heading to left
    if front.heading() != 0:
        front.seth(180)

def moveright(): #sets heading to right
    if front.heading() != 180:
        front.seth(0)

def movement():
    """
    The snake will move 20 pixels in the direction it is heading.
    """
    if front.heading()  == 90:
        y = front.ycor()
        front.sety(y + 20)
    if front.heading()  == 270:
        y = front.ycor()
        front.sety(y - 20)
    if front.heading()  == 180:
        x = front.xcor()
        front.setx(x - 20)
    if front.heading()  == 0:
        x = front.xcor()
        front.setx(x + 20)

#Keyboard Controls
screen.listen()
screen.onkey(moveup, "Up")
screen.onkey(movedown, "Down")
screen.onkey(moveright, "Right")
screen.onkey(moveleft, "Left")

parts = []
apples = [apple]

def new_apple_position(x, y):
    """
    This function takes in two coordinates and subtracts the remainder from
    dividing the number by 20 to get a new set of coordinates that
    is added to a list called new_values. The point of this is
    to make it so when updating new randomly placed apples on the
    screen, the apples appear inside a box in the grid. We divide by 20 because
    each box in the grid is 20 pixels in size.
    """
    """
    Helper function.
    Test Case 1:
    new_apple_position(17,8) == [0,0]
    This test case should return True because
    17 % 20 = 17 and 17 - 17 = 0, so x = 0. For y,
    8 % 20 = 8 and 8 - 8 = 0, so y = 0. Therefore,
    new_apple_position(17,8) would return a list of
    x and y which is [0,0].

    Test Case 2:
    new_apple_position(188,134) == [180,120]
    This test case should return True because
    188 % 20 = 8 and 188 - 8 = 180, so x = 180. For y,
    134 % 20 = 14 and 134 - 14 = 120, so y = 120. Therefore,
    new_apple_position(188,134) would return a list of
    x and y which is [180,120].

    """
    new_values = []
    if x/20 != 0:
        difference = x % 20
        x = x - difference
        new_values.append(x)
    if y/20 != 0:
        difference = y % 20
        y = y - difference
        new_values.append(y)
    return new_values

def apple_collision(apples, parts):
    """
    This block takes in the lists apples and parts. First, it checks if the
    position (coordinates) of the apple on the screen is the same as the
    front of the snake. If so, that means the snake has eaten the apple.
    The code says apples[0] since it is taking the first apple out of a
    list called "apples". This list only holds one apple at a time, but
    it is a list because it helps facilitate transfering
    apples to the "parts" list.

    Next, it creates a new apple (new_apple) which is a new turtle object.
    It then adds the new apple to the "apples" list and adds the eaten, old
    apple to the "parts" list. It then deletes the eaten apple, from the
    "apples" list. The point of adding the eaten apple to the "parts" list
    is so the eaten apple can become a body part of the snake. This will
    get rid of the eaten apple from the screen and the new apple will be
    the only apple on the screen.

    Then, we use a helper function new_apple_position() which outputs a set of
    random coordinates on the grid and set the new apple's position to that.

    Lastly, the score increases by 1, which is represented by the length
    of the list "parts" since that's how many apples were eaten.
    """
    if front.position() == apples[0].position():

        #create new apple
        new_apple = turtle.Turtle()
        new_apple.penup()
        new_apple.color("#DC143C")
        new_apple.speed(0)
        new_apple.shape("circle")

        #add eaten apple to parts list and add new apple to apples list
        #delete old apple from apples list
        apples.append(new_apple)
        parts.append(apples[0])
        apples.pop(0)

        #set new apple to a random position in the grid
        x = round(random.randint(-280,280))
        y = round(random.randint(-280,280))
        new = new_apple_position(x, y)
        r = new[0]
        c = new[1]
        apples[0].setposition(r,c)

        #increase the score by 1 each time a apple is eaten
        score = len(parts)
        print_score.clear()
        print_score.write("Score: {}".format(score), align = "center", font = ("Times New Roman", 20))

def body_parts(parts):
    """
    This function takes in the list parts, which now contains all the apples
    that were eaten. We use a for loop that counts down, so that it addresses
    the all the items in the parts list except for the first item. This makes
    all those items in the parts list, which are still apples, to a green
    square so it will look like a snake body part and not an apple. Then
    it sets each part to the coordinates of the part in front of it. We used
    a list to store the coordinates and use an index called "r" to set the
    parts to the coordinates in the list.

    For the first item in the list, which is the part closest to the front
    of the snake, we set that to the position of the front.

    """
    location = []
    r = 0
    for i in range(len(parts)-1, 0, -1):
        parts[i].shape("square")
        parts[i].color("#228B22")
        x = parts[i-1].xcor()
        y = parts[i-1].ycor()
        location.append([x,y])
        r += 1
        coordinates = location[r-1]
        x = coordinates[0]
        y = coordinates[1]
        parts[i].setposition(x,y)

    #Set first part to front coordinates
    if len(parts) > 0:
        x = front.xcor()
        y = front.ycor()
        parts[0].shape("square")
        parts[0].color("#228B22")
        parts[0].setposition(x,y)
    '''
    For description purposes I will be labeling turtle objects as "part #"
    Test Case 1:
    parts = ["part 1"]
    body_parts(parts) ==> there is no output but this will
    basically set the position of the first body part to the position of the
    front of the snake. Then, it will make the turtles square and green.
    Test Case 1:
    parts = ["part 1","part 2"]
    body_parts(parts) ==> Again no output but will
    first set part 2 to the position of part 1 and then set part 1
    to the position of the front of the snake. It will also make
    the turtles square and green.

    '''

#Main Game Code

while True:
    screen.update()

    """
    These three functions' descriptions are above.
    """
    apple_collision(apples, parts)
    body_parts(parts)
    movement()

    """
    Body Collisions:
    This section of code below checks for collisions with the snake's
    body parts. It checks for each body part in the list of parts to see if any
    of the positions (coordinates) of the body parts are also a the same
    position of the front of the snake (the purple head). If so, that means
    that the head has collided with a section of the body. It sends the
    front of the snake back to (0,0). Then, it deletes the body parts by
    hiding them offscreen and sets the score to zero.
    """
    for part in parts:
        if part.position() == front.position():
            time.sleep(1)
            front.setposition(0,0)
            front.setheading(-0.01)

            #Hide the body parts
            for part in parts:
                part.setposition(800,800)

            #Set score to 0
            parts = []
            score = len(parts)
            print_score.clear()
            print_score.write("Score: {}".format(score), align = "center", font = ("Times New Roman", 20))
    """
    Border Collisions:
    This section of code below checks for collisions with the border of
    the grid. It checks the coordinates of the front of the snake to
    see if it has passed the edge of the border. If it does pass
    those coordinates, it sends the front of the snake back to (0,0).
    Then, it deletes the body parts by hiding them
    offscreen and sets the score to zero.
    """
    #Collision with border, if True, send snake back to (0,0)
    if front.ycor()>280 or front.ycor()<-300:
        front.setposition(0,0)
        front.setheading(-0.01)
        time.sleep(1.2)
    elif front.xcor()>300 or front.xcor()<-280:
        front.setposition(0,0)
        front.setheading(-0.01)
        time.sleep(1.2)

        #Hide the body parts
        for part in parts:
            part.setposition(800,800)
        #Set score to 0
        parts = []
        score = len(parts)
        print_score.clear()
        print_score.write("Score: {}".format(score), align = "center", font = ("Times New Roman", 20))

    time.sleep(0.2) #delay so the snake doesn't move so fast

screen.done()
