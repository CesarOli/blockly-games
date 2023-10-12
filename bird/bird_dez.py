#bird_dez

worm_captured = False

def heading(angle):
    print('new angle = ' + angle)

def does_not_have_worm():
    if worm_captured:
        return False
    else:
        return True
    
def get_y_position():
    print('the current y position should be returned here.')

def get_x_position():
    print('the current x position should be returned here.')


if get_y_position() < 80 and get_x_position() < 50 and does_not_have_worm():
    heading(90)

elif get_x_position() < 80 and does_not_have_worm():
    heading(0)

elif does_not_have_worm():
    heading(270)

elif get_y_position() < 80 and get_x_position() > 60:
    heading(90)

elif get_x_position() > 20:
    heading(180)

else:
    heading(270)