#maze_dez

def move_forward():
    print('move forward')

def turn_left():
    print('turn left')

def turn_right():
    print('turn right')

def is_path_ahead():
    return move_forward()

def is_path_left():
    return turn_left()

def is_path_right():
    return turn_right()

while not condition():
    if is_path_left():
        turn_left()
    if is_path_ahead():
        move_forward()
    else:
        turn_right()