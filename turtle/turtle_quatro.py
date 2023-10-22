#turtle_quatro

def pencil_color(color):
    print(color)

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')

def select_direction(direction):
    print(f'To the {direction}')

pencil_color('yellow')
for count in range(0, 4):
    move(50)
    turn(144, 'right')
select_direction('up')
move(150)
select_direction('down')
move(20)