import random, turtle, time, os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.colors import is_color_like

win_size = 500
turtle.screensize(win_size,win_size)
turtle.title('Turtle Race')

class Turtle:
    def __init__(self, color, pos):
        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle')
        self.turtle.color(color)
        self.color = color
        self.start = (0,0)
        self.pos = pos
        self.turtle.penup()
        self.turtle.setpos(pos)
        self.turtle.setheading(0)

    def move(self):
        self.turtle.pendown()
        r = random.randint(1,16)
        self.turtle.forward(r)
        self.pos = (self.pos[0] + r, self.pos[1])

class GameTracker:
    def __init__(self, total_games):
        self.total_games = total_games
        self.num_games = 0

# Get number of games
while True:
    try:
        total_games = input('Number of games: ')
        convert_val = int(total_games)
        break # only if input is valid
    except ValueError:
        continue
game_tracker = GameTracker(convert_val)

# Get number of turtles 
num_turtles = int(input('Number of turtles (2-10): '))
while num_turtles not in range(2, 11):
    num_turtles = int(input('Number of turtles (2-10): '))

# For each turtle, ask for a color
chosen_colors = []
option = input('Auto or Choose (y/n)? ')
if option == 'n':
    for i in range(num_turtles):
        t_color = input('Color for turtle ' + str(i+1) + ': ')
        # need better method to find if color string is valid for tk color specification color values
        # also create an auto function to choose random colors
        while is_color_like(str(t_color)) == False or t_color in chosen_colors:
            t_color = input('Color for turtle ' + str(i+1) + ' (please enter a valid color): ')
        chosen_colors.append(t_color)
if option == 'y':
    colors = ['Red', 'Orange', 'Pink', 'Purple', 'Blue', 'Cyan', 'Green', 'Gray', 'Black', 'Brown', 'Yellow', 'Gold']
    random.shuffle(colors)
    for i in range(num_turtles):
        chosen_colors.append(colors[i])

# Create/ reset file 
file = open('score.txt', 'w')
for color in chosen_colors:
    file.write(color + ': 0\n')
# Delete last new line
file.close()

def game():
    # image = os.path.join('Assets', 'landscape.png')
    # turtle.bgpic(image)
    turtles = []
    start = -(win_size/2) + (230//num_turtles)
    for t in range(num_turtles):
            y_pos = start + t*(win_size)//num_turtles
            new_turtle = Turtle(chosen_colors[t], (-300, y_pos))
            turtles.append(new_turtle)

    running = True
    # time.sleep(3)
    while running:
        winner = []
        for t in turtles:
            if t.pos[0] < 300: 
                t.move()
            else:
                turtle.clearscreen()
                time.sleep(.1)
                game_tracker.num_games += 1
                # update file score after each win
                if game_tracker.num_games >= game_tracker.total_games:
                    turtle.bye()
                    break
                else:
                    game()

game()