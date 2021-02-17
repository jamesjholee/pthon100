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
# D6 Exercise Roboth Hurdle 5 
# D6 Project Escape the Maze
