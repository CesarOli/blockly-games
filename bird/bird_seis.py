#bird_seis

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

if does_not_have_worm():
    heading(345)

elif get_y_position() < 80:
    heading(90)

else:
    heading(180)
