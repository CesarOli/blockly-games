#turn_três

def pencil_color(color):
    print(color)

def move(length, direction='forward'):
    print(f'move {length} steps {direction}')

def turn(angle, side):
    print(f'turn {angle} to the {side}')


pencil_color('yellow')
for count in range(0, 4):
    move(100)
    turn(144, 'rigth')
    
