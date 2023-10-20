#turtle_dois

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')


for count in range(0,4):
    move(100)
    turn(72, 'rigth')
    