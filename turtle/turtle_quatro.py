#turtle_quatro

def pencil_color(color):
    print(color)

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')

def pencil(position):
    print('Now the pencil is {position}.')

pencil_color('yellow')
for count in range(0, 4):
    move(50)
    turn(144, 'right')
pencil('up')
move(150)
pencil('down')
move(20)