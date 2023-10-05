#bird_quatro

worm_captured = False

def heading(angle):
    print('new angle = ' + angle)

def get_x_position():
    print('the current x position should be returned here.')

if get_x_position() < 80:
    heading(0)
else:
    heading(270)