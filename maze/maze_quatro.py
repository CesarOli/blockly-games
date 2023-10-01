#maze_quatro

def move_forward():
    print('move forward')

def turn_left():
    print('turn left')

def turn_right():
    print('turn right')

destination = 3
i = 0

while i <= destination:
    move_forward()
    turn_left()
    move_forward()
    turn_right()
    i += 1
