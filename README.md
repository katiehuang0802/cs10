# CS10 Final Project: Snake Game
Project Member: Katie Huang & Michelle Cheung

Introduction Video to Snake Game: https://youtu.be/SBzzdIxevns


Features in Snake Game:

*Make the snake move in any direction it wants: the player can choose what directions they want to go to from left, right, up, down.

*The snake eats apples and grows bigger after eating apples: when the player makes the snake cross the apple, the apple will disappear and the snake will grow bigger.

*The game will be over when the snake hits the wall or crash itself: when the head of the snake touches the wall(border) or the snake’s head touches its body, the game will be over.


Techniques to implement the features:

*Lists: 

We use a list called “parts” to keep track of the body parts of the snake which were individual sprites (turtles). We also used a list called “location” to keep track of the coordinates of the snake’s body parts. There was also a list called “apples” to keep track of the apples.

*Local variables:

There were many local variables used. There are some called x and y in several sections of the code. Line 230 is the x-variable that represents the x-coordinates of the apple and it can let the new apple show up in random place on board. Line 231 is the y-variable that represents the y-coordinates of the apple. Line 262 is the x-variables that represent the x-coordinates of the body part of the snake, line 263 is the y-variables that represent the y-coordinates of the body part of the snake. There is also the local variable “r”, “c”, and “score.”


Python Version: Python 2.7.2


Way to run and operate the program: Type in terminal “python MichelleCheung_ChuyingHuang_Snake.py” to run the game. You should use the arrow keys on your keyboard to play the game. 


Cited Resources;

We imported turtle, time, and random to our project.

https://docs.python.org/3.7/library/turtle.html

https://docs.python.org/3/library/time.html

https://docs.python.org/3/library/random.html
