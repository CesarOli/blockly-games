#turtle_quatro

def pencil_color(color):
    print(color)

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')

def pencil_up(direction='up'):
    print(f'steps {direction}')

def pencil_down(direction='down'):
    print(f'steps {direction}')


pencil_color('yellow')
for count in range(0, 4):
    move(50)
    turn(144, 'right')
pencil_up()
move(150)
pencil_down()
move(20)