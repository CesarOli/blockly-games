#bird_oito

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


if get_y_position() < 50 and get_x_position() < 50:
    heading(30)

elif does_not_have_worm():
    heading(330)

elif get_x_position() > 50 and get_y_position() < 50:
    heading(135)

else:
    heading(45)

