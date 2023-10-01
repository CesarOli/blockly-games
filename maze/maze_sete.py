#maze_sete

def move_forward():
    print('move forward')

def turn_right():
    print('turn right')

def is_path_ahead():
    return move_forward()

def is_path_right():
    return turn_right()

while not condition:
    if is_path_right():
        turn_right()
    move_forward()