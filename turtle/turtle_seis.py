#turtle_seis

def pencil_color(color):
    print(color)

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')

def pencil(position):
    print('Now the pencil is {position}.')

pencil_color('Yellow')
for count in range(0, 2):
    for count1 in range(0, 4):
        move(50)
        turn(144, 'right')
    pencil('up')    
    move(150)
    pencil('down')
    turn(120, 'right')
turn(90, 'left')
pencil('up')
pencil_color('white')
move(100)
pencil('down')
move(50)
