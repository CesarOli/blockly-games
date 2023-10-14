#turtle_um

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')

for count in range(0,3):
    move(100, 'forward')
    turn(90, 'rigth')

