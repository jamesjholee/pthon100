# D6 Exercise Roboth Hurdle 1 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    path()

# D6 Exercise Roboth Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

# D6 Exercise Roboth Hurdle 3
while not at_goal():
    if wall_in_fornt():
        jump()
    else:
        move()

# D6 Exercise Roboth Hurdle 4
def jump():
    turn_left()
    while while_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_fornt():
        jump()
    else:
        move()

# D6 Project Escape the Maze
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right():
        move()
    elif fornt_is_clear():
        move()
    else:
        turn_left()
